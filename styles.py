import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>

        /* =========================================================
           EDUBOT — GLOBAL DESIGN SYSTEM
           ========================================================= */

        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        :root {
            /* Primary / secondary / accent — from the EduBot palette */
            --navy: #17324D;
            --navy-light: #E9EEF2;
            --teal: #2A9D8F;
            --teal-light: #E5F2F0;
            --yellow: #F4C95D;
            --yellow-light: #FCF3DC;

            /* Surfaces + text */
            --bg: #F7F8F5;
            --white: #FFFFFF;
            --text: #24313D;
            --muted: #687684;
            --border: #E4E7E1;

            /* Status */
            --success: #3FA66B;
            --success-light: #E7F5EC;
            --warning: #E5A93D;
            --warning-light: #FBF0DC;
            --error: #D95D5D;
            --error-light: #FBEAEA;

            --shadow-sm: 0 5px 18px rgba(23, 50, 77, 0.055);
            --shadow-md: 0 12px 30px rgba(23, 50, 77, 0.09);
        }

        /* =========================================================
           GLOBAL
           ========================================================= */

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: var(--text);
        }

        .stApp {
            background:
                radial-gradient(
                    circle at 90% 5%,
                    rgba(42,157,143,.045),
                    transparent 25%
                ),
                var(--bg);
        }

        .main .block-container {
            max-width: 1450px;
            padding: 2.4rem 3rem 4rem;
        }

        #MainMenu,
        footer {
            visibility: hidden;
        }

        header[data-testid="stHeader"] {
            background: transparent;
        }

        /* =========================================================
           SIDEBAR
           ========================================================= */

        section[data-testid="stSidebar"] {
            background: var(--navy);
            border-right: none;
        }

        section[data-testid="stSidebar"] > div {
            padding: 1.2rem 1rem;
        }
.edubot-brand-text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 48px;
}

.edubot-name {
    color: var(--white) !important;
    font-size: 16px;
    font-weight: 700;
    line-height: 1.3;
}

