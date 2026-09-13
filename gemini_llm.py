"""
EduBot Gemini LLM configuration.

The PRD specifies:
Google Gemini 3.6 Flash
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


def create_llm():
    """Create the Gemini 3.6 Flash model."""
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY is not set. "
            "Add it to your environment or .env file."
        )

        return ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=api_key,
        temperature=0
    )
