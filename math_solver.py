"""
EduBot - Mathematical Problem Solver

Standalone wrapper around the Person 2 tutor module.
"""

from ai_tutor import create_llm, solve_math


def solve(problem: str) -> str:
    """Create the configured Gemini LLM and solve a math problem."""
    llm = create_llm()
    return solve_math(llm, problem)


if __name__ == "__main__":
    question = input("Enter a mathematical problem: ").strip()
    print("\nSolution:\n")
    print(solve(question))