.edubot-tagline {
    color: #AFC0D0 !important;
    font-size: 11px;
    font-weight: 500;
    line-height: 1.3;
}
        .edubot-logo {
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--white);
            border-radius: 14px;
            box-shadow: 0 5px 15px rgba(23,50,77,.15);
        }

        .sidebar-divider,
        .profile-divider {
            height: 1px;
            background: rgba(255,255,255,.12);
        }

        .sidebar-divider {
            margin: 24px 0;
        }

        .profile-divider {
            margin: 8px 0 14px;
        }

        .sidebar-section-title {
            color: #AFC0D0;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1.4px;
            margin-bottom: 9px;
            padding-left: 12px;
        }

        section[data-testid="stSidebar"] div.stButton > button {
            width: 100%;
            height: 45px;
            margin: 2px 0;
            padding: 0 15px;

            border: none !important;
            border-radius: 10px;

            background: transparent !important;
            color: #C5D1DC !important;

            font-size: 14px;
            font-weight: 500;

            text-align: left;
            justify-content: flex-start;

            box-shadow: none !important;
            transition: all .18s ease;
        }

        section[data-testid="stSidebar"] div.stButton > button:hover {
            background: rgba(42,157,143,.14) !important;
            color: var(--white) !important;
            transform: translateX(2px);
        }

        section[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
            background: rgba(42,157,143,.20) !important;
            color: var(--white) !important;
            font-weight: 600 !important;
        }

        section[data-testid="stSidebar"] div.stButton > button[kind="primary"]::before {
            content: "";
            position: absolute;
            left: 0;
            top: 8px;
            bottom: 8px;
            width: 3px;
            background: var(--teal);
            border-radius: 0 4px 4px 0;
        }

        .profile-avatar {
            width: 42px;
            height: 42px;
            display: flex;
            align-items: center;
            justify-content: center;

            background: rgba(255,255,255,.10);
            border-radius: 50%;

            font-size: 18px;
        }

        .profile-name {
            color: var(--white) !important;
            font-size: 15px;
            font-weight: 600;
            line-height: 42px;

            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;

            padding-left: 4px;
        }

        /* =========================================================
           HEADER
           ========================================================= */

        .home-header {
            margin-bottom: 25px;
        }

        .home-header .eyebrow {
            color: var(--teal);
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1.7px;
            margin-bottom: 7px;
        }

        .home-header h1 {
            color: var(--navy);
            font-size: 38px;
            line-height: 1.12;
            font-weight: 800;
            letter-spacing: -1.4px;
            margin: 0;
        }

        .home-header p {
            color: var(--muted);
            font-size: 14px;
            margin: 8px 0 0;
        }

        .wave {
            display: inline-block;
            transform-origin: 70% 70%;
        }

        /* =========================================================
           HERO
           ========================================================= */

        .hero-card {
            min-height: 315px;
            padding: 42px 48px;

            border-radius: 25px;
            position: relative;
            overflow: hidden;

            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 35px;

            background:
                radial-gradient(
                    circle at 90% 20%,
                    rgba(42,157,143,.17),
                    transparent 28%
                ),
                linear-gradient(
                    135deg,
                    #FFFFFF 0%,
                    #FFFFFF 55%,
                    var(--teal-light) 100%
                );

            border: 1px solid rgba(42,157,143,.13);
            box-shadow: var(--shadow-md);
        }

        .hero-card::before {
            content: "";
            position: absolute;

            width: 240px;
            height: 240px;

            border: 1px solid rgba(42,157,143,.08);
            border-radius: 50%;

            right: 105px;
            top: -125px;
        }

        .hero-card::after {
            content: "";
            position: absolute;

            width: 350px;
            height: 350px;

            border: 1px solid rgba(23,50,77,.045);
            border-radius: 50%;

            right: -110px;
            bottom: -235px;
        }

        .hero-content {
            position: relative;
            z-index: 3;
            max-width: 670px;
        }

        .hero-kicker {
            color: var(--teal);
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1.35px;
            margin-bottom: 12px;
        }

        .hero-kicker .spark {
            margin-right: 5px;
            font-size: 13px;
        }

        .hero-content h2 {
            color: var(--navy);
            font-size: 42px;
            line-height: 1.06;
            letter-spacing: -1.8px;
            font-weight: 800;
            margin: 0;
        }

        .hero-content h2 span {
            color: var(--teal);
        }

        .hero-content p {
            color: var(--muted);
            font-size: 14px;
            line-height: 1.65;
            max-width: 590px;
            margin: 15px 0 0;
        }

        .hero-mini-stats {
            display: flex;
            gap: 28px;
            margin-top: 26px;
        }

        .hero-mini-stats div {
            display: flex;
            flex-direction: column;
        }

        .hero-mini-stats strong {
            color: var(--navy);
            font-size: 17px;
            font-weight: 800;
        }

        .hero-mini-stats span {
            color: var(--muted);
            font-size: 10px;
            margin-top: 2px;
        }

        /* =========================================================
           HERO ROBOT
           ========================================================= */

        .hero-visual {
            width: 285px;
            height: 235px;
            flex: 0 0 285px;

            border-radius: 24px;
            position: relative;
            overflow: hidden;

            display: flex;
            align-items: center;
            justify-content: center;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,.95),
                    rgba(232,243,241,.82)
                );

            border: 1px solid rgba(42,157,143,.12);
            box-shadow: inset 0 0 45px rgba(42,157,143,.055);

            z-index: 2;
        }

        .visual-glow {
            position: absolute;

            width: 155px;
            height: 155px;

            background: var(--yellow);
            opacity: .18;

            border-radius: 50%;
            filter: blur(18px);
        }

        .robot-orb {
            width: 104px;
            height: 104px;

            border-radius: 50%;
            background: var(--navy);

            box-shadow:
                0 14px 35px rgba(23,50,77,.20),
                inset 0 0 0 8px rgba(255,255,255,.055);

            position: relative;
            z-index: 3;

            display: flex;
            align-items: center;
            justify-content: center;
        }

        .hero-visual .robot-face {
            width: 55px;
            height: 43px;

            background: #F7FBFC;
            border-radius: 13px;

            position: relative;

            display: flex;
            align-items: center;
            justify-content: center;

            gap: 10px;
        }

        .hero-visual .robot-face span {
            width: 7px;
            height: 7px;

            background: var(--teal);
            border-radius: 50%;
        }

        .hero-visual .robot-face i {
            position: absolute;

            width: 16px;
            height: 4px;

            background: var(--teal);
            border-radius: 5px;

            bottom: 7px;
        }

        .robot-antenna {
            position: absolute;

            width: 3px;
            height: 17px;

            background: var(--navy);

            top: -13px;
            left: 50%;

            transform: translateX(-50%);
        }

        .robot-antenna::before {
            content: "";

            position: absolute;

            width: 8px;
            height: 8px;

            border-radius: 50%;
            background: var(--teal);

            top: -5px;
            left: -2.5px;
        }

        .floating-card {
            position: absolute;
            z-index: 5;

            background: rgba(255,255,255,.92);

            border: 1px solid rgba(23,50,77,.08);
            border-radius: 12px;

            padding: 8px 11px;

            font-size: 10px;
            font-weight: 700;
            color: var(--navy);

            box-shadow: 0 8px 20px rgba(23,50,77,.10);

            backdrop-filter: blur(8px);
        }

        .floating-card span {
            color: var(--teal);
            margin-right: 4px;
        }

        .floating-top {
            top: 27px;
            right: 20px;
        }

        .floating-bottom {
            left: 18px;
            bottom: 23px;
        }

        .orbit {
            position: absolute;

            border: 1px dashed rgba(42,157,143,.20);
            border-radius: 50%;
        }

        .orbit-one {
            width: 180px;
            height: 75px;
            transform: rotate(-18deg);
        }

        .orbit-two {
            width: 220px;
            height: 105px;
            transform: rotate(25deg);
        }

        .hero-action-space {
            height: 12px;
        }

        /* =========================================================
           SECTION HEADINGS
           ========================================================= */

        .section-heading {
            margin: 28px 0 14px;
        }

        .section-heading h3 {
            color: var(--navy);
            font-size: 19px;
            font-weight: 800;
            letter-spacing: -.45px;
            margin: 0;
        }

        .section-heading p {
            color: var(--muted);
            font-size: 12px;
            margin: 4px 0 0;
        }

        .progress-heading {
            margin-top: 32px;
        }

        .lower-heading {
            margin-top: 32px;
        }

        /* =========================================================
           BUTTONS
           ========================================================= */

        .main .stButton > button {
            min-height: 40px;

            border-radius: 11px !important;
            border: 1px solid var(--border);

            background: var(--white);
            color: var(--navy);

            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 12px;
            font-weight: 700;

            transition: all .18s ease;
        }

        .main .stButton > button:hover {
            border-color: var(--teal);
            color: var(--teal);

            transform: translateY(-1px);

            box-shadow:
                0 7px 16px rgba(42,157,143,.08);
        }

        .main .stButton > button[kind="primary"] {
            min-height: 44px;
            padding: 0 20px;

            border: none !important;
            border-radius: 11px !important;

            background: var(--navy) !important;
            color: var(--white) !important;

            box-shadow:
                0 7px 16px rgba(23,50,77,.14);
        }

        .main .stButton > button[kind="primary"]:hover {
            background: var(--teal) !important;
            color: var(--white) !important;

            transform: translateY(-2px);

            box-shadow:
                0 9px 20px rgba(42,157,143,.18);
        }

        /* =========================================================
           CARDS
           ========================================================= */

        [data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--white) !important;

            border: 1px solid var(--border) !important;
            border-radius: 17px !important;

            box-shadow: var(--shadow-sm);

            transition: all .2s ease;
        }

        [data-testid="stVerticalBlockBorderWrapper"]:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
        }

        /* =========================================================
           QUICK ACCESS
           ========================================================= */

        .tool-icon {
            width: 46px;
            height: 46px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 13px;

            font-size: 19px;
            margin-bottom: 12px;
        }

        .tool-icon.teal,
        .stat-icon.teal {
            background: var(--teal-light);
            color: var(--teal);
        }

        .tool-icon.blue,
        .stat-icon.blue {
            background: var(--navy-light);
            color: var(--navy);
        }

        .tool-icon.yellow {
            background: var(--yellow-light);
        }

        .tool-icon.purple {
            background: var(--warning-light);
        }

        .tool-title {
            color: var(--navy);
            font-size: 16px;
            font-weight: 800;
        }

        .tool-description {
            color: var(--muted);

            font-size: 11px;
            line-height: 1.55;

            min-height: 36px;

            margin: 5px 0 16px;
        }

        /* =========================================================
           METRICS
           ========================================================= */

        [data-testid="stMetric"] {
            background: transparent;
            border: none;
            padding: 0;
            box-shadow: none;
        }

        [data-testid="stMetricLabel"] {
            color: var(--muted) !important;
            font-size: 11px !important;
            font-weight: 600 !important;
        }

        [data-testid="stMetricValue"] {
            color: var(--navy) !important;
            font-size: 27px !important;
            font-weight: 800 !important;
        }

        .stat-icon {
            width: 42px;
            height: 42px;

            border-radius: 12px;

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 17px;
            margin-bottom: 10px;
        }

        .stat-icon.orange {
            background: var(--warning-light);
        }

        /* =========================================================
           PROGRESS
           ========================================================= */

        .stProgress {
            margin: 8px 0 0;
        }

        .stProgress > div > div {
            background: var(--border);
            border-radius: 20px;
        }

        .stProgress > div > div > div {
            background: var(--teal);
            border-radius: 20px;
        }

        /* =========================================================
           ACTIVITY
           ========================================================= */

        .activity-row {
            display: flex;
            align-items: center;

            gap: 12px;
            padding: 5px 0;
        }

        .activity-icon {
            width: 38px;
            height: 38px;

            flex: 0 0 38px;

            border-radius: 11px;
            background: var(--navy-light);

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 16px;
        }

        .activity-info {
            min-width: 0;
            flex: 1;

            display: flex;
            flex-direction: column;
        }

        .activity-info strong {
            color: var(--navy);
            font-size: 12px;
            font-weight: 700;
        }

        .activity-info span {
            color: var(--muted);
            font-size: 10px;
            margin-top: 2px;
        }

        .activity-time {
            color: #98A4AE;
            font-size: 10px;
            white-space: nowrap;
        }

        .activity-divider {
            height: 1px;
            background: var(--border);
            margin: 12px 0;
        }

        /* =========================================================
           CHECKBOXES
           ========================================================= */

        [data-testid="stCheckbox"] label {
            color: var(--text) !important;
            font-size: 12px !important;
        }

        [data-testid="stCheckbox"] {
            margin: 4px 0;
        }

        /* =========================================================
           RECOMMENDATION
           ========================================================= */

        .recommendation-space {
            height: 18px;
        }

        .recommendation {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .recommendation-icon {
            width: 44px;
            height: 44px;

            flex: 0 0 44px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 13px;
            background: var(--yellow-light);

            font-size: 18px;
        }

        .recommendation-title {
            color: var(--navy);
            font-size: 14px;
            font-weight: 800;
        }

        .recommendation-text {
            color: var(--muted);
            font-size: 11px;
            line-height: 1.5;
            margin-top: 3px;
        }

        .main .stCaption {
            color: var(--muted);
        }

        .main hr {
            border-color: var(--border);
        }

        /* =========================================================
           RESPONSIVE
           ========================================================= */

        @media (max-width: 1050px) {

            .main .block-container {
                padding: 2rem 1.5rem 3rem;
            }

            .hero-card {
                padding: 34px;
            }

            .hero-visual {
                width: 245px;
                flex-basis: 245px;
            }
        }

        @media (max-width: 850px) {

            .hero-card {
                flex-direction: column;
                align-items: flex-start;
            }

            .hero-visual {
                width: 100%;
                flex-basis: auto;
            }

            .hero-content h2 {
                font-size: 34px;
            }
        }

        @media (max-width: 650px) {

            .main .block-container {
                padding: 1.3rem 1rem 2.5rem;
            }

            .home-header h1 {
                font-size: 30px;
            }

            .hero-card {
                padding: 28px 24px;
                border-radius: 20px;
            }

            .hero-mini-stats {
                gap: 17px;
                flex-wrap: wrap;
            }
        }
/* /* ==========================================
   EDUBOT - STUDY PAGE
   ========================================== */


/* ==========================================
   HEADER
   ========================================== */

.study-header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    margin-bottom: 30px;
    padding: 8px 2px;
}

