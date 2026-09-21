import streamlit as st
from pathlib import Path

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="LiveMind AI",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# SAMPLE DATA
# =========================================================

ACCOUNT_ID = "LM-784521"
BALANCE = 402580.00

REQUIRED_STREAMS = 2
COMPLETED_STREAMS = 0

DAYS_LEFT = 30
MIN_SUPPORT = 5.00


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

html,
body,
[class*="css"] {
    font-family: "Inter", sans-serif;
}

.stApp {

    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(90, 70, 220, 0.25),
            transparent 32%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(0, 190, 255, 0.13),
            transparent 30%
        ),
        #070912;

    color: #f4f7ff;
}

.block-container {

    max-width: 1400px;

    padding-top: 1.5rem;
    padding-bottom: 3rem;
}


/* =========================================================
   BRAND
========================================================= */

.brand {

    font-size: 32px;

    font-weight: 800;

    letter-spacing: -1px;

    color: #ffffff;
}

.ai {

    color: #7dd3fc;
}

.badge {

    display: inline-block;

    margin-left: 9px;

    padding: 5px 10px;

    border-radius: 999px;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 0.7px;

    color: #dbeafe;

    background: rgba(59, 130, 246, 0.16);

    border: 1px solid rgba(96, 165, 250, 0.35);
}

.sub {

    color: #9ca9c8;

    margin-top: 7px;

    font-size: 14px;
}


/* =========================================================
   HERO
========================================================= */

.hero {

    border: 1px solid rgba(150, 170, 255, 0.16);

    border-radius: 24px;

    padding: 28px;

    background:
        linear-gradient(
            135deg,
            rgba(25, 31, 65, 0.96),
            rgba(10, 13, 28, 0.96)
        );

    box-shadow:
        0 18px 60px rgba(0, 0, 0, 0.35);
}


/* =========================================================
   SECTION TITLES
========================================================= */

.section-title {

    font-size: 21px;

    font-weight: 750;

    margin-top: 26px;

    margin-bottom: 13px;

    color: #ffffff;
}


/* =========================================================
   CARDS
========================================================= */

.card {

    background:
        linear-gradient(
            145deg,
            rgba(22, 27, 50, 0.97),
            rgba(11, 14, 29, 0.97)
        );

    border:
        1px solid rgba(145, 160, 210, 0.14);

    border-radius: 20px;

    padding: 22px;

    min-height: 145px;

    box-shadow:
        0 12px 35px rgba(0, 0, 0, 0.22);
}

.label {

    color: #8996b7;

    font-size: 12px;

    margin-bottom: 9px;

    letter-spacing: 0.4px;
}

.value {

    font-size: 29px;

    font-weight: 800;

    letter-spacing: -1px;
}

.green {

    color: #67e8a5;
}

.blue {

    color: #7dd3fc;
}

.purple {

    color: #c4b5fd;
}

.orange {

    color: #fdba74;
}

.small {

    color: #8491b1;

    font-size: 12px;

    margin-top: 7px;
}


/* =========================================================
   REQUIREMENT NOTICE
========================================================= */

.notice {

    border-radius: 18px;

    padding: 20px;

    background:
        linear-gradient(
            90deg,
            rgba(91, 72, 180, 0.20),
            rgba(39, 111, 160, 0.13)
        );

    border:
        1px solid rgba(139, 125, 255, 0.22);
}

.notice-title {

    font-weight: 750;

    font-size: 17px;

    color: #ffffff;
}

.notice-text {

    color: #b8c2dc;

    line-height: 1.65;

    margin-top: 7px;
}


/* =========================================================
   STREAM CARDS
========================================================= */

.stream-card {

    border:
        1px solid rgba(145, 160, 210, 0.14);

    border-radius: 18px;

    padding: 20px;

    background:
        rgba(16, 20, 39, 0.90);
}


/* =========================================================
   BUTTONS
========================================================= */

div.stButton > button {

    border-radius: 12px;

    font-weight: 700;

    min-height: 45px;
}


/* =========================================================
   FOOTER
========================================================= */

.footer {

    text-align: center;

    color: #687493;

    font-size: 11px;

    margin-top: 35px;

    padding-top: 20px;

    border-top:
        1px solid rgba(145, 160, 210, 0.10);
}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# HEADER / LOGO
# =========================================================

logo_path = Path("Logo.png")

if logo_path.exists():

    logo_col, brand_col = st.columns(
        [1, 7],
        vertical_alignment="center"
    )

    with logo_col:

        st.image(
            str(logo_path),
            width=85
        )

    with brand_col:

        st.markdown(
            """
<div class="brand">
    LiveMind <span class="ai">AI</span>
    <span class="badge">PROTOTYPE</span>
</div>

<div class="sub">
    Smart Live Streaming & Creator Dashboard
</div>
""",
            unsafe_allow_html=True
        )

else:

    st.markdown(
        """
<div class="hero">

    <div class="brand">
        LiveMind <span class="ai">AI</span>
        <span class="badge">PROTOTYPE</span>
    </div>

    <div class="sub">
        Smart Live Streaming & Creator Dashboard
    </div>

</div>
""",
        unsafe_allow_html=True
    )


