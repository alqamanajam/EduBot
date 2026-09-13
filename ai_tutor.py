import streamlit as st
from datetime import datetime


def _html(s: str) -> str:
    """Flatten a triple-quoted HTML string to zero indentation per line,
    so Streamlit's markdown parser never mistakes it for a code block."""
    lines = [line.strip() for line in s.strip("\n").splitlines()]
    return "\n".join(lines)


# =========================================================
# STATE
# =========================================================

def initialize_tutor():

    if "tutor_messages" not in st.session_state:
        st.session_state.tutor_messages = [
            {
                "role": "assistant",
                "content": (
                    "Hi! I'm EduBot, your AI Tutor. 👋\n\n"
                    "Choose a subject and topic, then ask me anything. "
                    "I'll help you understand concepts step by step."
                ),
                "time": datetime.now().strftime("%I:%M %p")
            }
        ]

    if "selected_subject" not in st.session_state:
        st.session_state.selected_subject = "Computer Science"

    if "selected_topic" not in st.session_state:
        st.session_state.selected_topic = "Programming Fundamentals"


def add_message(role, content):
    st.session_state.tutor_messages.append(
        {
            "role": role,
            "content": content,
            "time": datetime.now().strftime("%I:%M %p")
        }
    )


# =========================================================
# DEMO AI RESPONSE
# =========================================================

def generate_response(question):

    question_lower = question.lower()

    if "what is" in question_lower or "define" in question_lower:
        return (
            "Great question! Let's understand it simply. 💡\n\n"
            "A concept is easier to understand when we break it into "
            "three parts:\n\n"
            "**1. Definition** — What it means.\n\n"
            "**2. Purpose** — Why we use it.\n\n"
            "**3. Example** — How it works in a real situation.\n\n"
            "If you want, I can also explain this topic with a simple "
            "example or a small diagram."
        )

    if "example" in question_lower:
        return (
            "Sure! Here's a simple example. 🧠\n\n"
            "Imagine you're learning programming. Instead of trying to "
            "understand the entire program at once, divide it into small "
            "parts such as variables, conditions, loops, and functions.\n\n"
            "This makes the concept much easier to understand and remember."
        )

    if "help" in question_lower:
        return (
            "Of course! 🤖\n\n"
            "Tell me the exact concept you're struggling with and I'll "
            "break it down step by step.\n\n"
            "You can ask things like:\n"
            "• Explain this concept simply\n"
            "• Give me an example\n"
            "• Test me with questions\n"
            "• Explain it like I'm a beginner"
        )

    return (
        "That's a good question! 🤖\n\n"
        f"Let's work through **{question}** step by step.\n\n"
        "First, identify the main idea behind the question. "
        "Then break the problem into smaller parts and connect each "
        "part to an example.\n\n"
        "Would you like me to explain this in a **simple way**, "
        "give you an **example**, or **quiz you** on it?"
    )


def handle_prompt(prompt_text):
    """Send a question (typed or from a quick-action button) and rerun."""
    add_message("user", prompt_text)
    add_message("assistant", generate_response(prompt_text))
    st.rerun()


# =========================================================
# CUSTOM CSS  (safe as-is: <style> is read literally by markdown,
# it never suffers from the blank-line code-block bug)
# =========================================================

