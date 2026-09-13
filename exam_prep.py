import streamlit as st


# =========================================================
# EXAM PREP DATA
# =========================================================

SUBJECTS = [
    "Programming",
    "Artificial Intelligence",
    "Database Systems",
    "Computer Networks",
    "Software Engineering",
    "Information Technology",
]

TOPICS = [
    "Data Structures",
    "Algorithms",
    "Object-Oriented Programming",
    "Database Concepts",
    "Problem Solving",
]

WEAK_THRESHOLD = 72  # below this, a topic is flagged as a focus area

CHECKLIST_ITEMS = [
    ("review_concepts", "📖 Review important concepts"),
    ("review_weak_topics", "🎯 Revise weak topics"),
    ("practice_previous_questions", "🧩 Practice previous questions"),
    ("review_mistakes", "🔄 Review mistakes"),
    ("complete_mock_exam", "📝 Complete a mock exam"),
    ("final_revision", "✅ Final revision"),
]


def initialize_exam_data():
    defaults = {
        "exam_subject": "Programming",
        "exam_topic": "Data Structures",
        "revision_topics": {
            "Data Structures": 78,
            "Algorithms": 65,
            "Object-Oriented Programming": 82,
            "Database Concepts": 58,
            "Problem Solving": 70,
        },
        "mock_exam_started": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def compute_readiness():
    """Overall readiness = average of all topic scores."""
    scores = st.session_state.revision_topics.values()
    return round(sum(scores) / len(scores)) if scores else 0


# =========================================================
# CSS  (loaded once, no HTML left half-open anywhere else)
# =========================================================

def exam_prep_styles():
    st.markdown(
        """
        <style>
        .exam-header {
            background: linear-gradient(135deg, #0B1F3A 0%, #123B5D 100%);
            padding: 30px 34px;
            border-radius: 20px;
            margin-bottom: 22px;
            color: white;
            box-shadow: 0 8px 25px rgba(11, 31, 58, 0.12);
        }
        .exam-label {
            color: #62D6C8;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 1.5px;
            margin-bottom: 8px;
        }
        .exam-header h1 { color: white; margin: 0; font-size: 32px; font-weight: 750; }
        .exam-header p { color: #D9E7F1; margin: 9px 0 0 0; font-size: 15px; }

        .exam-card {
            background: white;
            border: 1px solid #E5EAEE;
            border-radius: 18px;
            padding: 20px 22px;
            margin-bottom: 18px;
            box-shadow: 0 5px 18px rgba(11, 31, 58, 0.05);
        }
        .card-title { color: #0B1F3A; font-size: 16px; font-weight: 750; margin-bottom: 2px; }
        .card-subtitle { color: #81909A; font-size: 12px; margin-bottom: 4px; }

        .readiness-card {
            background: linear-gradient(135deg, #EFF9F7, #F8FCFB);
            border: 1px solid #D7ECE8;
            border-radius: 18px;
            padding: 20px 22px;
            text-align: center;
        }
        .readiness-label { color: #39756F; font-size: 12px; font-weight: 700; letter-spacing: .6px; }
        .readiness-number { color: #0B5F59; font-size: 40px; font-weight: 800; margin: 2px 0; }

        .topic-row { margin-bottom: 16px; }
        .topic-header { display: flex; justify-content: space-between; margin-bottom: 6px; }
        .topic-name { color: #344D5D; font-size: 12px; font-weight: 650; }
        .topic-score { font-size: 12px; font-weight: 750; }
        .topic-track { height: 9px; background: #E9EFF1; border-radius: 20px; overflow: hidden; }
        .topic-fill { height: 9px; border-radius: 20px; transition: width 0.4s ease; }

        .weak-topic {
            display: flex; align-items: center; gap: 12px;
            padding: 10px 12px;
            background: #FFF9ED;
            border: 1px solid #F1E4C4;
            border-radius: 12px;
            margin-bottom: 8px;
        }
        .weak-icon { font-size: 18px; }
        .weak-title { color: #665021; font-size: 12px; font-weight: 700; }
        .weak-score { color: #987A37; font-size: 10px; margin-top: 2px; }
        .all-good {
            padding: 10px 12px; background: #EEF9F2; border: 1px solid #C9EBD4;
            border-radius: 12px; color: #226B45; font-size: 12px; font-weight: 650;
        }

        .mock-card {
            background: linear-gradient(135deg, #FFF7E8, #FFFBF4);
            border: 1px solid #F0E0B9;
            border-radius: 18px;
            padding: 22px;
            margin-bottom: 6px;
        }
        .mock-title { color: #765B20; font-size: 18px; font-weight: 800; margin: 0; }
        .mock-text { color: #806F4E; font-size: 12px; line-height: 1.6; margin-top: 6px; }

        .tip { display: flex; gap: 11px; padding: 10px 0; border-bottom: 1px solid #EDF0F2; }
        .tip:last-child { border-bottom: none; }
        .tip-icon { font-size: 16px; }
        .tip-text { color: #536774; font-size: 12px; line-height: 1.5; }

        .plan-item { padding: 9px 0; color: #536774; font-size: 12px; border-bottom: 1px solid #EDF0F2; }
        .plan-item:last-child { border-bottom: none; }

        .stButton > button {
            border-radius: 12px !important;
            min-height: 42px !important;
            border: 1px solid #DCE5E9 !important;
            background: white !important;
            color: #173047 !important;
            font-weight: 650 !important;
            transition: all 0.2s ease !important;
        }
        .stButton > button:hover { border-color: #0F766E !important; color: #0F766E !important; }

        /* ==========================================
           CHECKBOXES — single box: white fill, blue stroke
        ========================================== */
        div[data-testid="stCheckbox"] label > span:first-child {
            background-color: white !important;
            border: 2px solid #2563EB !important;
            border-radius: 4px !important;
            box-shadow: none !important;
        }
        div[data-testid="stCheckbox"] label > span:first-child svg {
            fill: #2563EB !important;
        }
        div[data-testid="stCheckbox"] label p {
            color: #344D5D !important;
            font-size: 13px !important;
        }

        /* ==========================================
           TABS — legible text in every state
           (targets ARIA role, which is stable across
           Streamlit versions, plus data-baseweb as backup;
           also forces opacity in case dimming, not just
           color, was making inactive tabs hard to read)
        ========================================== */
        button[role="tab"],
        button[role="tab"] *,
        button[data-baseweb="tab"],
        button[data-baseweb="tab"] * {
            color: #536774 !important;
            -webkit-text-fill-color: #536774 !important;
            opacity: 1 !important;
            font-weight: 600 !important;
        }
        button[role="tab"][aria-selected="true"],
        button[role="tab"][aria-selected="true"] *,
        button[data-baseweb="tab"][aria-selected="true"],
        button[data-baseweb="tab"][aria-selected="true"] * {
            color: #0F766E !important;
            -webkit-text-fill-color: #0F766E !important;
            opacity: 1 !important;
        }
        [data-baseweb="tab-highlight"],
        [data-baseweb="tab-list"] div[style*="background-color"] {
            background-color: #0F766E !important;
        }
        div[data-baseweb="tab-border"] {
            background-color: #E5EAEE !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# SMALL RENDER HELPERS (each returns/renders one complete,
# self-contained HTML block — never split across calls)
# =========================================================

def render_header():
    st.markdown(
        """
        <div class="exam-header">
            <div class="exam-label">✦ EXAM PREPARATION</div>
            <h1>Prepare with confidence. 📝</h1>
            <p>Review important topics, identify weak areas, and get ready for your next exam.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_readiness_card(readiness: int):
    st.markdown(
        f"""
        <div class="readiness-card">
            <div class="readiness-label">EXAM READINESS</div>
            <div class="readiness-number">{readiness}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(readiness / 100)
    if readiness >= 80:
        st.success("You're almost exam ready!")
    elif readiness >= 60:
        st.info("Good progress — keep revising.")
    else:
        st.warning("More revision is recommended.")


def render_topic_chart(topics: dict):
    """Native Streamlit/HTML bars — no extra dependency required."""
    for name, score in topics.items():
        color = "#0F766E" if score >= WEAK_THRESHOLD else "#D97706"
        st.markdown(
            f"""
            <div class="topic-row">
                <div class="topic-header">
                    <div class="topic-name">{name}</div>
                    <div class="topic-score" style="color:{color};">{score}%</div>
                </div>
                <div class="topic-track">
                    <div class="topic-fill" style="width:{score}%; background:{color};"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_weak_topics(topics: dict):
    weak = {k: v for k, v in topics.items() if v < WEAK_THRESHOLD}
    icons = ["📊", "🧠", "💡", "🗂️", "🔍"]

    if not weak:
        st.markdown(
            '<div class="all-good">🎉 No major weak spots right now — nice work!</div>',
            unsafe_allow_html=True,
        )
        return

    for i, (name, score) in enumerate(sorted(weak.items(), key=lambda x: x[1])):
        icon = icons[i % len(icons)]
        st.markdown(
            f"""
            <div class="weak-topic">
                <div class="weak-icon">{icon}</div>
                <div>
                    <div class="weak-title">{name}</div>
                    <div class="weak-score">Current understanding: {score}%</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# EXAM PREP PAGE
# =========================================================

def exam_prep_page():
    initialize_exam_data()
    exam_prep_styles()
    render_header()

    # -----------------------------------------------------
    # Subject / topic selection + readiness, side by side
    # -----------------------------------------------------
    selection_col, readiness_col = st.columns([1.3, 1], gap="large")

    with selection_col:
        st.markdown(
            """
            <div class="exam-card">
                <div class="card-title">📚 Build Your Exam Plan</div>
                <div class="card-subtitle">Select what you want to prepare</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        subject = st.selectbox("Subject", SUBJECTS, key="exam_subject_select")
        topic = st.selectbox("Focus area", TOPICS, key="exam_topic_select")
        st.session_state.exam_subject = subject
        st.session_state.exam_topic = topic

    with readiness_col:
        render_readiness_card(compute_readiness())

    st.divider()

    # -----------------------------------------------------
    # Tabs keep things interactive and organized
    # -----------------------------------------------------
    tab_progress, tab_mock, tab_tips = st.tabs(
        ["📊 Progress", "📝 Mock Exam", "💡 Tips & Plan"]
    )

    # ---------------- PROGRESS TAB ----------------
    with tab_progress:
        chart_col, weak_col = st.columns([1.5, 1], gap="large")

        with chart_col:
            st.markdown(
                """
                <div class="exam-card">
                    <div class="card-title">Topic Readiness</div>
                    <div class="card-subtitle">See which areas are strong and which need revision</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            render_topic_chart(st.session_state.revision_topics)

        with weak_col:
            st.markdown(
                """
                <div class="exam-card">
                    <div class="card-title">⚠️ Focus Areas</div>
                    <div class="card-subtitle">Topics that deserve extra attention</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            render_weak_topics(st.session_state.revision_topics)

        st.markdown(
            """
            <div class="exam-card">
                <div class="card-title">✅ Revision Checklist</div>
                <div class="card-subtitle">Organize your preparation before the exam</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        checklist_col1, checklist_col2 = st.columns(2)
        checked = []
        for i, (key, label) in enumerate(CHECKLIST_ITEMS):
            col = checklist_col1 if i % 2 == 0 else checklist_col2
            with col:
                checked.append(st.checkbox(label, key=key))

        completed = sum(checked)
        st.progress(completed / len(CHECKLIST_ITEMS))
        st.caption(f"{completed}/{len(CHECKLIST_ITEMS)} preparation tasks completed")
        if completed == len(CHECKLIST_ITEMS):
            st.balloons()
            st.success("All prep tasks done — you're ready to go!")

    # ---------------- MOCK EXAM TAB ----------------
    with tab_mock:
        st.markdown(
            """
            <div class="mock-card">
                <div class="mock-title">📝 Ready for a Mock Exam?</div>
                <div class="mock-text">
                    Test yourself under exam-like conditions. A mock exam can help
                    identify knowledge gaps before the real assessment.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        mock_col1, mock_col2, mock_col3 = st.columns(3)
        with mock_col1:
            st.selectbox("Difficulty", ["Easy", "Medium", "Hard"], key="mock_difficulty")
        with mock_col2:
            st.selectbox("Questions", [10, 20, 30, 50], key="mock_questions")
        with mock_col3:
            st.selectbox(
                "Time",
                ["15 minutes", "30 minutes", "45 minutes", "60 minutes"],
                key="mock_time",
            )

        if st.button("🚀 Start Mock Exam", use_container_width=True):
            st.session_state.mock_exam_started = True

        if st.session_state.mock_exam_started:
            st.success(
                f"Mock exam ready: {st.session_state.mock_questions} questions, "
                f"{st.session_state.mock_difficulty} difficulty, "
                f"{st.session_state.mock_time}. The exam engine can be connected next."
            )

    # ---------------- TIPS & PLAN TAB ----------------
    with tab_tips:
        tips_col, plan_col = st.columns([1.4, 1], gap="large")

        with tips_col:
            tips = [
                ("🎯", "Focus more time on topics where your readiness score is low."),
                ("🧠", "Try explaining difficult concepts in your own words."),
                ("⏱️", "Use timed practice to become comfortable working under exam pressure."),
                ("🔄", "Review mistakes instead of only repeating questions you already know."),
            ]
            tips_html = "".join(
                f'<div class="tip"><div class="tip-icon">{icon}</div>'
                f'<div class="tip-text">{text}</div></div>'
                for icon, text in tips
            )
            st.markdown(
                f"""
                <div class="exam-card">
                    <div class="card-title">💡 Exam Preparation Tips</div>
                    <div class="card-subtitle">Simple habits for better preparation</div>
                    {tips_html}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with plan_col:
            steps = [
                "📖 1. Review concepts",
                "🎯 2. Practice weak areas",
                "🧩 3. Solve questions",
                "📝 4. Take mock exam",
                "🔄 5. Review mistakes",
            ]
            plan_html = "".join(f'<div class="plan-item">{s}</div>' for s in steps)
            st.markdown(
                f"""
                <div class="exam-card">
                    <div class="card-title">🗓️ Quick Study Plan</div>
                    <div class="card-subtitle">Suggested preparation sequence</div>
                    {plan_html}
                </div>
                """,
                unsafe_allow_html=True,
            )


if __name__ == "__main__":
    st.set_page_config(page_title="EduBot — Exam Prep", layout="wide")
    exam_prep_page()