.study-header-content {
    max-width: 700px;
}

.study-eyebrow {
    color: #0F766E !important;
    font-size: 11px !important;
    font-weight: 800 !important;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.study-header h1 {
    color: #172033 !important;
    font-size: 38px !important;
    font-weight: 750 !important;
    line-height: 1.15 !important;
    margin: 0 0 8px 0 !important;
}

.study-header p {
    color: #64748B !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
    margin: 0 !important;
}

.study-header-badge {
    display: flex;
    align-items: center;
    gap: 12px;

    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;

    padding: 13px 18px;

    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
}

.study-header-badge > span {
    width: 38px;
    height: 38px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #E6FFFA;
    color: #0F766E;

    border-radius: 10px;

    font-size: 18px;
}

.study-header-badge strong {
    display: block;
    color: #172033 !important;
    font-size: 13px;
}

.study-header-badge small {
    display: block;
    color: #94A3B8 !important;
    font-size: 11px;
    margin-top: 2px;
}


/* ==========================================
   SELECTOR
   ========================================== */

.study-selector-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;

    padding: 20px 22px 5px 22px;

    box-shadow: 0 3px 12px rgba(15, 23, 42, 0.035);

    margin-bottom: 4px;
}

.selector-heading {
    display: flex;
    align-items: center;
    gap: 13px;
}