def tutor_styles():

    st.markdown(
        """
        <style>

        .tutor-header {
            background: linear-gradient(135deg, #0B1F3A 0%, #123B5D 100%);
            padding: 30px 34px;
            border-radius: 20px;
            margin-bottom: 22px;
            color: white;
            box-shadow: 0 8px 25px rgba(11, 31, 58, 0.14);
            position: relative;
            overflow: hidden;
        }

        .tutor-header::after {
            content: "";
            position: absolute;
            width: 220px;
            height: 220px;
            background: rgba(98, 214, 200, 0.12);
            border-radius: 50%;
            right: -60px;
            top: -90px;
        }

        .tutor-header-label {
            color: #62D6C8;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 1.6px;
            margin-bottom: 8px;
            position: relative;
            z-index: 2;
        }

        .tutor-header h1 {
            margin: 0;
            font-size: 32px;
            font-weight: 800;
            color: white;
            position: relative;
            z-index: 2;
        }

        .tutor-header p {
            margin-top: 8px;
            margin-bottom: 0;
            color: #C9DCE9;
            font-size: 14px;
            position: relative;
            z-index: 2;
        }

        .chat-card {
            background: white;
            border: 1px solid #E6EBF0;
            border-radius: 20px;
            padding: 22px;
            box-shadow: 0 6px 22px rgba(11, 31, 58, 0.06);
        }

        .chat-title {
            display: flex;
            align-items: center;
            gap: 10px;
            color: #0B1F3A;
            font-size: 17px;
            font-weight: 800;
            padding-bottom: 15px;
            border-bottom: 1px solid #EDF0F3;
            margin-bottom: 18px;
        }

        .chat-scroll {
            max-height: 480px;
            overflow-y: auto;
            padding-right: 6px;
        }

        .chat-scroll::-webkit-scrollbar { width: 6px; }
        .chat-scroll::-webkit-scrollbar-thumb {
            background: #D8E2E7;
            border-radius: 10px;
        }

        .message-row {
            display: flex;
            align-items: flex-end;
            gap: 8px;
            margin-bottom: 16px;
        }

        .message-row.user { justify-content: flex-end; }
        .message-row.assistant { justify-content: flex-start; }

        .message-avatar {
            width: 30px;
            height: 30px;
            min-width: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 15px;
            background: #E6FFFA;
        }

        .message-bubble {
            max-width: 76%;
            padding: 13px 16px;
            border-radius: 16px;
            font-size: 14px;
            line-height: 1.65;
        }

        .assistant-message {
            background: #F1F7F8;
            color: #253746;
            border-bottom-left-radius: 4px;
        }

        .user-message {
            background: #0F766E;
            color: white;
            border-bottom-right-radius: 4px;
        }

        .message-time {
            font-size: 10px;
            opacity: 0.65;
            margin-top: 7px;
        }

        .section-label {
            color: #0B1F3A;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 0.3px;
            margin: 4px 0 10px 2px;
        }

        .topic-status {
            background: #EFF9F7;
            border: 1px solid #D5EFEB;
            border-radius: 14px;
            padding: 13px 15px;
            margin: 6px 0 20px 0;
        }

        .topic-status-title {
            font-size: 10.5px;
            color: #5B7275;
            font-weight: 700;
            letter-spacing: 0.6px;
        }

        .topic-status-value {
            font-size: 14px;
            color: #0F766E;
            font-weight: 800;
            margin-top: 3px;
        }

        div[data-testid="stTextInput"] input {
            border-radius: 14px !important;
            border: 1px solid #DCE4E9 !important;
            padding: 14px !important;
        }

        div[data-testid="stTextInput"] input:focus {
            border-color: #0F766E !important;
            box-shadow: 0 0 0 1px #0F766E !important;
        }

        .stButton > button {
            border-radius: 12px !important;
            border: 1px solid #E0E7EB !important;
            background: white !important;
            color: #173047 !important;
            font-weight: 700 !important;
            transition: all 0.18s ease !important;
        }

        .stButton > button:hover {
            border-color: #0F766E !important;
            color: #0F766E !important;
            transform: translateY(-1px);
        }

        button[kind="primary"] {
            background: #0F766E !important;
            border: none !important;
            color: white !important;
        }

        button[kind="primary"]:hover {
            background: #0B5A54 !important;
            color: white !important;
        }

        /* =========================================
           QUICK ACTION CARDS
           (targets the keyed containers created with
           st.container(key="qa_card_N") below)
        ========================================= */

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

        </style>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# BUILD THE ENTIRE CHAT CARD AS ONE HTML STRING
# (fixes both the code-block bug AND the "divs not really
# wrapping messages" bug, since it's all one real element)
# =========================================================

def render_chat_card():

    bubbles = []
    for message in st.session_state.tutor_messages:
        role = message["role"]
        content_html = message["content"].replace(chr(10), "<br>")

        if role == "assistant":
            bubbles.append(_html(f"""
                <div class="message-row assistant">
                    <div class="message-avatar">🤖</div>
                    <div class="message-bubble assistant-message">
                        <div>{content_html}</div>
                        <div class="message-time">EduBot • {message["time"]}</div>
                    </div>
                </div>
                """))
        else:
            bubbles.append(_html(f"""
                <div class="message-row user">
                    <div class="message-bubble user-message">
                        <div>{content_html}</div>
                        <div class="message-time">You • {message["time"]}</div>
                    </div>
                </div>
                """))

    messages_html = "\n".join(bubbles)

    card_html = _html(f"""
        <div class="chat-card">
            <div class="chat-title">🤖 <span>Chat with EduBot</span></div>
            <div class="chat-scroll">
                {messages_html}
            </div>
        </div>
        """)

    st.markdown(card_html, unsafe_allow_html=True)


# =========================================================
# AI TUTOR PAGE
# =========================================================

def ai_tutor_page():

    initialize_tutor()
    tutor_styles()

    # HEADER
    st.markdown(_html("""
        <div class="tutor-header">
            <div class="tutor-header-label">✦ YOUR AI LEARNING COMPANION</div>
            <h1>AI Tutor 🤖</h1>
            <p>Ask questions, understand difficult concepts, and learn at your own pace.</p>
        </div>
        """), unsafe_allow_html=True)

    left, right = st.columns([2.4, 1], gap="large")

    # =====================================================
    # LEFT — CHAT
    # =====================================================
    with left:

        render_chat_card()

        st.write("")
        question = st.text_input(
            "Ask your tutor",
            placeholder="Ask anything about your topic...",
            label_visibility="collapsed",
            key="tutor_input"
        )

        send_col, clear_col = st.columns([4, 1])

        with send_col:
            if st.button("Send question  ➜", use_container_width=True, type="primary"):
                if question.strip():
                    handle_prompt(question.strip())

        with clear_col:
            if st.button("Clear", use_container_width=True):
                st.session_state.tutor_messages = []
                add_message("assistant", "Chat cleared! ✨ What would you like to learn?")
                st.rerun()

    # =====================================================
    # RIGHT — CONTEXT + QUICK ACTIONS
    # =====================================================
    with right:

        st.markdown('<div class="section-label">Learning context</div>', unsafe_allow_html=True)

        subject = st.selectbox(
            "Subject",
            [
                "Computer Science", "Artificial Intelligence", "Programming",
                "Database Systems", "Computer Networks", "Software Engineering"
            ],
            key="subject_selector"
        )

        topics = {
            "Computer Science": ["Programming Fundamentals", "Data Structures", "Algorithms", "Operating Systems"],
            "Artificial Intelligence": ["Machine Learning", "Neural Networks", "Computer Vision", "AI Fundamentals"],
            "Programming": ["Variables & Data Types", "Functions", "Loops", "Object-Oriented Programming"],
            "Database Systems": ["SQL", "Normalization", "ER Diagrams", "Transactions"],
            "Computer Networks": ["OSI Model", "TCP/IP", "Routing", "Network Security"],
            "Software Engineering": ["SDLC", "Requirements Engineering", "Software Testing", "Agile Development"]
        }

        topic = st.selectbox("Topic", topics[subject], key="topic_selector")

        st.markdown(_html(f"""
            <div class="topic-status">
                <div class="topic-status-title">CURRENT TOPIC</div>
                <div class="topic-status-value">{topic}</div>
            </div>
            """), unsafe_allow_html=True)

        # QUICK ACTIONS — real, clickable cards
        st.markdown('<div class="section-label">Quick actions</div>', unsafe_allow_html=True)

        quick_actions = [
            ("💡", "Explain simply", "Understand the concept", f"Explain {topic} simply"),
            ("🧩", "Give an example", "See it in practice", f"Give me an example of {topic}"),
            ("📝", "Quiz me", "Test your knowledge", f"Quiz me on {topic}"),
            ("📌", "Summarize", "Review key points", f"Summarize {topic}"),
        ]

        for i, (icon, title, description, prompt_text) in enumerate(quick_actions):
            with st.container(key=f"qa_card_{i}"):
                clicked = st.button(f"{icon}  {title}", key=f"qa_btn_{i}", use_container_width=True)
                st.caption(description)
            if clicked:
                handle_prompt(prompt_text)