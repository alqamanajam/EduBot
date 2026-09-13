"""
EduBot - Image/Textbook Question Solver

Gemini Vision is used to read the uploaded image and solve the question.
This supports textbook screenshots, handwritten questions, diagrams with
readable text, and ordinary image-based academic questions.
"""

from pathlib import Path

from ai_tutor import create_llm, solve_image_question


SUPPORTED_IMAGE_TYPES = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
}


def solve_file(image_path: str) -> str:
    """Read an image file and return EduBot's step-by-step solution."""
    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    mime_type = SUPPORTED_IMAGE_TYPES.get(path.suffix.lower())
    if not mime_type:
        raise ValueError(
            "Unsupported image format. Use JPG, JPEG, PNG, or WEBP."
        )

    llm = create_llm()

    with path.open("rb") as file:
        image_bytes = file.read()

    return solve_image_question(llm, image_bytes, mime_type)


if __name__ == "__main__":
    image_path = input("Enter image path: ").strip()
    print("\nSolution:\n")
    print(solve_file(image_path))