.selector-icon {
    width: 38px;
    height: 38px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #E6FFFA;
    color: #0F766E;

    border-radius: 10px;

    font-size: 16px;
}

.selector-heading h3 {
    color: #172033 !important;
    font-size: 16px !important;
    margin: 0 0 3px 0 !important;
}

.selector-heading p {
    color: #64748B !important;
    font-size: 13px !important;
    margin: 0 !important;
}


/* ==========================================
   STREAMLIT SELECTBOX
   ========================================== */

div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 10px !important;
    min-height: 46px !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: #0F9D91 !important;
}

div[data-baseweb="select"] span {
    color: #172033 !important;
}

label[data-testid="stWidgetLabel"] p {
    color: #64748B !important;
    font-size: 11px !important;
    font-weight: 750 !important;
    letter-spacing: 0.8px !important;
}


/* ==========================================
   TOPIC PROGRESS
   ========================================== */

.study-progress-row {
    display: flex;
    align-items: center;
    justify-content: space-between;

    margin: 22px 2px 18px 2px;
}

.study-progress-row > div:first-child span {
    display: block;

    color: #0F766E !important;
    font-size: 10px !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
}

.study-progress-row > div:first-child strong {
    display: block;

    color: #172033 !important;
    font-size: 13px !important;

    margin-top: 3px;
}

