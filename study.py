import streamlit as st


def _html(s: str) -> str:
    """Flatten a triple-quoted HTML string to zero indentation per line,
    so Streamlit's markdown parser never mistakes it for a code block."""
    lines = [line.strip() for line in s.strip("\n").splitlines()]
    return "\n".join(lines)


def study_page():

    topic_data = {
        "Programming Fundamentals": [
            "Variables & Data Types", "Conditional Statements", "Loops", "Functions"
        ],
        "Object-Oriented Programming": [
            "Classes & Objects", "Inheritance", "Polymorphism", "Encapsulation"
        ],
        "Data Structures & Algorithms": [
            "Arrays", "Linked Lists", "Stacks & Queues", "Searching & Sorting"
        ],
        "Database Systems": [
            "Database Concepts", "SQL", "Normalization", "Relationships"
        ],
        "Computer Networks": [
            "Network Basics", "OSI Model", "TCP/IP", "Network Security"
        ],
        "Artificial Intelligence": [
            "Introduction to AI", "Intelligent Agents", "Search Algorithms", "Knowledge Representation"
        ],
        "Machine Learning": [
            "Introduction to ML", "Supervised Learning", "Unsupervised Learning", "Model Evaluation"
        ]
    }

    # ==========================================
    # HEADER
    # ==========================================
    st.markdown(_html("""
        <div class="study-header">
            <div class="study-header-content">
                <div class="study-eyebrow">✦ LEARNING PATH</div>
                <h1>📚 Study smarter.</h1>
                <p>Choose a subject, explore a topic, and build your
                understanding step by step with EduBot.</p>
            </div>
            <div class="study-header-badge">
                <span>🤖</span>
                <div>
                    <strong>EduBot Tutor</strong>
                    <small>Always ready to help</small>
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)

    # ==========================================
    # LEARNING PATH SELECTOR
    # ==========================================
    st.markdown(_html("""
        <div class="study-selector-card">
            <div class="selector-heading">
                <div class="selector-icon">🎯</div>
                <div>
                    <h3>Choose your learning path</h3>
                    <p>Select a subject and the topic you want to explore.</p>
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox("SUBJECT", list(topic_data.keys()), key="study_subject")
    with col2:
        topic = st.selectbox("TOPIC", topic_data[subject], key="study_topic")

    # ==========================================
    # PROGRESS
    # ==========================================
    current_index = topic_data[subject].index(topic)
    total_topics = len(topic_data[subject])
    topic_number = current_index + 1
    percentage = int((topic_number / total_topics) * 100)

    st.markdown(_html(f"""
        <div class="study-progress-row">
            <div>
                <span>TOPIC {topic_number} OF {total_topics}</span>
                <strong>{topic}</strong>
            </div>
            <div class="study-progress-container">
                <div class="study-progress-bar">
                    <div class="study-progress-fill" style="width:{percentage}%;"></div>
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)

    # ==========================================
    # MAIN LEARNING CARD
    # ==========================================
    st.markdown(_html(f"""
        <div class="learning-card">
            <div class="learning-card-header">
                <div class="learning-icon">📚</div>
                <div class="learning-title">
                    <span>{subject}</span>
                    <h2>{topic}</h2>
                </div>
                <div class="learning-status"><span>●</span> Currently learning</div>
            </div>

            <div class="learning-divider"></div>

            <div class="learning-section">
                <div class="section-number">01</div>
                <div>
                    <h3>Understanding the topic</h3>
                    <p><strong>{topic}</strong> is an important concept within
                    <strong>{subject}</strong>. This lesson will help you understand
                    the concept clearly before moving on to examples and practice.</p>
                    <p>EduBot simplifies complex concepts and presents them step by
                    step so they are easier to understand.</p>
                </div>
            </div>

            <div class="learning-divider"></div>

            <div class="learning-section key-concepts-section">
                <div class="section-number">02</div>
                <div class="key-concepts-content">
                    <h3>Key concepts</h3>
                    <div class="concept-grid">
                        <div class="concept-item">
                            <div class="concept-icon">01</div>
                            <div><strong>Core idea</strong><span>Understand the fundamental concept.</span></div>
                        </div>
                        <div class="concept-item">
                            <div class="concept-icon">02</div>
                            <div><strong>How it works</strong><span>Explore the process step by step.</span></div>
                        </div>
                        <div class="concept-item">
                            <div class="concept-icon">03</div>
                            <div><strong>Practical use</strong><span>Connect the concept to real situations.</span></div>
                        </div>
                        <div class="concept-item">
                            <div class="concept-icon">04</div>
                            <div><strong>Remember</strong><span>Review the most important points.</span></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="example-section">
                <div class="example-icon">💡</div>
                <div>
                    <span>LEARN THROUGH EXAMPLE</span>
                    <h3>Put {topic} into context</h3>
                    <p>EduBot can explain <strong>{topic}</strong> using a practical
                    example that connects theory with something you already understand.</p>
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)

    # ==========================================
    # ACTIONS
    # ==========================================
    st.markdown(_html("""
        <div class="study-action-heading">
            <h3>Continue learning</h3>
            <p>Choose how you want to work with this topic.</p>
        </div>
        """), unsafe_allow_html=True)

    action1, action2, action3 = st.columns(3)

    with action1:
        if st.button("🤖 Ask AI Tutor", use_container_width=True, key="study_tutor_button"):
            st.session_state["study_action"] = "tutor"
        st.markdown(_html('<p class="action-description">Ask questions and get personalized explanations.</p>'), unsafe_allow_html=True)

    with action2:
        if st.button("📝 Practice Topic", use_container_width=True, key="study_practice_button"):
            st.session_state["study_action"] = "practice"
        st.markdown(_html('<p class="action-description">Test your understanding with practice questions.</p>'), unsafe_allow_html=True)

    with action3:
        if st.button("✓ Mark Complete", use_container_width=True, key="study_complete_button"):
            st.session_state["study_completed"] = topic
            st.session_state["study_action"] = "complete"
        st.markdown(_html("<p class=\"action-description\">Keep track of the topics you've finished.</p>"), unsafe_allow_html=True)

    # ==========================================
    # ACTION FEEDBACK
    # ==========================================
    action = st.session_state.get("study_action")

    if action == "tutor":
        st.markdown(_html(f"""
            <div class="study-feedback">
                <div class="feedback-icon">🤖</div>
                <div><strong>AI Tutor</strong>
                <p>Ready to help you understand <strong>{topic}</strong>.
                The AI Tutor functionality can be connected here next.</p></div>
            </div>
            """), unsafe_allow_html=True)
    elif action == "practice":
        st.markdown(_html(f"""
            <div class="study-feedback">
                <div class="feedback-icon">📝</div>
                <div><strong>Practice Mode</strong>
                <p>Practice questions for <strong>{topic}</strong>
                can be connected to your Practice section next.</p></div>
            </div>
            """), unsafe_allow_html=True)
    elif action == "complete":
        st.markdown(_html(f"""
            <div class="study-feedback success-feedback">
                <div class="feedback-icon">✓</div>
                <div><strong>Topic completed!</strong>
                <p>Great work! <strong>{topic}</strong>
                has been marked as completed.</p></div>
            </div>
            """), unsafe_allow_html=True)