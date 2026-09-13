# EduBot — Person 2: Abdul Qudoos

## Role
**AI Tutor, Math & Image Solver**

This module implements Abdul Qudoos's assigned responsibilities:
- AI Tutor
- Beginner / Intermediate / Advanced learning modes
- Teach Me Mode
- Step-by-step Math Solver
- Image/Textbook Question Solver
- Gemini Vision/OCR-style multimodal question reading
- Clear and personalized explanations
- Integration-ready Python functions

## What was improved
The module is now designed as a real working/demo-ready component rather than only a code example.

### 1. AI Tutor
Adapts explanations to three learning levels and validates the selected mode.

### 2. Teach Me Mode
Uses the required loop:
**Explain → Ask Student → Evaluate → Correct/Guide → Follow-up → Continue**

The checking question is explicitly marked as `CHECKING_QUESTION:` and extracted into session state. This avoids losing the question between Streamlit reruns.

### 3. Math Solver
Returns structured sections for given values, required result, formula/method, calculations, verification and final answer.

### 4. Image/Textbook Solver
Accepts JPG/JPEG/PNG/WEBP, validates file type/size, sends the image to Gemini multimodal input, transcribes readable text, and solves the academic question. It is instructed not to guess unreadable content.

### 5. Error handling
API failures are converted into clear feature-specific errors. Input validation covers empty questions, invalid learning modes, missing API keys, unsupported images and oversized uploads.

### 6. Standalone demo
`app_person2.py` provides a complete Streamlit demo for all Person 2 features. It can be run independently before integration into the team's final EduBot application.

## Run
```bash
pip install -r requirements.txt
```

Create `.env`:
```env
GOOGLE_API_KEY=your_google_ai_studio_key
GEMINI_MODEL=gemini-2.5-flash
```

Start the demo:
```bash
streamlit run app_person2.py
```

Run offline unit tests:
```bash
python -m unittest test_ai_tutor.py
```

## Main API
```python
from ai_tutor import (
    create_llm,
    tutor_answer,
    start_teach_me,
    evaluate_teach_me,
    solve_math,
    solve_image_question,
    extract_checking_question,
    TeachMeSession,
)
```

## Integration note
The final team application can import these functions into Samrah's Streamlit frontend. `app_person2.py` is the standalone Person 2 demo, not a replacement for the team's final integrated app.

## Gemini model note
The original project document names Gemini 1.5 Flash, but the code now uses a configurable `GEMINI_MODEL` setting and defaults to the currently available stable `gemini-2.5-flash`. The team can change the environment variable without editing application code.
