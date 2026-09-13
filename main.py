import streamlit as st
from styles import apply_styles
from components import sidebar
from home import home_page
from study import study_page
from ai_tutor import ai_tutor_page
from solve import solve_page
from practice import practice_page
from progress import progress_page
from exam_prep import exam_prep_page

# Initialize page safely
if "page" not in st.session_state:
    st.session_state.page = "Home"

# -----------------------------
# Page settings
# -----------------------------

st.set_page_config(
    page_title="EduBot",
    page_icon="🎓",
    layout="wide"
)

apply_styles()
sidebar()

# -----------------------------

# -----------------------------
# Current page
# -----------------------------

page = st.session_state.page


# -----------------------------
# Main content
# -----------------------------

if page == "Home":

    home_page()


elif page == "Study":

    study_page()


elif page == "AI Tutor":
    ai_tutor_page()


elif page == "Solve":
    solve_page()


elif page == "Practice":
    practice_page()


elif page == "Progress":
    progress_page()


elif page == "Exam Prep":
    exam_prep_page()