import streamlit as st
from datetime import date


# =============================================================
# STATE
# =============================================================

def _init_state():
    """Set up the bits of session state the dashboard depends on.
    Call once per session; safe to call every rerun."""

    if "goals" not in st.session_state:
        st.session_state.goals = {
            "study_30": {"label": "Study for 30 minutes", "done": True},
            "solve_10": {"label": "Solve 10 questions", "done": True},
            "review_topic": {"label": "Review one topic", "done": False},
            "tutor_practice": {"label": "Practice with AI Tutor", "done": False},
        }

    if "streak" not in st.session_state:
        st.session_state.streak = 7

    if "last_streak_day" not in st.session_state:
        st.session_state.last_streak_day = None

    if "questions_solved" not in st.session_state:
        st.session_state.questions_solved = 48

    if "activity_log" not in st.session_state:
        st.session_state.activity_log = [
            {"icon": "📚", "title": "Data Structures", "detail": "Studied for 35 minutes", "when": "Today"},
            {"icon": "🧩", "title": "Practice Questions", "detail": "Solved 10 questions", "when": "Yesterday"},
            {"icon": "💬", "title": "AI Tutor Session", "detail": "Asked 5 questions", "when": "Yesterday"},
        ]


def _log_activity(icon: str, title: str, detail: str):
    st.session_state.activity_log.insert(0, {"icon": icon, "title": title, "detail": detail, "when": "Just now"})
    st.session_state.activity_log = st.session_state.activity_log[:6]


def _goals_progress() -> float:
    goals = st.session_state.goals.values()
    if not goals:
        return 0.0
    return sum(1 for g in goals if g["done"]) / len(goals)


def _go_to(page: str, toast: str | None = None):
    st.session_state.page = page
    if toast:
        st.toast(toast, icon="✨")
    st.rerun()


# =============================================================
# HOME PAGE
# =============================================================

