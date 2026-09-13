import streamlit as st
from datetime import datetime


def _html(s: str) -> str:
    """Flatten a triple-quoted HTML string to zero indentation per line,
    so Streamlit's markdown parser never mistakes it for a code block."""
    lines = [line.strip() for line in s.strip("\n").splitlines()]
    return "\n".join(lines)


# =========================================================
# INITIALIZE SOLVER
# =========================================================

def initialize_solver():

    if "solve_history" not in st.session_state:
        st.session_state.solve_history = []

    if "current_problem" not in st.session_state:
        st.session_state.current_problem = ""

    if "solution_visible" not in st.session_state:
        st.session_state.solution_visible = False

    if "hint_visible" not in st.session_state:
        st.session_state.hint_visible = False


# =========================================================
# DEMO SOLVER
# =========================================================

def generate_solution(problem, subject, difficulty):

    if not problem.strip():
        return None

    problem_lower = problem.lower()

    if "2 + 2" in problem_lower:
        return {
            "steps": [
                "Identify the two numbers: 2 and 2.",
                "Add the first number to the second number.",
                "2 + 2 = 4."
            ],
            "answer": "4",
            "explanation": "The sum of 2 and 2 is 4."
        }

    if "5 * 5" in problem_lower or "5 × 5" in problem_lower:
        return {
            "steps": [
                "Identify the two numbers: 5 and 5.",
                "Multiply the numbers together.",
                "5 × 5 = 25."
            ],
            "answer": "25",
            "explanation": "Multiplying 5 by 5 gives 25."
        }

    return {
        "steps": [
            f"First, identify the main concept involved in this {subject} problem.",
            "Break the problem into smaller parts.",
            "Apply the relevant concept or rule to each part.",
            "Check the result to make sure the reasoning is consistent."
        ],
        "answer": "A step-by-step solution can be generated here.",
        "explanation": (
            f"This is a {difficulty.lower()}-level {subject} problem. "
            "The actual AI-powered solution will be connected later."
        )
    }


def generate_hint(subject):

    hints = {
        "Mathematics":
            "Start by identifying the values given in the question and determine which formula or operation applies.",
        "Programming":
            "Break the problem into smaller logical steps before thinking about the complete code.",
        "Artificial Intelligence":
            "Identify the input, the learning/task objective, and the method that could be used to solve the problem.",
        "Computer Science":
            "First identify the main concept being tested, then connect it to the appropriate algorithm or principle.",
        "Database Systems":
            "Look for the entities, relationships, attributes, or query requirements mentioned in the problem.",
        "Computer Networks":
            "Identify which networking layer, protocol, or communication process the question is describing.",
        "Software Engineering":
            "Determine which development process, requirement, design principle, or testing concept is relevant."
    }

    return hints.get(
        subject,
        "Break the problem into smaller parts and identify the main concept first."
    )


# =========================================================
# CSS
# =========================================================

