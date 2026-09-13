"""Offline unit tests for Person 2 logic.
Run: python -m unittest test_ai_tutor.py
API calls are not required for these tests.
"""
import unittest
from ai_tutor import normalize_level, extract_checking_question, validate_image, tutor_answer

class FakeLLM:
    def invoke(self, messages):
        class R:
            content = "Mock tutor response"
        return R()

class Person2Tests(unittest.TestCase):
    def test_learning_levels(self):
        self.assertEqual(normalize_level("beginner"), "Beginner")
        self.assertEqual(normalize_level("ADVANCED"), "Advanced")
        with self.assertRaises(ValueError):
            normalize_level("Expert")

    def test_question_extraction(self):
        response = "Explain photosynthesis.\nCHECKING_QUESTION: What is chlorophyll?"
        self.assertEqual(extract_checking_question(response), "What is chlorophyll?")

    def test_image_validation(self):
        validate_image(b"123", "image/png")
        with self.assertRaises(ValueError):
            validate_image(b"123", "text/plain")

    def test_tutor_with_fake_llm(self):
        self.assertEqual(tutor_answer(FakeLLM(), "What is a variable?", "Beginner", "Python"), "Mock tutor response")

if __name__ == "__main__":
    unittest.main()
