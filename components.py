import streamlit as st


# ==========================================
# Navigation Button
# ==========================================

def navigation_button(label):

    is_active = st.session_state.page == label

    if st.sidebar.button(
        label,
        use_container_width=True,
        key=f"nav_{label}",
        type="primary" if is_active else "secondary"
    ):
        st.session_state.page = label
        st.rerun()


# ==========================================
# Sidebar
# ==========================================

def sidebar():

    # --------------------------------------
    # EduBot Brand
    # --------------------------------------

    brand_col1, brand_col2 = st.sidebar.columns(
        [1, 3],
        gap="small"
    )

    with brand_col1:
        st.markdown(
            """
            <div class="edubot-logo">
                <div class="robot-face">
                    <div class="robot-eye"></div>
                    <div class="robot-eye"></div>
                    <div class="robot-mouth"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with brand_col2:
        st.markdown(
            """
            <div class="edubot-brand-text">
                <div class="edubot-name">EduBot</div>
                <div class="edubot-tagline">
                    AI Learning Assistant
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------
    # Divider
    # --------------------------------------

    st.sidebar.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )

    # --------------------------------------
    # Main Menu
    # --------------------------------------

    st.sidebar.markdown(
        '<div class="sidebar-section-title">MAIN MENU</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------
    # Navigation
    # --------------------------------------

    navigation_button("Home")
    navigation_button("Study")
    navigation_button("AI Tutor")
    navigation_button("Solve")
    navigation_button("Practice")
    navigation_button("Progress")
    navigation_button("Exam Prep")

    # --------------------------------------
    # Spacer
    # --------------------------------------

    st.sidebar.markdown(
        '<div class="sidebar-profile-space"></div>',
        unsafe_allow_html=True
    )

    # --------------------------------------
    # Profile Divider
    # --------------------------------------

    st.sidebar.markdown(
        '<div class="profile-divider"></div>',
        unsafe_allow_html=True
    )

    # --------------------------------------
    # User Profile
    # --------------------------------------

    user_name = st.session_state.get(
        "user_name",
        "Muhammad Ahmed"
    )

    profile_col1, profile_col2 = st.sidebar.columns(
        [1, 3],
        gap="small"
    )

    with profile_col1:
        st.markdown(
            '<div class="profile-avatar">👤</div>',
            unsafe_allow_html=True
        )

    with profile_col2:
        st.markdown(
            f'<div class="profile-name">{user_name}</div>',
            unsafe_allow_html=True
        )