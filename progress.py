import streamlit as st


def _html(s: str) -> str:
    """Flatten a triple-quoted HTML string to zero indentation per line,
    so Streamlit's markdown parser never mistakes it for a code block."""
    lines = [line.strip() for line in s.strip("\n").splitlines()]
    return "\n".join(lines)


# =========================================================
# PROGRESS DATA
# =========================================================

def initialize_progress_data():

    if "overall_progress" not in st.session_state:
        st.session_state.overall_progress = 72

    if "questions_solved" not in st.session_state:
        st.session_state.questions_solved = 48

    if "learning_accuracy" not in st.session_state:
        st.session_state.learning_accuracy = 84

    if "study_streak" not in st.session_state:
        st.session_state.study_streak = 7

    if "weekly_activity" not in st.session_state:
        st.session_state.weekly_activity = [35, 52, 42, 68, 58, 76, 64]

    if "subject_progress" not in st.session_state:
        st.session_state.subject_progress = {
            "Programming": 80,
            "Artificial Intelligence": 65,
            "Database Systems": 58,
            "Computer Networks": 48,
            "Software Engineering": 72
        }


# =========================================================
# CSS
# =========================================================

def progress_styles():

    st.markdown(
        """
        <style>

        .progress-header {
            background: linear-gradient(135deg, #0B1F3A 0%, #123B5D 100%);
            padding: 30px 34px;
            border-radius: 20px;
            margin-bottom: 22px;
            color: white;
            box-shadow: 0 8px 25px rgba(11, 31, 58, 0.14);
            position: relative;
            overflow: hidden;
        }

        .progress-header::after {
            content: "";
            position: absolute;
            width: 220px;
            height: 220px;
            background: rgba(98, 214, 200, 0.12);
            border-radius: 50%;
            right: -60px;
            top: -90px;
        }

        .progress-label {
            color: #62D6C8;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 1.6px;
            margin-bottom: 8px;
            position: relative;
            z-index: 2;
        }

        .progress-header h1 {
            color: white;
            margin: 0;
            font-size: 32px;
            font-weight: 800;
            position: relative;
            z-index: 2;
        }

        .progress-header p {
            color: #C9DCE9;
            margin: 8px 0 0 0;
            font-size: 14px;
            position: relative;
            z-index: 2;
        }

        .stat-card {
            background: white;
            border: 1px solid #E5EAEE;
            border-radius: 18px;
            padding: 20px;
            min-height: 112px;
            box-shadow: 0 5px 18px rgba(11, 31, 58, 0.05);
            transition: all 0.18s ease;
        }

        .stat-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 9px 22px rgba(11, 31, 58, 0.09);
        }

        .stat-icon { font-size: 22px; margin-bottom: 6px; }

        .stat-label {
            color: #71808C;
            font-size: 10.5px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.7px;
        }

        .stat-value {
            color: #0B1F3A;
            font-size: 24px;
            font-weight: 800;
            margin-top: 4px;
        }

        .stat-small { color: #0F766E; font-size: 11px; margin-top: 3px; }

        .dashboard-card {
            background: white;
            border: 1px solid #E5EAEE;
            border-radius: 19px;
            padding: 22px;
            margin-top: 20px;
            box-shadow: 0 5px 18px rgba(11, 31, 58, 0.05);
        }

        .card-title {
            color: #0B1F3A;
            font-size: 16.5px;
            font-weight: 800;
            margin-bottom: 4px;
        }

        .card-subtitle {
            color: #81909A;
            font-size: 12px;
            margin-bottom: 16px;
        }

        .activity-chart {
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            height: 190px;
            padding: 10px 8px 0 8px;
            border-bottom: 1px solid #E8EDF0;
        }

        .activity-column {
            display: flex;
            flex-direction: column;
            align-items: center;
            height: 100%;
            justify-content: flex-end;
            flex: 1;
        }

        .activity-bar-wrapper {
            height: 145px;
            display: flex;
            align-items: flex-end;
            flex-direction: column;
            justify-content: flex-end;
        }

        .activity-bar {
            width: 25px;
            background: #0F766E;
            border-radius: 7px 7px 2px 2px;
            transition: all 0.2s ease;
        }

        .activity-bar:hover {
            background: #0B5F59;
            transform: translateY(-3px);
        }

        .activity-value { color: #71808C; font-size: 9px; margin-bottom: 5px; }
        .activity-day { color: #788792; font-size: 10px; margin-top: 9px; }

        .subject-row { margin-bottom: 16px; }
        .subject-row:last-child { margin-bottom: 0; }

        .subject-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 7px;
        }

        .subject-name { color: #31495A; font-size: 12px; font-weight: 650; }
        .subject-percent { color: #0F766E; font-size: 12px; font-weight: 750; }

        .subject-track {
            height: 8px;
            background: #E9EFF1;
            border-radius: 20px;
            overflow: hidden;
        }

        .subject-fill {
            height: 8px;
            background: #0F766E;
            border-radius: 20px;
            transition: width 0.3s ease;
        }

        .goal {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 0;
            border-bottom: 1px solid #EDF0F2;
        }

        .goal:last-child { border-bottom: none; padding-bottom: 0; }
        .goal-icon { font-size: 18px; }
        .goal-content { flex: 1; }
        .goal-title { color: #344D5D; font-size: 12px; font-weight: 650; }
        .goal-description { color: #89969E; font-size: 10px; margin-top: 3px; }
        .goal-status { font-size: 12px; font-weight: 750; }
        .goal-done { color: #19734C; }
        .goal-pending { color: #8A6A1D; }

        .achievement {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            background: #F8FAFB;
            border: 1px solid #E9EEF1;
            border-radius: 13px;
            margin-bottom: 9px;
            transition: all 0.15s ease;
        }

        .achievement:last-child { margin-bottom: 0; }
        .achievement:hover { border-color: #BFE9E4; transform: translateY(-1px); }
        .achievement-icon { font-size: 22px; }
        .achievement-title { color: #334B5C; font-size: 12px; font-weight: 700; }
        .achievement-description { color: #89969E; font-size: 10px; margin-top: 2px; }

        .activity-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 0;
            border-bottom: 1px solid #EDF0F2;
        }

        .activity-item:last-child { border-bottom: none; padding-bottom: 0; }

        .activity-icon {
            width: 34px;
            height: 34px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #EFF8F7;
            border-radius: 10px;
            font-size: 16px;
        }

        .activity-content { flex: 1; }
        .activity-title { color: #354D5D; font-size: 12px; font-weight: 650; }
        .activity-time { color: #919DA4; font-size: 10px; margin-top: 3px; }

        .streak-card {
            background: linear-gradient(135deg, #FFF8E9, #FFFBF3);
            border: 1px solid #F1E2BA;
            border-radius: 18px;
            padding: 20px;
            margin-top: 20px;
        }

        .streak-icon { font-size: 27px; }
        .streak-title { color: #765B20; font-size: 14px; font-weight: 750; margin-top: 5px; }
        .streak-number { color: #9A7018; font-size: 27px; font-weight: 800; }
        .streak-text { color: #897650; font-size: 11px; margin-top: 2px; }

        .stButton > button {
            border-radius: 12px !important;
            min-height: 42px !important;
            border: 1px solid #DCE5E9 !important;
            background: white !important;
            color: #173047 !important;
            font-weight: 650 !important;
            transition: all 0.2s ease !important;
        }

        .stButton > button:hover {
            border-color: #0F766E !important;
            color: #0F766E !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# STAT CARD
# =========================================================

def stat_card(icon, label, value, description):

    st.markdown(_html(f"""
        <div class="stat-card">
            <div class="stat-icon">{icon}</div>
            <div class="stat-label">{label}</div>
            <div class="stat-value">{value}</div>
            <div class="stat-small">{description}</div>
        </div>
        """), unsafe_allow_html=True)


# =========================================================
# PROGRESS PAGE
# =========================================================

def progress_page():

    initialize_progress_data()
    progress_styles()

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(_html("""
        <div class="progress-header">
            <div class="progress-label">✦ YOUR LEARNING JOURNEY</div>
            <h1>Track your progress. 📈</h1>
            <p>See how far you've come, celebrate your achievements, and keep moving forward.</p>
        </div>
        """), unsafe_allow_html=True)

    # =====================================================
    # TOP STATISTICS
    # =====================================================

    col1, col2, col3, col4 = st.columns(4, gap="medium")

    with col1:
        stat_card("📚", "Overall Progress", f'{st.session_state.overall_progress}%', "Keep learning")
    with col2:
        stat_card("🎯", "Questions Solved", st.session_state.questions_solved, "Practice completed")
    with col3:
        stat_card("✅", "Accuracy", f'{st.session_state.learning_accuracy}%', "Strong performance")
    with col4:
        stat_card("🔥", "Study Streak", f'{st.session_state.study_streak} days', "Keep it going")

    # =====================================================
    # MAIN ROW — WEEKLY ACTIVITY + GOALS
    # =====================================================

    left_col, right_col = st.columns([1.7, 1], gap="large")

    with left_col:

        values = st.session_state.weekly_activity
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        bar_columns = "\n".join(
            _html(f"""
                <div class="activity-column">
                    <div class="activity-bar-wrapper">
                        <div class="activity-value">{value}%</div>
                        <div class="activity-bar" style="height: {value * 1.35}px;"></div>
                    </div>
                    <div class="activity-day">{day}</div>
                </div>
                """)
            for day, value in zip(days, values)
        )

        weekly_card = _html(f"""
            <div class="dashboard-card">
                <div class="card-title">📈 Weekly Activity</div>
                <div class="card-subtitle">Your learning activity over the last 7 days</div>
                <div class="activity-chart">
                    {bar_columns}
                </div>
            </div>
            """)

        st.markdown(weekly_card, unsafe_allow_html=True)

    with right_col:

        st.markdown(_html("""
            <div class="dashboard-card">
                <div class="card-title">🎯 Today's Goals</div>
                <div class="card-subtitle">Small steps lead to big progress</div>
                <div class="goal">
                    <div class="goal-icon">✅</div>
                    <div class="goal-content">
                        <div class="goal-title">Complete a study session</div>
                        <div class="goal-description">30 minutes of focused learning</div>
                    </div>
                    <div class="goal-status goal-done">Done</div>
                </div>
                <div class="goal">
                    <div class="goal-icon">🎯</div>
                    <div class="goal-content">
                        <div class="goal-title">Solve 5 questions</div>
                        <div class="goal-description">Practice your current topic</div>
                    </div>
                    <div class="goal-status goal-pending">3/5</div>
                </div>
                <div class="goal">
                    <div class="goal-icon">📖</div>
                    <div class="goal-content">
                        <div class="goal-title">Review one topic</div>
                        <div class="goal-description">Strengthen your understanding</div>
                    </div>
                    <div class="goal-status goal-pending">0/1</div>
                </div>
            </div>
            """), unsafe_allow_html=True)

    # =====================================================
    # SECOND ROW — SUBJECT PROGRESS + ACHIEVEMENTS
    # =====================================================

    subject_col, achievement_col = st.columns([1.7, 1], gap="large")

    with subject_col:

        subject_rows = "\n".join(
            _html(f"""
                <div class="subject-row">
                    <div class="subject-header">
                        <div class="subject-name">{subject}</div>
                        <div class="subject-percent">{percentage}%</div>
                    </div>
                    <div class="subject-track">
                        <div class="subject-fill" style="width: {percentage}%;"></div>
                    </div>
                </div>
                """)
            for subject, percentage in st.session_state.subject_progress.items()
        )

        subject_card = _html(f"""
            <div class="dashboard-card">
                <div class="card-title">📚 Subject Progress</div>
                <div class="card-subtitle">Your current understanding by subject</div>
                {subject_rows}
            </div>
            """)

        st.markdown(subject_card, unsafe_allow_html=True)

    with achievement_col:

        st.markdown(_html("""
            <div class="dashboard-card">
                <div class="card-title">🏆 Achievements</div>
                <div class="card-subtitle">Milestones you've reached</div>
                <div class="achievement">
                    <div class="achievement-icon">🔥</div>
                    <div>
                        <div class="achievement-title">7 Day Streak</div>
                        <div class="achievement-description">Studied for 7 consecutive days</div>
                    </div>
                </div>
                <div class="achievement">
                    <div class="achievement-icon">🧠</div>
                    <div>
                        <div class="achievement-title">Knowledge Builder</div>
                        <div class="achievement-description">Solved 40+ questions</div>
                    </div>
                </div>
                <div class="achievement">
                    <div class="achievement-icon">⭐</div>
                    <div>
                        <div class="achievement-title">High Accuracy</div>
                        <div class="achievement-description">Reached 80%+ accuracy</div>
                    </div>
                </div>
            </div>
            """), unsafe_allow_html=True)

    # =====================================================
    # THIRD ROW — RECENT ACTIVITY + STREAK
    # =====================================================

    activity_col, streak_col = st.columns([1.7, 1], gap="large")

    with activity_col:

        st.markdown(_html("""
            <div class="dashboard-card">
                <div class="card-title">🕘 Recent Activity</div>
                <div class="card-subtitle">Your latest learning activities</div>
                <div class="activity-item">
                    <div class="activity-icon">📚</div>
                    <div class="activity-content">
                        <div class="activity-title">Completed a Study session</div>
                        <div class="activity-time">Today • 20 minutes</div>
                    </div>
                </div>
                <div class="activity-item">
                    <div class="activity-icon">🎯</div>
                    <div class="activity-content">
                        <div class="activity-title">Solved 5 practice questions</div>
                        <div class="activity-time">Today • Programming</div>
                    </div>
                </div>
                <div class="activity-item">
                    <div class="activity-icon">🤖</div>
                    <div class="activity-content">
                        <div class="activity-title">Asked AI Tutor a question</div>
                        <div class="activity-time">Yesterday • Artificial Intelligence</div>
                    </div>
                </div>
            </div>
            """), unsafe_allow_html=True)

    with streak_col:

        st.markdown(_html(f"""
            <div class="streak-card">
                <div class="streak-icon">🔥</div>
                <div class="streak-title">Current Study Streak</div>
                <div class="streak-number">{st.session_state.study_streak} days</div>
                <div class="streak-text">You're building a great learning habit. Keep going!</div>
            </div>
            """), unsafe_allow_html=True)

        st.markdown(_html("""
            <div class="dashboard-card">
                <div class="card-title">🚀 Keep going</div>
                <div class="card-subtitle">Consistency is more important than perfection.</div>
            </div>
            """), unsafe_allow_html=True)