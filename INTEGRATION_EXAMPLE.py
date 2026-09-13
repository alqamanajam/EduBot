"""
Minimal Streamlit integration example for Person 2.

This is only an integration reference. Samrah/Alqama can merge the functions
into the final EduBot UI rather than using this file as the complete app.
"""

import streamlit as st

from ai_tutor import (
    create_llm,
    tutor_answer,
    solve_math,
    solve_image_question,
    start_teach_me,
    evaluate_teach_me,
)

st.title("EduBot - AI Tutor, Math & Image Solver")

llm = create_llm()

mode = st.selectbox(
    "Choose module",
    ["AI Tutor", "Math Solver", "Image/Textbook Solver", "Teach Me Mode"]
)

if mode == "AI Tutor":
    level = st.selectbox("Learning level", ["Beginner", "Intermediate", "Advanced"])
    topic = st.text_input("Topic", "Python")
    question = st.text_area("Your question")

    if st.button("Ask EduBot") and question.strip():
        with st.spinner("Thinking..."):
            answer = tutor_answer(llm, question, level, topic)
        st.markdown(answer)

elif mode == "Math Solver":
    problem = st.text_area("Mathematical problem")

    if st.button("Solve") and problem.strip():
        with st.spinner("Solving step by step..."):
            answer = solve_math(llm, problem)
        st.markdown(answer)

elif mode == "Image/Textbook Solver":
    image = st.file_uploader(
        "Upload a question image",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if image and st.button("Solve Image"):
        with st.spinner("Reading and solving image..."):
            answer = solve_image_question(
                llm,
                image.getvalue(),
                image.type
            )
        st.markdown(answer)

else:
    level = st.selectbox("Learning level", ["Beginner", "Intermediate", "Advanced"])
    topic = st.text_input("Teach me topic", "Photosynthesis")

    if "teach_started" not in st.session_state:
        st.session_state.teach_started = False

    if st.button("Start Lesson"):
        response = start_teach_me(llm, topic, level)
        st.session_state.teach_started = True
        st.session_state.previous_teaching = response
        st.session_state.checking_question = ""
        st.markdown(response)

    if st.session_state.get("teach_started"):
        student_response = st.text_area("Your answer to EduBot's question")

        if st.button("Submit Answer") and student_response.strip():
            response = evaluate_teach_me(
                llm,
                topic=topic,
                checking_question=st.session_state.get("checking_question", ""),
                student_response=student_response,
                previous_teaching=st.session_state.get("previous_teaching", ""),
                level=level,
            )
            st.session_state.previous_teaching = response
            st.markdown(response)
