"""
EduBot Gemini LLM configuration.

The PRD specifies:
Google Gemini 1.5 Flash
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


def create_llm():
    """Create the Gemini 1.5 Flash model."""
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY is not set. "
            "Add it to your environment or .env file."
        )

    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0
    )