.study-progress-container {
    width: 180px;
}

.study-progress-bar {
    width: 100%;
    height: 6px;

    background: #E2E8F0;

    border-radius: 10px;

    overflow: hidden;
}

.study-progress-fill {
    height: 100%;

    background: #0F9D91;

    border-radius: 10px;

    transition: width 0.3s ease;
}


/* ==========================================
   MAIN LEARNING CARD
   ========================================== */

.learning-card {
    background: #FFFFFF;

    border: 1px solid #E2E8F0;
    border-radius: 20px;

    padding: 30px;

    box-shadow: 0 5px 20px rgba(15, 23, 42, 0.055);

    margin-top: 4px;
}


/* ==========================================
   LEARNING CARD HEADER
   ========================================== */

.learning-card-header {
    display: flex;
    align-items: center;

    gap: 15px;
}

.learning-icon {
    width: 58px;
    height: 58px;
    min-width: 58px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #E6FFFA;

    border-radius: 15px;

    font-size: 25px;
}

.learning-title {
    flex: 1;
}

.learning-title span {
    color: #0F766E !important;

    font-size: 11px !important;
    font-weight: 750 !important;

    letter-spacing: 0.5px;
}

.learning-title h2 {
    color: #172033 !important;

    font-size: 25px !important;
    font-weight: 700 !important;

    margin: 3px 0 0 0 !important;
}

.learning-status {
    background: #ECFDF5;

    color: #047857 !important;

    border-radius: 20px;

    padding: 7px 12px;

    font-size: 11px !important;
    font-weight: 700 !important;
}

.learning-status span {
    font-size: 8px;
}


/* ==========================================
   DIVIDER
   ========================================== */

.learning-divider {
    height: 1px;

    background: #E2E8F0;

    margin: 25px 0;
}


/* ==========================================
   LEARNING SECTION
   ========================================== */

.learning-section {
    display: flex;

    gap: 20px;

    margin-bottom: 25px;
}

