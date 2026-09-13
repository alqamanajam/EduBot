
"""EduBot Person 2 — AI Tutor, Math & Image Solver.

Reusable, integration-ready implementation for Abdul Qudoos's assigned role:
AI Tutor, three learning levels, Teach Me Mode, Math Solver, and Image/Textbook
Question Solver using Gemini multimodal models.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import base64
import os
import re

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

LEARNING_MODES = {
    "Beginner": "Use very simple language, define terms, explain one idea at a time, and give an easy example.",
    "Intermediate": "Use balanced detail, explain important terminology, and include useful examples.",
    "Advanced": "Use precise technical terminology, deeper reasoning, edge cases, and advanced examples when useful.",
}


def normalize_level(level: str) -> str:
    value = (level or "Intermediate").strip().title()
    if value not in LEARNING_MODES:
        raise ValueError(f"Invalid learning level: {level}. Choose Beginner, Intermediate, or Advanced.")
    return value


def create_llm(model: Optional[str] = None):
    """Create the configured Gemini model.

    GEMINI_MODEL is configurable so the team can update models without changing code.
    Current stable default is Gemini 2.5 Flash; the project document's older 1.5
    model can still be selected explicitly through GEMINI_MODEL if the account supports it.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is not set. Add it to .env or the deployment secrets.")
    selected = model or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    return ChatGoogleGenerativeAI(model=selected, temperature=0.2, google_api_key=api_key)


def _text(response: Any) -> str:
    content = getattr(response, "content", response)
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and "text" in item:
                parts.append(item["text"])
            elif isinstance(item, str):
                parts.append(item)
        return "\n".join(parts).strip()
    return str(content).strip()


def _invoke(llm, messages, feature: str) -> str:
    try:
        return _text(llm.invoke(messages))
    except Exception as exc:
        raise RuntimeError(f"EduBot {feature} failed: {exc}") from exc

TUTOR_PROMPT = ChatPromptTemplate.from_template("""
You are EduBot, a patient AI personal study tutor.

Student level: {level}
Topic: {topic}
Level instruction: {instruction}

Teach rather than merely outputting an answer. Address the question first, then explain
with short sections, steps, examples, formulas, or analogies when useful. Stay academic,
accurate, and focused. Never invent missing facts. If the question is ambiguous, state
the assumption. End with one short "Quick Check" question when appropriate.

Student question:
{question}
""")

TEACH_START_PROMPT = ChatPromptTemplate.from_template("""
You are EduBot in interactive Teach Me Mode.
Topic: {topic}
Student level: {level}
Level instruction: {instruction}

Follow this exact stage: EXPLAIN -> ASK STUDENT -> WAIT.
Explain only one manageable concept/chunk, then ask exactly ONE short checking question.
Do not answer the checking question. Put the question on its own final line beginning with:
CHECKING_QUESTION:
""")

TEACH_EVAL_PROMPT = ChatPromptTemplate.from_template("""
You are EduBot in interactive Teach Me Mode.
Topic: {topic}
Student level: {level}
Level instruction: {instruction}
Previous lesson:
{previous}

Checking question:
{question}

Student answer:
{answer}

Follow this exact stage: EVALUATE -> CORRECT/GUIDE -> FOLLOW-UP -> CONTINUE.
1. Classify as Correct, Partially Correct, or Incorrect.
2. Explain why briefly.
3. Correct misconceptions and praise what was right.
4. Teach the next small concept.
5. Ask exactly ONE new checking question.
Put the new question on its own final line beginning with:
CHECKING_QUESTION:
""")

MATH_PROMPT = ChatPromptTemplate.from_template("""
You are EduBot's step-by-step Mathematical Problem Solver.

Problem:
{problem}

Return these sections:
### Given
### Required
### Method / Formula
### Step-by-step Solution
### Verification
### Final Answer

Show calculations clearly. Explain reasoning. Do not invent missing values. If ambiguous,
state the assumption. If the problem is not actually mathematical, say that clearly and
explain what information is needed.
""")

