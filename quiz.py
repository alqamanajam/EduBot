"""
EduBot - Person 3: Quiz & Progress Module
Developer: Samrah

Responsibilities:
- MCQ Quiz Generator
- Interactive Quiz UI
- Score Calculation
- Weak Area Detection
- Progress Dashboard
- Exam Preparation Mode
"""

import json
import re


def generate_quiz(llm, topic: str, num_questions: int = 5, difficulty: str = "Medium"):
    """
    Topic pe MCQ quiz generate karo using the Gemini LLM.

    Returns a list of dicts like:
    [
        {
            "question": "What is ...?",
            "options": {"A": "...", "B": "...", "C": "...", "D": "..."},
            "correct": "B",
            "explanation": "..."
        },
        ...
    ]
    """
    prompt = f"""You are EduBot, an AI that creates multiple-choice quizzes for students.

Create exactly {num_questions} multiple-choice questions on the topic: "{topic}".
Difficulty level: {difficulty}

Return ONLY valid JSON (no markdown, no extra text, no code fences) in this exact format:

[
  {{
    "question": "question text here",
    "options": {{"A": "option A text", "B": "option B text", "C": "option C text", "D": "option D text"}},
    "correct": "A",
    "explanation": "short explanation of why this is correct"
  }}
]

Rules:
- Exactly 4 options per question (A, B, C, D)
- Only one correct answer per question
- Questions must match the difficulty level
- Do not include anything outside the JSON array
"""

    response = llm.invoke(prompt)
    text = getattr(response, "content", str(response))

    # Strip markdown code fences if the model added them anyway
    text = text.strip()
    text = re.sub(r"^```(json)?", "", text).strip()
    text = re.sub(r"```$", "", text).strip()

    try:
        questions = json.loads(text)
        return questions
    except json.JSONDecodeError:
        # Try to extract the JSON array if there's stray text around it
        match = re.search(r"\[.*\]", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass
        raise ValueError("Could not parse quiz JSON from the model's response.")


def calculate_score(answers: list, correct_answers: list) -> float:
    """
    Score calculate karo.
    answers / correct_answers are lists of option letters, e.g. ["A", "C", "B"]
    Returns percentage score (0-100).
    """
    if not correct_answers:
        return 0.0

    correct_count = sum(
        1 for given, correct in zip(answers, correct_answers) if given == correct
    )
    return round((correct_count / len(correct_answers)) * 100, 1)


def detect_weak_areas(quiz_results: list) -> list:
    """
    Weak topics dhundo quiz results se.

    quiz_results: list of dicts like:
    [{"topic": "Algebra", "correct": False}, {"topic": "Algebra", "correct": True}, ...]

    Returns list of topics where the student got more wrong than right.
    """
    topic_stats = {}

    for result in quiz_results:
        topic = result.get("topic", "General")
        is_correct = result.get("correct", False)

        if topic not in topic_stats:
            topic_stats[topic] = {"correct": 0, "total": 0}

        topic_stats[topic]["total"] += 1
        if is_correct:
            topic_stats[topic]["correct"] += 1

    weak_areas = []
    for topic, stats in topic_stats.items():
        accuracy = stats["correct"] / stats["total"] if stats["total"] else 0
        if accuracy < 0.5:
            weak_areas.append(topic)

    return weak_areas