.section-number {
    color: #0F766E !important;

    font-size: 11px !important;
    font-weight: 800 !important;

    min-width: 30px;

    padding-top: 3px;
}

.learning-section h3 {
    color: #172033 !important;

    font-size: 18px !important;
    font-weight: 700 !important;

    margin: 0 0 10px 0 !important;
}

.learning-section p {
    color: #526174 !important;

    font-size: 14px !important;
    line-height: 1.75 !important;

    margin: 0 0 9px 0 !important;
}

.learning-section strong {
    color: #334155 !important;
}


/* ==========================================
   KEY CONCEPTS
   ========================================== */

.key-concepts-section {
    margin-top: 10px;
}

.key-concepts-content {
    width: 100%;
}

.concept-grid {
    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 10px;

    margin-top: 14px;
}

.concept-item {
    display: flex;
    align-items: center;

    gap: 12px;

    background: #F8FAFC;

    border: 1px solid #EEF2F7;

    border-radius: 12px;

    padding: 14px;

    transition: all 0.2s ease;
}

.concept-item:hover {
    border-color: #BFE9E4;

    transform: translateY(-1px);

    box-shadow: 0 3px 10px rgba(15, 23, 42, 0.04);
}

.concept-icon {
    width: 34px;
    height: 34px;
    min-width: 34px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #FFFFFF;

    border: 1px solid #DCE7EA;

    border-radius: 9px;

    color: #0F766E !important;

    font-size: 10px !important;
    font-weight: 800 !important;
}

.concept-item strong {
    display: block;

    color: #273449 !important;

    font-size: 12px !important;

    margin-bottom: 3px;
}

.concept-item span {
    display: block;

    color: #7A8798 !important;

    font-size: 11px !important;

    line-height: 1.4;
}


/* ==========================================
   EXAMPLE
   ========================================== */

.example-section {
    display: flex;

    align-items: flex-start;

    gap: 14px;

    background: #FFFBEB;

    border: 1px solid #FDE68A;

    border-radius: 13px;

    padding: 18px;

    margin-top: 8px;
}

.example-icon {
    font-size: 20px;

    width: 35px;
    min-width: 35px;
    height: 35px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #FFFFFF;

    border-radius: 9px;
}

.example-section span {
    color: #B45309 !important;

    font-size: 10px !important;
    font-weight: 800 !important;

    letter-spacing: 0.7px;
}

.example-section h3 {
    color: #172033 !important;

    font-size: 15px !important;

    margin: 3px 0 5px 0 !important;
}

.example-section p {
    color: #6B7280 !important;

    font-size: 13px !important;
    line-height: 1.6 !important;

    margin: 0 !important;
}


/* ==========================================
   ACTIONS
   ========================================== */

.study-action-heading {
    margin: 28px 0 13px 2px;
}

.study-action-heading h3 {
    color: #172033 !important;

    font-size: 17px !important;

    margin: 0 0 3px 0 !important;
}

.study-action-heading p {
    color: #64748B !important;

    font-size: 13px !important;

    margin: 0 !important;
}


/* ==========================================
   BUTTONS
   ========================================== */

div.stButton > button {
    min-height: 48px !important;

    background: #FFFFFF !important;

    color: #263449 !important;

    border: 1px solid #CBD5E1 !important;

    border-radius: 11px !important;

    font-size: 13px !important;

    font-weight: 650 !important;

    transition: all 0.2s ease !important;
}

div.stButton > button:hover {
    border-color: #0F9D91 !important;

    color: #0F766E !important;

    background: #F0FDFA !important;

    transform: translateY(-1px);
}

.action-description {
    color: #8491A3 !important;

    text-align: center;

    font-size: 11px !important;

    line-height: 1.5;

    margin-top: 7px;
}


/* ==========================================
   FEEDBACK
   ========================================== */

.study-feedback {
    display: flex;

    align-items: flex-start;

    gap: 14px;

    background: #F0FDFA;

    border: 1px solid #BFE9E4;

    border-radius: 13px;

    padding: 16px 18px;

    margin-top: 18px;
}

.feedback-icon {
    width: 36px;
    height: 36px;
    min-width: 36px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #FFFFFF;

    border-radius: 9px;

    font-size: 17px;
}