st.write("")


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        "### 🚀 LiveMind AI"
    )

    st.caption(
        "Creator Control Center"
    )

    st.divider()

    st.markdown(
        "**Account**"
    )

    st.code(
        ACCOUNT_ID,
        language=None
    )

    st.markdown(
        "**Navigation**"
    )

    st.button(
        "🏠 Dashboard",
        use_container_width=True
    )

    st.button(
        "🎥 Live Studio",
        use_container_width=True
    )

    st.button(
        "💰 Earnings",
        use_container_width=True
    )

    st.button(
        "⚙️ Account Settings",
        use_container_width=True
    )

    st.divider()

    st.caption(
        "Prototype interface — figures shown are sample data."
    )


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    f"""
<div class="hero">

    <div class="label">
        CREATOR ACCOUNT · {ACCOUNT_ID}
    </div>

    <div style="
        font-size:36px;
        font-weight:850;
        letter-spacing:-1.5px;
        color:#ffffff;
    ">
        Welcome to your LiveMind AI dashboard
    </div>

    <div class="sub">
        Manage live sessions, creator requirements
        and account activity from one place.
    </div>

</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# ACCOUNT OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">Account Overview</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


# ---------------------------------------------------------
# BALANCE
# ---------------------------------------------------------

with col1:

    st.markdown(
        f"""
<div class="card">

    <div class="label">
        ACCOUNT BALANCE
    </div>

    <div class="value green">
        ${BALANCE:,.2f}
    </div>

    <div class="small">
        Sample account figure
    </div>

</div>
""",
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# STATUS
# ---------------------------------------------------------

with col2:

    st.markdown(
        """
<div class="card">

    <div class="label">
        FUNDS STATUS
    </div>

    <div class="value orange">
        LOCKED
    </div>

    <div class="small">
        Pending creator requirements
    </div>

</div>
""",
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# STREAMS
# ---------------------------------------------------------

with col3:

    st.markdown(
        f"""
<div class="card">

    <div class="label">
        LIVE SESSIONS
    </div>

    <div class="value blue">
        {COMPLETED_STREAMS} / {REQUIRED_STREAMS}
    </div>

    <div class="small">
        Required sessions
    </div>

</div>
""",
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# TIME
# ---------------------------------------------------------

with col4:

    st.markdown(
        f"""
<div class="card">

    <div class="label">
        TIME WINDOW
    </div>

    <div class="value purple">
        {DAYS_LEFT} DAYS
    </div>

    <div class="small">
        Remaining window
    </div>

</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# REQUIREMENT
# =========================================================

st.markdown(
    '<div class="section-title">Account Requirement</div>',
    unsafe_allow_html=True
)


st.markdown(
    f"""
<div class="notice">

    <div class="notice-title">
        Complete {REQUIRED_STREAMS}
        live sessions within {DAYS_LEFT} days
    </div>

    <div class="notice-text">

        The account workflow shown here requires
        two live sessions during the stated period.

        Each session can be private and does not
        require a public audience.

        Minimum support activity shown for each
        session:
        <b>${MIN_SUPPORT:.2f}</b>.

    </div>

</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# PROGRESS
# =========================================================

progress = (
    COMPLETED_STREAMS /
    REQUIRED_STREAMS
)


st.progress(
    progress,
    text=(
        f"Requirement progress — "
        f"{COMPLETED_STREAMS} of "
        f"{REQUIRED_STREAMS} sessions completed"
    )
)


# =========================================================
# MAIN CONTENT
# =========================================================

left_col, right_col = st.columns(
    [1.45, 1],
    gap="large"
)


# =========================================================
# LIVE CENTER
# =========================================================

with left_col:

    st.markdown(
        '<div class="section-title">'
        'Live Session Center'
        '</div>',
        unsafe_allow_html=True
    )

    session1, session2 = st.columns(2)


    # -----------------------------------------------------
    # SESSION 1
    # -----------------------------------------------------

    with session1:

        st.markdown(
            """
<div class="stream-card">

    <div class="label">
        SESSION 01
    </div>

    <div style="
        font-size:20px;
        font-weight:750;
        color:#ffffff;
    ">
        🔴 Private Live
    </div>

    <div class="small">
        No public audience required.
    </div>

</div>
""",
            unsafe_allow_html=True
        )

        if st.button(
            "🎥 Start Private Live",
            key="start_live",
            use_container_width=True
        ):

            st.info(
                "Prototype action: connect this button "
                "to your real live-stream provider."
            )


    # -----------------------------------------------------
    # SESSION 2
    # -----------------------------------------------------

    with session2:

        st.markdown(
            """
<div class="stream-card">

    <div class="label">
        SESSION 02
    </div>

    <div style="
        font-size:20px;
        font-weight:750;
        color:#ffffff;
    ">
        📅 Private Live
    </div>

    <div class="small">
        No public audience required.
    </div>

</div>
""",
            unsafe_allow_html=True
        )

        if st.button(
            "📅 Schedule Session",
            key="schedule_live",
            use_container_width=True
        ):

            st.info(
                "Prototype action: connect this button "
                "to your scheduling backend."
            )


# =========================================================
# ACTIVITY
# =========================================================

with right_col:

    st.markdown(
        '<div class="section-title">'
        'Activity'
        '</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
<div class="card">

    <div class="label">
        CURRENT STATUS
    </div>

    <div style="
        font-size:21px;
        font-weight:750;
        color:#ffffff;
    ">
        Requirements pending
    </div>

    <div class="small">

        Complete the displayed live-session
        requirements to update the account workflow.

    </div>

    <hr style="
        border-color:
        rgba(145,160,210,.10);
        margin:18px 0;
    ">

    <div class="label">
        SUPPORT THRESHOLD
    </div>

    <div style="
        font-size:24px;
        font-weight:800;
        color:#ffffff;
    ">
        ${MIN_SUPPORT:.2f}
    </div>

    <div class="small">
        Minimum per session
    </div>

</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
<div class="footer">

    LiveMind AI · Creator Dashboard Prototype

    <br><br>

    Sample financial figures are for
    interface testing only.

</div>
""",
    unsafe_allow_html=True
)
