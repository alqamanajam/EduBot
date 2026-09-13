"""
EduBot - AI Tutor, Math Solver & Image Question Solver
Developer: Abdul Qudoos

Provides:
- create_llm()               → configured Gemini chat model
- tutor_answer()              → AI Tutor Q&A
- solve_math()                → Math Solver
- solve_image_question()      → Image Question Solver
- start_teach_me()            → Teach Me Mode: start a lesson
- evaluate_teach_me()         → Teach Me Mode: evaluate student's answer
- extract_checking_question() → pull out the checking question from a response
- TeachMeSession              → convenience session object used by teach_me_mode.py
"""

import os
import re
import base64

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage


# =========================================================
# LLM SETUP
# =========================================================

def create_llm():
    """Create the configured Gemini model for tutoring, math, and image solving."""
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY is not set. "
            "Add it to your environment or .env file."
        )

    return ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=api_key,
        temperature=0.3,
    )


def _ask(llm, prompt: str) -> str:
    """Send a plain text prompt to the LLM and return the text response."""
    response = llm.invoke(prompt)
    return getattr(response, "content", str(response))


# =========================================================
# AI TUTOR
# =========================================================

def tutor_answer(llm, question: str, level: str, topic: str) -> str:
    """Answer a student's question at their chosen level, on their chosen topic."""
    prompt = f"""You are EduBot, a friendly and knowledgeable AI tutor.

Topic: {topic}
Student level: {level}
- Beginner: simple language, many examples, avoid jargon
- Intermediate: balanced explanation with moderate terminology
- Advanced: detailed technical explanation with deeper concepts

Student question: {question}

Rules:
1. Answer clearly and in a student-friendly way
2. Use bullet points or numbered steps when helpful
3. Give examples where useful
4. Stay focused on the given topic and level

Answer:"""
    return _ask(llm, prompt)


# =========================================================
# MATH SOLVER
# =========================================================

def solve_math(llm, problem: str) -> str:
    """Solve a math problem step by step with full explanation."""
    prompt = f"""You are EduBot, an AI math tutor.

Solve the following mathematical problem with full step-by-step working.

Problem: {problem}

Structure your answer with these sections:
- **Given** — What information is provided
- **Required** — What needs to be found
- **Method / Formula** — Which formula or concept applies
- **Step-by-step Solution** — Full calculations with explanation
- **Verification** — Check that the answer is correct
- **Final Answer** — Clearly stated final result

Answer:"""
    return _ask(llm, prompt)


# =========================================================
# IMAGE QUESTION SOLVER
# =========================================================

def solve_image_question(llm, image_bytes: bytes, image_type: str) -> str:
    """Read a question from an image and solve it step by step."""
    b64_image = base64.b64encode(image_bytes).decode("utf-8")

    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": (
                    "You are EduBot, an AI tutor. Read the question in this image "
                    "carefully, then solve it fully.\n\n"
                    "Structure your answer as:\n"
                    "- **Question Read from Image** — transcribe the question\n"
                    "- **Topic** — subject/topic identified\n"
                    "- **Given / Options** — data or MCQ options if present\n"
                    "- **Step-by-step Solution** — full working\n"
                    "- **Final Answer** — clear result"
                ),
            },
            {
                "type": "image_url",
                "image_url": f"data:{image_type};base64,{b64_image}",
            },
        ]
    )

    response = llm.invoke([message])
    return getattr(response, "content", str(response))


# =========================================================
# TEACH ME MODE
# =========================================================

def start_teach_me(llm, topic: str, level: str) -> str:
    """Start a Teach Me Mode lesson: explain one concept, then ask a checking question."""
    prompt = f"""You are EduBot, running "Teach Me Mode" — an interactive teaching workflow.

Topic: {topic}
Student level: {level}

Instructions:
1. Explain ONE key concept about this topic, appropriate for the student's level.
2. Keep the explanation focused and not too long.
3. At the end, ask exactly ONE short checking question to test the student's understanding
   of what you just explained.
4. Clearly mark the checking question by starting it on its own line with "CHECKING QUESTION:".

Begin the lesson now."""
    return _ask(llm, prompt)


def evaluate_teach_me(
    llm,
    topic: str,
    checking_question: str,
    student_response: str,
    previous_teaching: str,
    level: str,
) -> str:
    """Evaluate the student's answer, correct misconceptions, and continue the lesson."""
    prompt = f"""You are EduBot, running "Teach Me Mode" for topic: {topic}
Student level: {level}

Previous teaching:
{previous_teaching}

Checking question you asked: {checking_question}
Student's answer: {student_response}

Instructions:
1. Evaluate whether the student's answer is correct, partially correct, or incorrect.
2. Give clear, encouraging feedback and correct any misconceptions.
3. Then teach the NEXT concept in this topic (one concept at a time).
4. End with exactly ONE new checking question, marked on its own line starting with
   "CHECKING QUESTION:".

Continue the lesson now."""
    return _ask(llm, prompt)


def extract_checking_question(response: str) -> str:
    """Pull the checking question out of a Teach Me Mode response."""
    match = re.search(r"CHECKING QUESTION:\s*(.+)", response, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Fallback: last line ending in a question mark
    lines = [line.strip() for line in response.strip().splitlines() if line.strip()]
    for line in reversed(lines):
        if line.endswith("?"):
            return line

    return ""


class TeachMeSession:
    """Convenience object that tracks the state of a Teach Me Mode session."""

    def __init__(self, topic: str, level: str = "Beginner"):
        self.topic = topic
        self.level = level
        self.previous_teaching = ""
        self.checking_question = ""
        self.history = []

    def update_lesson(self, response: str):
        self.previous_teaching = response
        self.checking_question = extract_checking_question(response)
        self.history.append({"role": "tutor", "content": response})

    def add_student_answer(self, student_response: str):
        self.history.append({"role": "student", "content": student_response})
