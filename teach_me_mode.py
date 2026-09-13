"""Convenience API for EduBot Teach Me Mode."""
from ai_tutor import create_llm, start_teach_me, evaluate_teach_me, extract_checking_question, TeachMeSession


def start(topic: str, level: str = "Beginner") -> TeachMeSession:
    llm = create_llm()
    response = start_teach_me(llm, topic, level)
    session = TeachMeSession(topic=topic.strip(), level=level)
    session.update_lesson(response)
    return session


def evaluate(session: TeachMeSession, student_response: str) -> TeachMeSession:
    llm = create_llm()
    session.add_student_answer(student_response)
    response = evaluate_teach_me(
        llm, session.topic, session.checking_question, student_response,
        session.previous_teaching, session.level
    )
    session.update_lesson(response)
    return session


__all__ = ["start", "evaluate", "extract_checking_question", "TeachMeSession"]