.study-feedback strong {
    color: #172033 !important;

    font-size: 13px !important;
}

.study-feedback p {
    color: #526174 !important;

    font-size: 12px !important;

    line-height: 1.5;

    margin: 4px 0 0 0 !important;
}

.success-feedback {
    background: #F0FDF4;

    border-color: #BBF7D0;
}
/* ============================================================
   FIX — force readable text on native Streamlit components
   (prevents white-on-white when the base theme is dark)
   ============================================================ */
.main [data-testid="stMarkdownContainer"] p,
.main [data-testid="stMarkdownContainer"] li,
.main [data-testid="stMarkdownContainer"] span,
.main [data-testid="stMarkdownContainer"] strong,
.main [data-testid="stCaptionContainer"],
.main [data-testid="stCaptionContainer"] *,
.main [data-testid="stWidgetLabel"] p {
    color: var(--text) !important;
}

.main [data-testid="stAlert"] * {
    color: var(--navy) !important;
}

div[data-baseweb="select"] input,
div[data-baseweb="select"] div[role="button"] {
    color: var(--text) !important;
}
div[class*="st-key-qa_card_"] {
    background: white;
    border: 1px solid #E5EAEE;
    border-radius: 14px;
    padding: 10px 14px 4px 14px;
    margin-bottom: 10px;
    transition: all 0.18s ease;
}

div[class*="st-key-qa_card_"]:hover {
    border-color: #62CFC3;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(15, 118, 110, 0.08);
}

div[class*="st-key-qa_card_"] .stButton > button {
    text-align: left !important;
    justify-content: flex-start !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    font-size: 14px !important;
    padding: 4px 2px !important;
}

div[class*="st-key-qa_card_"] .stButton > button:hover {
    color: #0F766E !important;
    transform: none !important;
}

div[class*="st-key-qa_card_"] [data-testid="stCaptionContainer"] {
    margin-top: 1px !important;
    padding-left: 2px;
}
   /* Sidebar radio menu text visibility fix */
section[data-testid="stSidebar"] [data-testid="stRadio"] label {
    color: #FFFFFF !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    color: var(--teal) !important;
}

section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label div p {
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #AFC0D0 !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] .stMarkdown {
    color: #FFFFFF !important;
}
  section[data-testid="stSidebar"] [data-testid="stRadio"] > div {
    gap: 4px;
}

section[data-testid="stSidebar"] [data-testid="stRadio"] label {
    background: rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 10px 14px !important;
    margin: 2px 0;
    transition: all 0.18s ease;
    display: flex;
    width: 100%;
}

section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: rgba(42,157,143,0.20);
    transform: translateX(3px);
}    
      /* ===== LOGO POLISH ===== */
section[data-testid="stSidebar"] img {
    background: linear-gradient(135deg, #FFFFFF, #E9EEF2);
    border-radius: 16px;
    padding: 10px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.18);
}

/* ===== SIDEBAR BRAND HEADER CARD ===== */
section[data-testid="stSidebar"] > div:first-child {
    padding-top: 8px;
}

/* ===== CARD DEPTH UPGRADE (Home / Progress / Quiz cards) ===== */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 20px !important;
    box-shadow: 0 10px 28px rgba(11,31,58,0.10) !important;
    border: 1px solid rgba(233,238,242,0.9) !important;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover {
    box-shadow: 0 16px 36px rgba(11,31,58,0.16) !important;
    transform: translateY(-4px) !important;
}

/* ===== st.success / st.info boxes on Home page — make them card-like ===== */
[data-testid="stAlert"] {
    border-radius: 16px !important;
    padding: 18px 20px !important;
    box-shadow: 0 6px 18px rgba(11,31,58,0.08) !important;
    border: none !important;
}

/* ===== Titles: bigger, bolder, tighter letter spacing ===== */
h1 {
    font-weight: 800 !important;
    letter-spacing: -1px !important;
}

/* ===== MOBILE RESPONSIVE FIXES ===== */
@media (max-width: 650px) {
    section[data-testid="stSidebar"] [data-testid="stRadio"] label {
        padding: 12px 14px !important;
        font-size: 15px !important;
    }

    .main .block-container {
        padding: 1rem 0.8rem 2rem !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px !important;
    }
}  
        </style>
        """,

        unsafe_allow_html=True,
    )