def solve_styles():

    st.markdown(
        """
        <style>

        .solve-header {
            background: linear-gradient(135deg, #0B1F3A 0%, #123B5D 100%);
            padding: 30px 34px;
            border-radius: 20px;
            margin-bottom: 22px;
            color: white;
            box-shadow: 0 8px 25px rgba(11, 31, 58, 0.14);
            position: relative;
            overflow: hidden;
        }

        .solve-header::after {
            content: "";
            position: absolute;
            width: 220px;
            height: 220px;
            background: rgba(98, 214, 200, 0.12);
            border-radius: 50%;
            right: -60px;
            top: -90px;
        }

        .solve-header-label {
            color: #62D6C8;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 1.6px;
            margin-bottom: 8px;
            position: relative;
            z-index: 2;
        }

        .solve-header h1 {
            margin: 0;
            color: white;
            font-size: 32px;
            font-weight: 800;
            position: relative;
            z-index: 2;
        }

        .solve-header p {
            margin: 8px 0 0 0;
            color: #C9DCE9;
            font-size: 14px;
            position: relative;
            z-index: 2;
        }

        /* Solver card is now a real st.container(border=True) —
           style the generic bordered wrapper only inside the main column
           via a keyed container, so it doesn't clash with other cards. */

        div[class*="st-key-solver_card"] {
            background: white;
            border: 1px solid #E5EAEE;
            border-radius: 20px;
            padding: 22px 25px 6px 25px;
            box-shadow: 0 6px 22px rgba(11, 31, 58, 0.06);
        }

        .solver-title {
            font-size: 18px;
            font-weight: 800;
            color: #0B1F3A;
            margin-bottom: 4px;
        }

        .solver-subtitle {
            color: #71808C;
            font-size: 13px;
            margin-bottom: 18px;
        }

        .problem-label {
            color: #20394D;
            font-size: 13px;
            font-weight: 700;
            margin: 4px 0 8px 0;
        }

        textarea {
            border-radius: 14px !important;
        }

        .solution-card {
            background: #F7FAFB;
            border: 1px solid #E1E9EC;
            border-radius: 17px;
            padding: 20px;
            margin-top: 18px;
        }

        .solution-heading {
            color: #0F766E;
            font-size: 15px;
            font-weight: 800;
            margin-bottom: 14px;
        }

        .step {
            display: flex;
            gap: 8px;
            background: white;
            border: 1px solid #E8EEF1;
            border-radius: 12px;
            padding: 12px 14px;
            margin-bottom: 9px;
            color: #334B5C;
            font-size: 13px;
            line-height: 1.5;
            transition: all 0.15s ease;
        }

        .step:hover {
            border-color: #BFE9E4;
            transform: translateX(2px);
        }

        .step-number {
            color: #0F766E;
            font-weight: 800;
            white-space: nowrap;
        }

        .answer-card {
            background: #EFF9F7;
            border: 1px solid #CDEBE5;
            border-radius: 16px;
            padding: 18px;
            margin-top: 4px;
        }

        .answer-label {
            color: #5B7275;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1px;
        }

        .answer-value {
            color: #0F766E;
            font-size: 22px;
            font-weight: 800;
            margin-top: 5px;
        }

        .answer-explanation {
            color: #50646C;
            font-size: 12px;
            margin-top: 7px;
        }

        .hint-card {
            background: #FFF9EA;
            border: 1px solid #F1E2B8;
            border-radius: 15px;
            padding: 16px;
            margin-top: 4px;
        }

        .hint-title {
            color: #946B16;
            font-weight: 800;
            font-size: 13px;
        }

        .hint-text {
            color: #725D2C;
            font-size: 12px;
            line-height: 1.5;
            margin-top: 5px;
        }

        .side-card {
            background: white;
            border: 1px solid #E5EAEE;
            border-radius: 18px;
            padding: 19px;
            margin-bottom: 15px;
            box-shadow: 0 5px 18px rgba(11, 31, 58, 0.05);
        }

        .side-title {
            color: #0B1F3A;
            font-size: 14px;
            font-weight: 800;
            margin-bottom: 13px;
        }

        .tip {
            display: flex;
            gap: 10px;
            margin-bottom: 13px;
        }

        .tip:last-child { margin-bottom: 0; }

        .tip-icon { font-size: 18px; }

        .tip-text {
            color: #63737E;
            font-size: 12px;
            line-height: 1.45;
        }

        .history-item {
            border-bottom: 1px solid #EDF0F2;
            padding: 10px 4px;
            border-radius: 8px;
            transition: background 0.15s ease;
        }

        .history-item:hover { background: #F7FAFB; }
        .history-item:last-child { border-bottom: none; }

        .history-problem {
            color: #324A5B;
            font-size: 12px;
            font-weight: 700;
        }

        .history-meta {
            color: #89969E;
            font-size: 10px;
            margin-top: 3px;
        }

        .stButton > button {
            border-radius: 12px !important;
            min-height: 42px !important;
            font-weight: 700 !important;
            border: 1px solid #DCE5E9 !important;
            background: white !important;
            color: #173047 !important;
            transition: all 0.2s ease !important;
        }

        .stButton > button:hover {
            border-color: #0F766E !important;
            color: #0F766E !important;
        }

        div[data-testid="stButton"] button[kind="primary"] {
            background: #0F766E !important;
            border-color: #0F766E !important;
            color: white !important;
        }

        div[data-testid="stButton"] button[kind="primary"]:hover {
            background: #0D625C !important;
            color: white !important;
        }

        div[data-baseweb="select"] > div {
            border-radius: 12px !important;
            border-color: #DCE5E9 !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# SOLVE PAGE
# =========================================================

def solve_page():

    initialize_solver()
    solve_styles()

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(_html("""
        <div class="solve-header">
            <div class="solve-header-label">✦ SMART PROBLEM SOLVING</div>
            <h1>Let's solve it. 🧩</h1>
            <p>Work through problems step by step and understand the reasoning behind every answer.</p>
        </div>
        """), unsafe_allow_html=True)

    main_col, side_col = st.columns([2.35, 1], gap="large")

    # =====================================================
    # MAIN SOLVER
    # =====================================================

    with main_col:

        with st.container(key="solver_card"):

            st.markdown('<div class="solver-title">🧠 Problem Solver</div>', unsafe_allow_html=True)
            st.markdown(
                '<div class="solver-subtitle">Enter a question or problem and EduBot will guide you through the solution.</div>',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:
                subject = st.selectbox(
                    "Subject",
                    [
                        "Mathematics", "Programming", "Artificial Intelligence",
                        "Computer Science", "Database Systems",
                        "Computer Networks", "Software Engineering"
                    ]
                )

            with col2:
                difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])

            st.markdown('<div class="problem-label">Your problem</div>', unsafe_allow_html=True)

            problem = st.text_area(
                "Problem",
                placeholder="Example: Explain how a binary search algorithm works and give a simple example...",
                height=150,
                label_visibility="collapsed"
            )

            solve_col, hint_col, clear_col = st.columns([2.2, 1, 1])

            with solve_col:
                solve_clicked = st.button("🧠 Solve Problem", type="primary", use_container_width=True)

            with hint_col:
                hint_clicked = st.button("💡 Hint", use_container_width=True)

            with clear_col:
                clear_clicked = st.button("Clear", use_container_width=True)

            # -------------------------------------------------
            # CLEAR
            # -------------------------------------------------
            if clear_clicked:
                st.session_state.current_problem = ""
                st.session_state.solution_visible = False
                st.session_state.hint_visible = False
                st.rerun()

            # -------------------------------------------------
            # HINT
            # -------------------------------------------------
            if hint_clicked:
                st.session_state.hint_visible = True

            if st.session_state.hint_visible:
                hint = generate_hint(subject)
                st.markdown(_html(f"""
                    <div class="hint-card">
                        <div class="hint-title">💡 Think about this...</div>
                        <div class="hint-text">{hint}</div>
                    </div>
                    """), unsafe_allow_html=True)

            # -------------------------------------------------
            # SOLVE
            # -------------------------------------------------
            if solve_clicked:
                if not problem.strip():
                    st.warning("Please enter a problem first.")
                else:
                    st.session_state.current_problem = problem
                    st.session_state.solution_visible = True
                    st.session_state.hint_visible = False

                    st.session_state.solve_history.insert(0, {
                        "problem": problem,
                        "subject": subject,
                        "time": datetime.now().strftime("%I:%M %p")
                    })

            # -------------------------------------------------
            # SOLUTION — built as ONE string (steps + answer together)
            # -------------------------------------------------
            if st.session_state.solution_visible:

                solution = generate_solution(
                    st.session_state.current_problem, subject, difficulty
                )

                if solution:
                    steps_html = "\n".join(
                        _html(f"""
                            <div class="step">
                                <span class="step-number">Step {index}:</span>
                                <span>{step}</span>
                            </div>
                            """)
                        for index, step in enumerate(solution["steps"], start=1)
                    )

                    solution_block = _html(f"""
                        <div class="solution-card">
                            <div class="solution-heading">✦ Step-by-step solution</div>
                            {steps_html}
                            <div class="answer-card">
                                <div class="answer-label">FINAL ANSWER</div>
                                <div class="answer-value">{solution["answer"]}</div>
                                <div class="answer-explanation">{solution["explanation"]}</div>
                            </div>
                        </div>
                        """)

                    st.markdown(solution_block, unsafe_allow_html=True)

    # =====================================================
    # SIDE PANEL
    # =====================================================

    with side_col:

        # Learning tips — one self-contained block
        st.markdown(_html("""
            <div class="side-card">
                <div class="side-title">💡 Smart solving tips</div>
                <div class="tip">
                    <div class="tip-icon">1️⃣</div>
                    <div class="tip-text">Read the complete problem before trying to solve it.</div>
                </div>
                <div class="tip">
                    <div class="tip-icon">2️⃣</div>
                    <div class="tip-text">Break complicated problems into smaller steps.</div>
                </div>
                <div class="tip">
                    <div class="tip-icon">3️⃣</div>
                    <div class="tip-text">Use hints before looking at the complete solution.</div>
                </div>
                <div class="tip">
                    <div class="tip-icon">4️⃣</div>
                    <div class="tip-text">Understand why an answer is correct, not just the final result.</div>
                </div>
            </div>
            """), unsafe_allow_html=True)

        # Recent problems — built as ONE string (header + items together)
        if st.session_state.solve_history:
            items_html = "\n".join(
                _html(f"""
                    <div class="history-item">
                        <div class="history-problem">
                            {(item["problem"][:70] + "...") if len(item["problem"]) > 70 else item["problem"]}
                        </div>
                        <div class="history-meta">{item["subject"]} • {item["time"]}</div>
                    </div>
                    """)
                for item in st.session_state.solve_history[:5]
            )
        else:
            items_html = _html("""
                <div class="history-meta">Your solved problems will appear here.</div>
                """)

        history_block = _html(f"""
            <div class="side-card">
                <div class="side-title">🕘 Recent problems</div>
                {items_html}
            </div>
            """)

        st.markdown(history_block, unsafe_allow_html=True)

        # Challenge card — one self-contained block
        st.markdown(_html("""
            <div class="side-card">
                <div class="side-title">🎯 Challenge yourself</div>
                <div class="tip-text">
                    Try solving a problem without using the hint first.
                    Then compare your reasoning with EduBot's solution.
                </div>
            </div>
            """), unsafe_allow_html=True)