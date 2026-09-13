## 🎓 EduBot — AI-Powered Personal Study Assistant

> Built for **HEC-NCEAC GenAI Cohort 11 — Midterm Hackathon 1**

EduBot is an all-in-one AI study companion built with **Streamlit** and **Google Gemini**. It helps students learn faster by combining conversational Q&A, document-grounded answers, personalized tutoring, step-by-step problem solving, and self-testing — all in a single, unified app.

**🔗 Live App:** [edubot-grfqnwapwgywf4n2ze5mwn.streamlit.app](https://edubot-grfqnwapwgywf4n2ze5mwn.streamlit.app)

---

## ✨ Features

| Feature | Description | Status |
|---|---|---|
| 💬 **AI Q&A** | Ask any academic question and get level-adjusted explanations | ✅ Ready |
| 📄 **Document Q&A (RAG)** | Upload a PDF and ask questions grounded strictly in its content | ✅ Ready |
| 🧑‍🏫 **AI Tutor** | Subject/topic-based conversational tutoring at your chosen level | ✅ Ready |
| 🎯 **Teach Me Mode** | Interactive teach → check → evaluate → continue learning loop | ✅ Ready |
| 🔢 **Math Solver** | Step-by-step math solutions with verification | ✅ Ready |
| 🖼️ **Image Question Solver** | Upload a photo of a question (textbook/handwritten) and get it solved | ✅ Ready |
| 📝 **Quiz Generator** | AI-generated MCQ quizzes with live scoring and weak-area detection | ✅ Ready |
| 📊 **Progress Dashboard** | Visual tracking of study streaks, accuracy, and subject progress | ✅ Ready |
| 🗺️ **Exam Preparation Mode** | Guided workflow across Study → Practice → Quiz → Review | ✅ Ready |
| 📃 **AI Text Summarizer** | Summarize notes or chapters into concise, revision-ready points | ✅ Ready |

---

## 🧱 Tech Stack

- **Frontend / App Framework:** Streamlit
- **LLM:** Google Gemini (`gemini-3.6-flash`) via `langchain-google-genai` & `google-generativeai`
- **RAG / Knowledge Engine:** LangChain, ChromaDB, `sentence-transformers`, `pypdf`
- **Orchestration:** LangGraph
- **Language:** Python 3.14

---

## 📂 Project Structure

```
EduBot/
├── app.py                # Main Streamlit entry point & page routing
├── home.py                # Home dashboard UI
├── ai_tutor.py            # AI Tutor, Math Solver, Image Solver, Teach Me Mode logic
├── teach_me_mode.py        # Convenience wrapper for Teach Me Mode sessions
├── rag_engine.py           # PDF chunking, embeddings & vector store (RAG)
├── rag_chain.py             # RAG retrieval chain
├── rag_prompt.py             # RAG prompt templates
├── gemini_llm.py              # Gemini LLM configuration for RAG
├── quiz.py                     # MCQ generation, scoring, weak-area detection
├── progress.py                   # Progress Dashboard UI & data
├── styles.py                       # Global custom CSS / design system
├── components.py                     # Shared UI components
├── requirements.txt                    # Python dependencies
├── .env.example                          # Environment variable template
└── README.md
```

---

## 👥 Team

| Member | Responsibility |
|---|---|
| **Alqama Najam** | Team Lead — Integration, deployment, UI/UX |
| **Umar Saeed Jan** | RAG & Knowledge Engine |
| **Abdul Qudoos** | AI Tutor, Math Solver, Image Question Solver |
| **Samrah** | Quiz Generator, Progress Dashboard, UI styling |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

```bash
git clone https://github.com/alqamanajam/EduBot.git
cd EduBot
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
```

### Configuration

Copy the example environment file and add your API key:

```bash
copy .env.example .env       # Windows
cp .env.example .env         # macOS/Linux
```

Edit `.env`:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Run Locally

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## ☁️ Deployment

EduBot is deployed on **Streamlit Community Cloud**.

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select the repository, branch (`main`), and main file (`app.py`)
4. Under **Advanced settings → Secrets**, add:
   ```toml
   GOOGLE_API_KEY = "your_gemini_api_key_here"
   ```
5. Click **Deploy**

---

## 🗺️ Roadmap

- [ ] Personalized practice-question generation for detected weak areas
- [ ] Multi-language support for explanations
- [ ] Exportable progress reports
- [ ] Collaborative study rooms

---

## 📄 License

This project was built for academic purposes as part of the **HEC-NCEAC Generative & Agentic AI Training — Cohort 11**.
## 👥 Team

| Member | Role |
|---|---|
| **Alqama Najam** | Team Leader, Integration, GitHub & Deployment |
| **Umar Saeed Jan** | RAG & Knowledge Engine |
| **Abdul Qudoos** | AI Tutor, Teach Me Mode, Math Solver, Image Solver |
| **Samrah** | Quiz Generator, Progress Dashboard, UI/UX |