def home_page():

    _init_state()

    today_progress = _goals_progress()

    # ---------------------------------------------------------
    # HEADER
    # ---------------------------------------------------------

    st.markdown(
        """
        <div class="home-header">
            <div class="eyebrow">Learning dashboard</div>
            <h1>Welcome back <span class="wave">👋</span></h1>
            <p>Ready to make today a productive learning day?</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------------------------------------------------------
    # HERO
    # ---------------------------------------------------------

    # The entire card — text side AND visual side — has to be built as ONE
    # HTML string in a single st.markdown call. Streamlit doesn't let you open
    # a <div> in one call, drop st.columns/st.button in between, and close it
    # in a later call; each call is its own sibling block, not a nested child.
    st.markdown(
        f"""
        <div class="hero-card">
            <div class="hero-content">
                <div class="hero-kicker"><span class="spark">✦</span>YOUR AI LEARNING COMPANION</div>
                <h2>Learn smarter.<br><span>Understand better.</span></h2>
                <p>Study, solve problems, practice concepts, and prepare for exams
                with your personalized AI learning assistant.</p>
                <div class="hero-mini-stats">
                    <div><strong>{int(today_progress * 100)}%</strong><span>Today's goals</span></div>
                    <div><strong>{st.session_state.streak} days</strong><span>Current streak</span></div>
                    <div><strong>{st.session_state.questions_solved}</strong><span>Questions solved</span></div>
                </div>
            </div>
            <div class="hero-visual">
                <div class="orbit orbit-one"></div>
                <div class="orbit orbit-two"></div>
                <div class="visual-glow"></div>
                <div class="robot-orb">
                    <div class="robot-antenna"></div>
                    <div class="robot-face"><span></span><span></span><i></i></div>
                </div>
                <div class="floating-card floating-top"><span>✓</span>Session saved</div>
                <div class="floating-card floating-bottom"><span>🔥</span>7-day streak</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Real Streamlit button goes below the card, not inside it — it's a
    # separate DOM element regardless of where the Python call sits.
    btn_col, _ = st.columns([1, 3])
    with btn_col:
        if st.button("Start learning", key="hero_start_learning", type="primary", use_container_width=True):
            _go_to("Study", "Heading to Study")

    # ---------------------------------------------------------
    # QUICK ACCESS (with a working filter)
    # ---------------------------------------------------------

    st.markdown(
        """
        <div class="section-heading">
            <h3>Quick Access</h3>
            <p>Jump straight into your learning tools.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tools = [
        {"key": "AI Tutor", "icon": "💬", "color": "teal", "title": "AI Tutor", "desc": "Ask questions and learn interactively."},
        {"key": "Solve", "icon": "🧩", "color": "blue", "title": "Solve", "desc": "Get help solving difficult problems."},
        {"key": "Practice", "icon": "✦", "color": "yellow", "title": "Practice", "desc": "Test your knowledge with practice questions."},
        {"key": "Study", "icon": "📚", "color": "purple", "title": "Study", "desc": "Review subjects and learning materials."},
    ]

    search = st.text_input(
        "Search tools", placeholder="Search your tools\u2026", label_visibility="collapsed"
    )
    visible_tools = [t for t in tools if search.lower() in t["title"].lower()] if search else tools

    if not visible_tools:
        st.caption(f"No tools match \u201c{search}\u201d.")
    else:
        cols = st.columns(len(visible_tools), gap="medium")
        for col, tool in zip(cols, visible_tools):
            with col:
                with st.container(border=True):
                    st.markdown(f'<div class="tool-icon {tool["color"]}">{tool["icon"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="tool-title">{tool["title"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="tool-description">{tool["desc"]}</div>', unsafe_allow_html=True)
                    if st.button("Open", key=f"home_{tool['key']}", use_container_width=True):
                        _go_to(tool["key"], f"Opening {tool['title']}")

    # ---------------------------------------------------------
    # PROGRESS
    # ---------------------------------------------------------

    st.markdown(
        """
        <div class="section-heading progress-heading">
            <h3>Your Progress</h3>
            <p>Keep track of your learning journey.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    progress1, progress2, progress3 = st.columns(3, gap="medium")

    with progress1:
        with st.container(border=True):
            st.markdown('<div class="stat-icon teal">📈</div>', unsafe_allow_html=True)
            st.metric("Today's Goals", f"{int(today_progress * 100)}%")
            st.progress(today_progress)

    with progress2:
        with st.container(border=True):
            st.markdown('<div class="stat-icon orange">🔥</div>', unsafe_allow_html=True)
            st.metric("Study Streak", f"{st.session_state.streak} Days")
            already_logged_today = st.session_state.last_streak_day == date.today().isoformat()
            if st.button(
                "Logged for today" if already_logged_today else "Mark today done",
                key="log_streak",
                disabled=already_logged_today,
                use_container_width=True,
            ):
                st.session_state.streak += 1
                st.session_state.last_streak_day = date.today().isoformat()
                _log_activity("🔥", "Streak extended", f"{st.session_state.streak}-day streak")
                st.toast("Nice — streak extended!", icon="🔥")
                st.rerun()

    with progress3:
        with st.container(border=True):
            st.markdown('<div class="stat-icon blue">✓</div>', unsafe_allow_html=True)
            st.metric("Questions Solved", st.session_state.questions_solved)
            st.caption("This month")

    # ---------------------------------------------------------
    # LOWER DASHBOARD
    # ---------------------------------------------------------

    activity_col, goals_col = st.columns([1.5, 1], gap="medium")

    with activity_col:
        st.markdown(
            """
            <div class="section-heading lower-heading">
                <h3>Recent Activity</h3>
                <p>Your latest learning sessions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            for i, entry in enumerate(st.session_state.activity_log):
                st.markdown(
                    f"""
                    <div class="activity-row">
                        <div class="activity-icon">{entry['icon']}</div>
                        <div class="activity-info">
                            <strong>{entry['title']}</strong>
                            <span>{entry['detail']}</span>
                        </div>
                        <div class="activity-time">{entry['when']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if i < len(st.session_state.activity_log) - 1:
                    st.markdown('<div class="activity-divider"></div>', unsafe_allow_html=True)

    with goals_col:
        st.markdown(
            """
            <div class="section-heading lower-heading">
                <h3>Today's Goals</h3>
                <p>Small steps, consistent progress.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            for key, goal in st.session_state.goals.items():
                checked = st.checkbox(goal["label"], value=goal["done"], key=f"goal_{key}")
                if checked != goal["done"]:
                    st.session_state.goals[key]["done"] = checked
                    if checked:
                        _log_activity("✅", goal["label"], "Marked complete")
                        st.toast(f"Nice — {goal['label'].lower()} done!", icon="✅")
                    st.rerun()

    # ---------------------------------------------------------
    # RECOMMENDATION (reacts to actual progress)
    # ---------------------------------------------------------

    st.markdown('<div class="recommendation-space"></div>', unsafe_allow_html=True)

    with st.container(border=True):
        rec_col1, rec_col2 = st.columns([4, 1], vertical_alignment="center")

        if today_progress == 1.0:
            rec_icon, rec_title, rec_text, rec_button, rec_target = (
                "🎉", "All goals done for today",
                "You cleared every goal. Keep the streak alive tomorrow, or get ahead with a bonus practice set.",
                "Bonus practice", "Practice",
            )
        elif today_progress >= 0.5:
            rec_icon, rec_title, rec_text, rec_button, rec_target = (
                "💡", "Almost there",
                "You're over halfway through today's goals. Finish strong with a quick practice round.",
                "Continue", "Practice",
            )
        else:
            rec_icon, rec_title, rec_text, rec_button, rec_target = (
                "💡", "Recommended for You",
                "Continue practicing Data Structures to strengthen your understanding and improve your problem-solving skills.",
                "Continue", "Practice",
            )

        with rec_col1:
            st.markdown(f"### {rec_icon} {rec_title}")
            st.caption(rec_text)

        with rec_col2:
            if st.button(rec_button, key="recommendation_continue", type="primary", use_container_width=True):
                _go_to(rec_target, f"Opening {rec_target}")