IMAGE_PROMPT = """
You are EduBot's Image/Textbook Question Solver.
Analyze the supplied academic image.

Return exactly these sections:
### Question Read from Image
Transcribe only what is readable. Mark unreadable text as [unclear] instead of guessing.

### Topic

### Given / Options

### Step-by-step Solution

### Final Answer

Rules:
- Solve what is actually visible in the image.
- For MCQs, identify the option and explain it.
- For math, show formulas and calculations.
- For diagrams, use visible labels and explain the relevant relationship.
- If the image is unreadable or contains no academic question, say so clearly.
"""


def tutor_answer(llm, question: str, level: str = "Intermediate", topic: str = "General") -> str:
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")
    level = normalize_level(level)
    messages = TUTOR_PROMPT.format_messages(
        level=level, topic=(topic or "General").strip(),
        instruction=LEARNING_MODES[level], question=question.strip()
    )
    return _invoke(llm, messages, "AI Tutor")


def start_teach_me(llm, topic: str, level: str = "Beginner") -> str:
    if not topic or not topic.strip():
        raise ValueError("Topic cannot be empty.")
    level = normalize_level(level)
    messages = TEACH_START_PROMPT.format_messages(
        topic=topic.strip(), level=level, instruction=LEARNING_MODES[level]
    )
    return _invoke(llm, messages, "Teach Me Mode")


def extract_checking_question(response: str) -> str:
    """Reliably extract the model's explicit Teach Me question."""
    text = response or ""
    match = re.search(r"CHECKING_QUESTION\s*:\s*(.+?)(?:\n|$)", text, flags=re.I)
    if match:
        return match.group(1).strip()
    questions = re.findall(r"[^\n?]{5,}\?", text)
    return questions[-1].strip() if questions else ""


def evaluate_teach_me(llm, topic: str, checking_question: str, student_response: str,
                      previous_teaching: str = "", level: str = "Beginner") -> str:
    if not topic.strip() or not student_response.strip():
        raise ValueError("Topic and student response are required.")
    if not checking_question.strip():
        raise ValueError("Checking question is missing. Start the lesson again so EduBot can track it.")
    level = normalize_level(level)
    messages = TEACH_EVAL_PROMPT.format_messages(
        topic=topic.strip(), level=level, instruction=LEARNING_MODES[level],
        previous=previous_teaching.strip(), question=checking_question.strip(),
        answer=student_response.strip()
    )
    return _invoke(llm, messages, "Teach Me evaluation")


def solve_math(llm, problem: str) -> str:
    if not problem or not problem.strip():
        raise ValueError("Mathematical problem cannot be empty.")
    return _invoke(llm, MATH_PROMPT.format_messages(problem=problem.strip()), "Math Solver")


def validate_image(image_bytes: bytes, mime_type: str, max_mb: int = 10) -> None:
    allowed = {"image/jpeg", "image/png", "image/webp", "image/jpg"}
    if not image_bytes:
        raise ValueError("Image data is empty.")
    if mime_type not in allowed:
        raise ValueError("Unsupported image type. Use JPG, JPEG, PNG, or WEBP.")
    if len(image_bytes) > max_mb * 1024 * 1024:
        raise ValueError(f"Image is too large. Maximum allowed size is {max_mb} MB.")


def solve_image_question(llm, image_bytes: bytes, mime_type: str = "image/jpeg") -> str:
    """Use Gemini's multimodal input for OCR/vision + academic solving."""
    validate_image(image_bytes, mime_type)
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    data_url = f"data:{mime_type};base64,{encoded}"
    message = HumanMessage(content=[
        {"type": "text", "text": IMAGE_PROMPT},
        {"type": "image_url", "image_url": {"url": data_url}},
    ])
    return _invoke(llm, [message], "Image/Textbook Solver")


@dataclass
class TeachMeSession:
    """Stateful helper for Streamlit or another frontend."""
    topic: str
    level: str = "Beginner"
    previous_teaching: str = ""
    checking_question: str = ""
    history: List[Dict[str, str]] = field(default_factory=list)

    def update_lesson(self, response: str) -> None:
        self.previous_teaching = response
        self.checking_question = extract_checking_question(response)
        self.history.append({"role": "tutor", "content": response})

    def add_student_answer(self, answer: str) -> None:
        self.history.append({"role": "student", "content": answer})

    def reset(self) -> None:
        self.previous_teaching = ""
        self.checking_question = ""
        self.history.clear()
