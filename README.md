# 🎓 EduBot — AI-Powered Personal Study Assistant

> HEC-NCEAC & PEC Generative & Agentic AI Training | Cohort 11 | Midterm Hackathon 1

---

## ✅ Module Status

| Module | Developer | Status |
|---|---|---|
| 📄 RAG & Document Q&A | Umar Saeed Jan | ✅ Complete |
| 🧑‍🏫 AI Tutor + Teach Me Mode | Abdul Qudoos | ✅ Complete |
| 🔢 Math Solver | Abdul Qudoos | ✅ Complete |
| 🖼️ Image/Textbook Solver | Abdul Qudoos | ✅ Complete |
| 💬 AI Q&A | Alqama (Integration) | ✅ Complete |
| 📃 AI Text Summarizer | Alqama (Integration) | ✅ Complete |
| 📝 Quiz + Interactive Quiz | Samrah | ✅ Complete |
| 📊 Progress Dashboard | Samrah | ✅ Complete |
| 🗺️ Exam Preparation Mode | Full Team | ✅ Complete |
| 🔗 Final Integration + Deployment | Alqama Najam | ✅ Complete |

---

## ✨ Features

- 💬 **AI Q&A** — Ask any academic question with level-based answers
- 📄 **RAG Document Q&A** — Upload PDF, ask questions from it with source citations
- 🧑‍🏫 **AI Tutor** — Personalized explanations at Beginner / Intermediate / Advanced level
- 🎯 **Teach Me Mode** — Interactive: Explain → Ask → Evaluate → Correct → Continue
- 🔢 **Math Solver** — Step-by-step structured math solutions
- 🖼️ **Image Question Solver** — Gemini Vision reads textbook/handwritten questions
- 📃 **AI Text Summarizer** — Summarize notes in multiple styles with download
- 📝 **Quiz Generator** — AI-generated MCQs 
- 📊 **Progress Dashboard** — Score tracking & weak area detection 
- 🗺️ **Exam Preparation Mode** — Full study workflow

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| Language | Python |
| LLM | Google Gemini 2.5 Flash |
| RAG | LangChain + ChromaDB |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| Vision/OCR | Gemini Multimodal Vision |
| Deployment | Streamlit Community Cloud |

---

## 📁 Project Structure

```
EduBot/
├── app.py                  ← Main integrated Streamlit app (Alqama)
├── requirements.txt        ← All dependencies
├── .env.example            ← API key template
├── .gitignore
├── README.md
├── test_rag.py             ← Umar's RAG test
└── modules/
    ├── rag_engine.py       ← PDF processing, embeddings, retrieval (Umar)
    ├── rag_chain.py        ← LangChain RAG chain (Umar)
    ├── rag_prompt.py       ← RAG prompt template (Umar)
    ├── gemini_llm.py       ← Gemini config for RAG (Umar)
    ├── ai_tutor.py         ← AI Tutor, Teach Me, Math, Image (Abdul)
    ├── teach_me_mode.py    ← Teach Me session helper (Abdul)
    ├── math_solver.py      ← Math solver wrapper (Abdul)
    ├── image_solver.py     ← Image solver wrapper (Abdul)
    ├── tutor_prompt.py     ← Tutor prompt library (Abdul)
    └── quiz.py             ← Quiz + Progress (Samrah — in progress)
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/EduBot.git
cd EduBot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
cp .env.example .env
# Add your Google AI Studio API key inside .env

# 4. Run the app
streamlit run app.py
```

---

## 🔑 Environment Variables

```env
GOOGLE_API_KEY=your_google_ai_studio_key_here
GEMINI_MODEL=gemini-3.6-flash
```

Get your free key: https://aistudio.google.com/app/apikey

---

## 👥 Team

| Member | Role |
|---|---|
| **Alqama Najam** | Team Leader, Integration, GitHub & Deployment |
| **Umar Saeed Jan** | RAG & Knowledge Engine |
| **Abdul Qudoos** | AI Tutor, Teach Me Mode, Math Solver, Image Solver |
| **Samrah** | Quiz Generator, Progress Dashboard, UI/UX |
