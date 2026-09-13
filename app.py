"""
EduBot — AI-Powered Personal Study Assistant
Team Leader / Integration: Alqama Najam

Modules:
- RAG & Knowledge Engine      → Umar Saeed Jan   (rag_engine.py)
- AI Tutor, Math & Image      → Abdul Qudoos     (ai_tutor.py)
- Quiz, Progress & UI         → Samrah           (quiz.py)
"""

import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

load_dotenv()
load_dotenv()

from styles import apply_styles
apply_styles()
# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="EduBot – AI Study Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.image("https://img.icons8.com/fluency/96/graduation-cap.png", width=80)
st.sidebar.title("📚 EduBot")
st.sidebar.markdown("*Your AI-Powered Study Assistant*")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "💬 AI Q&A",
        "📄 Document Q&A (RAG)",
        "🧑‍🏫 AI Tutor",
        "🎯 Teach Me Mode",
        "🔢 Math Solver",
        "🖼️ Image Question Solver",
        "📝 Quiz Generator",
        "📊 Progress Dashboard",
        "🗺️ Exam Preparation",
        "📃 AI Text Summarizer",
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("👥 Team: Alqama | Umar | Abdul | Samrah")
st.sidebar.caption("🏆 HEC-NCEAC GenAI Cohort 11")

# ── API Key Check Helper ──────────────────────────────────────────────────────
def check_api_key():
    if not os.getenv("GOOGLE_API_KEY"):
        st.error("⚠️ GOOGLE_API_KEY not found. Please set it in your .env file.")
        st.info("Get your free key at: https://aistudio.google.com/app/apikey")
        st.stop()

# ── Direct Gemini Call (for Q&A and Summarizer) ───────────────────────────────
def call_gemini_direct(prompt: str) -> str:
    try:
        try:
            import google.generativeai as genai
        except ImportError:
            return ("❌ Error: 'google.generativeai' package not installed. "
                    "Install it with: pip install google-generativeai")
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model_name = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return getattr(response, "text", str(response))
    except Exception as e:
        return f"❌ Error: {e}"

# ── LLM Instance (Abdul's module) ─────────────────────────────────────────────
@st.cache_resource
def get_llm():
    from ai_tutor import create_llm
    return create_llm()

# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
if menu == "🏠 Home":
    try:
        from home import home_page
        home_page()
    except Exception as e:
        st.error(f"❌ Module load error: {e}")

