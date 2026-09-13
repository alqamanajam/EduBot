"""Standalone Streamlit demo for Abdul Qudoos's complete Person 2 module.
Run: streamlit run app_person2.py
"""
import streamlit as st
from ai_tutor import create_llm, tutor_answer, solve_math, solve_image_question, start_teach_me, evaluate_teach_me, extract_checking_question

st.set_page_config(page_title="EduBot — Abdul Qudoos", page_icon="🎓", layout="wide")
st.title("🎓 EduBot — AI Tutor, Math & Image Solver")
st.caption("Person 2: Abdul Qudoos | AI Tutor • Learning Modes • Teach Me • Math • Vision")

try:
    llm = create_llm()
except Exception as exc:
    st.error(str(exc))
    st.info("Create a .env file with GOOGLE_API_KEY=your_key, or add the key to Streamlit secrets.")
    st.stop()

module = st.sidebar.radio("Choose Module", ["AI Tutor", "Teach Me Mode", "Math Solver", "Image/Textbook Solver"])

if module == "AI Tutor":
    level = st.selectbox("Learning Level", list(["Beginner", "Intermediate", "Advanced"]))
    topic = st.text_input("Topic", "Python")
    question = st.text_area("Ask EduBot", height=140, placeholder="e.g. What is a Python function?")
    if st.button("Ask EduBot", type="primary") and question.strip():
        with st.spinner("EduBot is teaching..."):
            st.markdown(tutor_answer(llm, question, level, topic))

elif module == "Teach Me Mode":
    level = st.selectbox("Learning Level", ["Beginner", "Intermediate", "Advanced"], key="teach_level")
    topic = st.text_input("Topic", "Photosynthesis", key="teach_topic")
    if "teach_active" not in st.session_state:
        st.session_state.teach_active = False
    if "teach_question" not in st.session_state:
        st.session_state.teach_question = ""
    if "teach_previous" not in st.session_state:
        st.session_state.teach_previous = ""

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Start / Restart Lesson", type="primary"):
            with st.spinner("Starting lesson..."):
                response = start_teach_me(llm, topic, level)
            st.session_state.teach_active = True
            st.session_state.teach_previous = response
            st.session_state.teach_question = extract_checking_question(response)
            st.rerun()
    with c2:
        if st.button("Reset"):
            st.session_state.teach_active = False
            st.session_state.teach_question = ""
            st.session_state.teach_previous = ""
            st.rerun()

    if st.session_state.teach_active:
        st.markdown(st.session_state.teach_previous)
        st.caption("Current checking question: " + (st.session_state.teach_question or "Not detected — restart lesson."))
        answer = st.text_area("Your Answer", height=120)
        if st.button("Submit Answer") and answer.strip():
            if not st.session_state.teach_question:
                st.error("EduBot could not track the checking question. Please restart the lesson.")
            else:
                with st.spinner("Evaluating your answer and continuing..."):
                    response = evaluate_teach_me(
                        llm, topic, st.session_state.teach_question, answer,
                        st.session_state.teach_previous, level
                    )
                st.session_state.teach_previous = response
                st.session_state.teach_question = extract_checking_question(response)
                st.rerun()

elif module == "Math Solver":
    problem = st.text_area("Mathematical Problem", height=160, placeholder="e.g. Solve 2x + 5 = 17")
    if st.button("Solve Step-by-Step", type="primary") and problem.strip():
        with st.spinner("Solving..."):
            st.markdown(solve_math(llm, problem))

else:
    image = st.file_uploader("Upload textbook, handwritten, or screenshot question", type=["jpg", "jpeg", "png", "webp"])
    if image:
        st.image(image, caption="Uploaded question", width=500)
        if st.button("Read & Solve", type="primary"):
            with st.spinner("Reading image and solving..."):
                st.markdown(solve_image_question(llm, image.getvalue(), image.type))