# ══════════════════════════════════════════════════════════════════════════════
# AI Q&A
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "💬 AI Q&A":
    st.markdown(
        """
        <div class="page-header">
            <div class="page-header-icon">💬</div>
            <h1>AI-Powered Q&A</h1>
            <p>Ask Anything, EduBot will Explain.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    check_api_key()

    level = st.selectbox("Select your level:", ["Beginner", "Intermediate", "Advanced"])

    if "qa_history" not in st.session_state:
        st.session_state.qa_history = []

    question = st.text_input("🎓 Ask your academic question:")

    if st.button("Ask EduBot", type="primary") and question.strip():
        with st.spinner("🤔 EduBot is thinking..."):
            prompt = f"""You are EduBot, a friendly and helpful AI study assistant.

Student level: {level}
- Beginner: simple language, many examples, avoid jargon
- Intermediate: balanced explanation with moderate terminology
- Advanced: detailed technical explanation with deeper concepts

Rules:
1. Answer clearly and in a student-friendly way
2. Use bullet points or numbered steps when helpful
3. Give examples where useful
4. End with one short Quick Check question to test understanding

Student question: {question}

Answer:"""
            answer = call_gemini_direct(prompt)
            st.session_state.qa_history.append({"q": question, "a": answer})

        for item in reversed(st.session_state.qa_history):
        st.markdown(
            f"""
            <div class="qa-answer-card">
                <div class="qa-question">🙋 {item['q']}</div>
                <div class="qa-answer-label">EduBot's Answer</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(item["a"])

# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT Q&A —  ✅
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "📄 Document Q&A (RAG)":
    st.title("📄 Document Q&A")
    st.markdown("Apna PDF upload karo — phir ussi se sawal karo. EduBot sirf tumhare document se answer dega.")
    check_api_key()

    uploaded_file = st.file_uploader("📂 Upload your PDF", type=["pdf"])

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        if "vectorstore" not in st.session_state or st.session_state.get("last_file") != uploaded_file.name:
            with st.spinner("⏳ Building knowledge base from your PDF... (~30 seconds)"):
                try:
                    from rag_engine import build_knowledge_base, get_retriever
                    from gemini_llm import create_llm as rag_llm
                    from rag_chain import create_rag_chain

                    vectorstore, chunks = build_knowledge_base(tmp_path)
                    retriever = get_retriever(vectorstore, top_k=4)
                    llm = rag_llm()
                    rag_chain = create_rag_chain(retriever, llm)

                    st.session_state.vectorstore = vectorstore
                    st.session_state.rag_chain = rag_chain
                    st.session_state.last_file = uploaded_file.name
                    st.success(f"✅ Knowledge base ready! ({len(chunks)} chunks from your PDF)")
                except Exception as e:
                    st.error(f"❌ Error building knowledge base: {e}")
                    st.stop()
        else:
            st.success(f"✅ Knowledge base ready: **{uploaded_file.name}**")

        st.markdown("---")
        question = st.text_input("💬 Ask a question from your document:")

        if st.button("🔍 Get Answer", type="primary") and question.strip():
            with st.spinner("🤔 EduBot is searching your document..."):
                try:
                    from rag_engine import get_sources
                    response = st.session_state.rag_chain.invoke(question)
                    docs = st.session_state.vectorstore.similarity_search(question, k=4)
                    sources = get_sources(docs)

                    st.markdown("### 📖 Answer:")
                    st.write(response.content)

                    if sources:
                        st.markdown("**📌 Sources from your document:**")
                        for s in sources:
                            pg = s["page"] if s["page"] else "?"
                            st.caption(f"• {s['source']} — Page {pg}")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

# ══════════════════════════════════════════════════════════════════════════════
# AI TUTOR —✅
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "🧑‍🏫 AI Tutor":
    st.title("🧑‍🏫 AI Tutor")
    st.markdown("Apna level choose karo, topic batao, sawal karo — EduBot tumhare level pe explain karega.")
    check_api_key()

    try:
        from ai_tutor import tutor_answer
        llm = get_llm()
    except Exception as e:
        st.error(f"❌ Module load error: {e}")
        st.stop()

    col1, col2 = st.columns(2)
    with col1:
        level = st.selectbox("🎯 Learning Level:", ["Beginner", "Intermediate", "Advanced"])
    with col2:
        topic = st.text_input("📚 Topic:", placeholder="e.g. Python, Photosynthesis, Newton's Laws")

    question = st.text_area("💬 Your Question:", height=120,
                            placeholder="e.g. What is a function in Python?")

    if st.button("Ask EduBot", type="primary") and question.strip():
        if not topic.strip():
            st.warning("Please enter a topic first.")
        else:
            with st.spinner("🤔 EduBot is teaching..."):
                try:
                    answer = tutor_answer(llm, question, level, topic)
                    st.markdown("### 📖 EduBot's Explanation:")
                    st.markdown(answer)
                except Exception as e:
                    st.error(f"❌ Error: {e}")

    with st.expander("ℹ️ About Learning Levels"):
        st.markdown("""
        - **Beginner** — Simple language, definitions, easy examples
        - **Intermediate** — Balanced detail, terminology, examples
        - **Advanced** — Technical depth, precise terminology, advanced reasoning
        """)

# ══════════════════════════════════════════════════════════════════════════════
# TEACH ME MODE — ✅
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "🎯 Teach Me Mode":
    st.title("🎯 Teach Me Mode")
    st.markdown("EduBot sikhata hai → sawal karta hai → tumhara jawab evaluate karta hai → aage badhta hai.")
    check_api_key()

    try:
        from ai_tutor import (
            start_teach_me, evaluate_teach_me, extract_checking_question
        )
        llm = get_llm()
    except Exception as e:
        st.error(f"❌ Module load error: {e}")
        st.stop()

    col1, col2 = st.columns(2)
    with col1:
        level = st.selectbox("🎯 Learning Level:", ["Beginner", "Intermediate", "Advanced"], key="teach_level")
    with col2:
        topic = st.text_input("📚 Topic to Learn:", "Photosynthesis", key="teach_topic")

    # Session state init
    for key in ["teach_active", "teach_question", "teach_previous", "teach_history"]:
        if key not in st.session_state:
            st.session_state[key] = False if key == "teach_active" else ([] if key == "teach_history" else "")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("▶️ Start / Restart Lesson", type="primary"):
            if not topic.strip():
                st.warning("Please enter a topic first.")
            else:
                with st.spinner("📖 Starting your lesson..."):
                    try:
                        response = start_teach_me(llm, topic, level)
                        st.session_state.teach_active = True
                        st.session_state.teach_previous = response
                        st.session_state.teach_question = extract_checking_question(response)
                        st.session_state.teach_history = [{"role": "tutor", "content": response}]
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error: {e}")
    with c2:
        if st.button("🔄 Reset"):
            for key in ["teach_active", "teach_question", "teach_previous", "teach_history"]:
                st.session_state[key] = False if key == "teach_active" else ([] if key == "teach_history" else "")
            st.rerun()

    if st.session_state.teach_active:
        st.markdown("---")

        # Show lesson history
        for item in st.session_state.teach_history:
            if item["role"] == "tutor":
                with st.chat_message("assistant"):
                    st.markdown(item["content"])
            else:
                with st.chat_message("user"):
                    st.markdown(item["content"])

        # Current checking question
        if st.session_state.teach_question:
            st.info(f"📝 **EduBot's Question:** {st.session_state.teach_question}")
        else:
            st.warning("⚠️ EduBot could not detect a checking question. Please restart the lesson.")

        st.markdown("---")
        answer = st.text_area("✍️ Your Answer:", height=100, key="teach_answer")

        if st.button("Submit Answer ➡️", type="primary") and answer.strip():
            if not st.session_state.teach_question:
                st.error("Please restart the lesson — checking question is missing.")
            else:
                with st.spinner("🤔 Evaluating your answer and continuing..."):
                    try:
                        response = evaluate_teach_me(
                            llm,
                            topic=topic,
                            checking_question=st.session_state.teach_question,
                            student_response=answer,
                            previous_teaching=st.session_state.teach_previous,
                            level=level,
                        )
                        st.session_state.teach_history.append({"role": "student", "content": answer})
                        st.session_state.teach_history.append({"role": "tutor", "content": response})
                        st.session_state.teach_previous = response
                        st.session_state.teach_question = extract_checking_question(response)
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error: {e}")

    with st.expander("ℹ️ How Teach Me Mode Works"):
        st.markdown("""
        **Workflow:**
        1. 📖 **Explain** — EduBot explains one concept at a time
        2. ❓ **Ask** — EduBot asks you a checking question
        3. ✅ **Evaluate** — EduBot evaluates your answer
        4. 🔧 **Correct/Guide** — EduBot corrects misconceptions
        5. ➡️ **Follow-up** — EduBot continues to the next concept
        6. 🔁 **Repeat** until topic is covered
        """)

# ══════════════════════════════════════════════════════════════════════════════
# MATH SOLVER  ✅
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "🔢 Math Solver":
    st.title("🔢 Math Solver")
    st.markdown("Math problem likho — EduBot step-by-step solve karega with full explanation.")
    check_api_key()

    try:
        from ai_tutor import solve_math
        llm = get_llm()
    except Exception as e:
        st.error(f"❌ Module load error: {e}")
        st.stop()

    problem = st.text_area(
        "📝 Enter your mathematical problem:",
        height=150,
        placeholder="e.g. Solve 2x + 5 = 17\ne.g. Find the derivative of x³ + 2x² - 5\ne.g. A train travels 120km in 2 hours, find speed"
    )

    if st.button("🔢 Solve Step-by-Step", type="primary") and problem.strip():
        with st.spinner("🧮 Solving your problem..."):
            try:
                solution = solve_math(llm, problem)
                st.markdown("### 📊 Solution:")
                st.markdown(solution)
            except Exception as e:
                st.error(f"❌ Error: {e}")

    with st.expander("ℹ️ What EduBot shows in the solution"):
        st.markdown("""
        - **Given** — What information is provided
        - **Required** — What needs to be found
        - **Method / Formula** — Which formula or concept to use
        - **Step-by-step Solution** — Full calculations with explanation
        - **Verification** — Check if the answer is correct
        - **Final Answer** — Clear final result
        """)

# ══════════════════════════════════════════════════════════════════════════════
# IMAGE QUESTION SOLVER  ✅
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "🖼️ Image Question Solver":
    st.title("🖼️ Image Question Solver")
    st.markdown("Textbook, handwritten, ya screenshot wala sawal upload karo — EduBot padh ke solve karega.")
    check_api_key()

    try:
        from ai_tutor import solve_image_question
        llm = get_llm()
    except Exception as e:
        st.error(f"❌ Module load error: {e}")
        st.stop()

    st.info("📌 Supported formats: JPG, JPEG, PNG, WEBP (Max 10MB)")

    img = st.file_uploader(
        "📷 Upload image of your question:",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if img:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(img, caption="Your uploaded question", use_column_width=True)
        with col2:
            st.markdown("**File details:**")
            st.write(f"• Name: {img.name}")
            st.write(f"• Type: {img.type}")
            st.write(f"• Size: {round(img.size / 1024, 1)} KB")

            if st.button("🔍 Read & Solve", type="primary"):
                with st.spinner("👁️ EduBot is reading and solving your image..."):
                    try:
                        solution = solve_image_question(llm, img.getvalue(), img.type)
                        st.markdown("---")
                        st.markdown("### 📖 Solution:")
                        st.markdown(solution)
                    except Exception as e:
                        st.error(f"❌ Error: {e}")

    with st.expander("ℹ️ What EduBot reads from the image"):
        st.markdown("""
        - **Question Read from Image** — Transcribed text from the image
        - **Topic** — Subject/topic identified
        - **Given / Options** — Data or MCQ options
        - **Step-by-step Solution** — Full working
        - **Final Answer** — Clear result
        """)

# ══════════════════════════════════════════════════════════════════════════════
# QUIZ GENERATOR — (Placeholder)
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "📝 Quiz Generator":
    st.title("📝 Quiz Generator")
    st.markdown("Kisi bhi topic pe MCQ quiz generate karo aur khud ko test karo.")
    check_api_key()

    try:
        from quiz import generate_quiz, calculate_score, detect_weak_areas
        llm = get_llm()
    except Exception as e:
        st.error(f"❌ Module load error: {e}")
        st.stop()

    for key in ["quiz_questions", "quiz_submitted", "quiz_topic"]:
        if key not in st.session_state:
            st.session_state[key] = None if key != "quiz_submitted" else False

    col1, col2 = st.columns(2)
    with col1:
        topic = st.text_input("Enter topic for quiz:", placeholder="e.g. Photosynthesis")
    with col2:
        difficulty = st.selectbox("Difficulty:", ["Easy", "Medium", "Hard"])
    num_q = st.slider("Number of questions:", 3, 10, 5)

    if st.button("🎲 Generate Quiz", type="primary"):
        if not topic.strip():
            st.warning("Please enter a topic first.")
        else:
            with st.spinner("🧠 EduBot is generating your quiz..."):
                try:
                    questions = generate_quiz(llm, topic, num_q, difficulty)
                    st.session_state.quiz_questions = questions
                    st.session_state.quiz_topic = topic
                    st.session_state.quiz_submitted = False
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error generating quiz: {e}")

    if st.session_state.quiz_questions and not st.session_state.quiz_submitted:
        st.markdown("---")
        st.markdown(f"### 📝 Quiz: {st.session_state.quiz_topic}")

        user_answers = []
        for i, q in enumerate(st.session_state.quiz_questions):
            st.markdown(f"**Q{i+1}. {q['question']}**")
            choice = st.radio(
                f"Select answer for Q{i+1}",
                options=list(q["options"].keys()),
                format_func=lambda k, opts=q["options"]: f"{k}. {opts[k]}",
                key=f"quiz_q_{i}",
                label_visibility="collapsed",
            )
            user_answers.append(choice)
            st.markdown("")

        if st.button("✅ Submit Quiz", type="primary"):
            st.session_state.quiz_user_answers = user_answers
            st.session_state.quiz_submitted = True
            st.rerun()

    if st.session_state.quiz_submitted and st.session_state.quiz_questions:
        st.markdown("---")
        questions = st.session_state.quiz_questions
        user_answers = st.session_state.quiz_user_answers
        correct_answers = [q["correct"] for q in questions]

        score = calculate_score(user_answers, correct_answers)
        st.markdown(f"### 🏆 Your Score: {score}%")
        st.progress(score / 100)

        quiz_results = []
        for i, q in enumerate(questions):
            is_correct = user_answers[i] == q["correct"]
            quiz_results.append({"topic": st.session_state.quiz_topic, "correct": is_correct})

            with st.container(border=True):
                icon = "✅" if is_correct else "❌"
                st.markdown(f"{icon} **Q{i+1}. {q['question']}**")
                st.caption(f"Your answer: {user_answers[i]}. {q['options'][user_answers[i]]}")
                if not is_correct:
                    st.caption(f"Correct answer: {q['correct']}. {q['options'][q['correct']]}")
                st.caption(f"💡 {q.get('explanation', '')}")

        weak_areas = detect_weak_areas(quiz_results)
        if weak_areas:
            st.warning(f"🎯 Weak areas detected: {', '.join(weak_areas)} — consider reviewing these with AI Tutor.")
        else:
            st.success("🎉 Great job! No weak areas detected in this quiz.")

        if st.button("🔄 Try Another Quiz"):
            st.session_state.quiz_questions = None
            st.session_state.quiz_submitted = False
            st.rerun()
# ══════════════════════════════════════════════════════════════════════════════
# PROGRESS DASHBOARD —  (Placeholder)
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "📊 Progress Dashboard":
    try:
        from progress import progress_page
        progress_page()
    except Exception as e:
        st.error(f"❌ Module load error: {e}")
# ══════════════════════════════════════════════════════════════════════════════
# EXAM PREPARATION MODE
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "🗺️ Exam Preparation":
    st.title("🗺️ Exam Preparation Mode")
    st.markdown("Complete workflow: Study → Revision → Practice → Quiz → Analysis → Weak-Area Practice → Re-Test")
    st.info("🔧 Yeh integrated module sabse last mein complete hoga jab Samrah ka Quiz module ready ho.")

    st.markdown("---")
    st.markdown("### 📋 Your Exam Prep Journey:")

    steps = [
        ("📖", "Study", "Document Q&A (RAG)", "Upload your PDF and ask EduBot to explain key concepts"),
        ("🔄", "Revision", "AI Text Summarizer", "Summarize your notes into concise key points"),
        ("🧑‍🏫", "Learn", "AI Tutor + Teach Me Mode", "Learn difficult concepts with EduBot at your level"),
        ("✏️", "Practice", "Math & Image Solver", "Solve practice problems step by step"),
        ("📝", "Quiz", "Quiz Generator", "Test yourself with AI-generated MCQs (Coming Soon)"),
        ("📊", "Analysis", "Progress Dashboard", "Check your score and identify weak areas (Coming Soon)"),
        ("🎯", "Targeted Practice", "Personalized Questions", "Practice weak topics with custom questions (Coming Soon)"),
        ("✅", "Re-Test", "Quiz Generator", "Take another quiz to confirm improvement (Coming Soon)"),
    ]

    for i, (icon, title, feature, desc) in enumerate(steps, 1):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown(f"### {icon}")
        with col2:
            st.markdown(f"**Step {i} — {title}** *(via {feature})*")
            st.caption(desc)
        st.markdown("---")

# ══════════════════════════════════════════════════════════════════════════════
# AI TEXT SUMMARIZER ✅
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "📃 AI Text Summarizer":
    st.title("📃 AI Text Summarizer")
    st.markdown("Notes, chapter, ya article paste karo — EduBot concise key points mein summarize karega.")
    check_api_key()

    text_input = st.text_area("📋 Paste your text here (notes, chapter, article):", height=250)

    summary_style = st.selectbox(
        "Summary style:",
        [
            "Concise bullet points",
            "Short paragraph summary",
            "Detailed with key concepts highlighted",
            "Simple language (Beginner-friendly)",
        ]
    )

    if st.button("📃 Summarize", type="primary") and text_input.strip():
        with st.spinner("✍️ EduBot is summarizing..."):
            prompt = f"""You are EduBot, an AI study assistant.

Summarize the following text for a student.
Summary style: {summary_style}

Rules:
1. Be concise and capture all important points
2. Use bullet points if style requests it
3. Make it student-friendly and easy to revise from
4. Do not add anything not in the original text
5. Do not mention these instructions

Text to summarize:
{text_input}

Summary:"""
            summary = call_gemini_direct(prompt)

            st.markdown("### 📝 Summary:")
            st.markdown(summary)

            st.download_button(
                label="⬇️ Download Summary as .txt",
                data=summary,
                file_name="EduBot_Summary.txt",
                mime="text/plain"
            )
