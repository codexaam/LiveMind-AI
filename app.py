import streamlit as st

st.set_page_config(
    page_title="LiveMind AI",
    page_icon="🎥",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #070912;
    color: white;
}

.title {
    font-size: 42px;
    font-weight: 800;
}

.blue {
    color: #38bdf8;
}

.card {
    background: linear-gradient(145deg, #171b32, #0b0e1d);
    border: 1px solid #252d4d;
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 15px;
}

.label {
    color: #8996b7;
    font-size: 13px;
}

.number {
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="title">LiveMind <span class="blue">AI</span></div>',
    unsafe_allow_html=True
)

st.caption("Smart Live Streaming & Creator Dashboard")

st.divider()

st.subheader("Account Overview")


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="label">ACCOUNT BALANCE</div>', unsafe_allow_html=True)
    st.markdown('<div class="number">$402,580.00</div>', unsafe_allow_html=True)
    st.caption("Sample account figure")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="label">FUNDS STATUS</div>', unsafe_allow_html=True)
    st.markdown('<div class="number">LOCKED</div>', unsafe_allow_html=True)
    st.caption("Pending requirements")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="label">LIVE SESSIONS</div>', unsafe_allow_html=True)
    st.markdown('<div class="number">0 / 2</div>', unsafe_allow_html=True)
    st.caption("Required sessions")
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="label">TIME WINDOW</div>', unsafe_allow_html=True)
    st.markdown('<div class="number">30 DAYS</div>', unsafe_allow_html=True)
    st.caption("Remaining window")
    st.markdown('</div>', unsafe_allow_html=True)


st.subheader("Account Requirement")

st.info(
    "Complete 2 live sessions within 30 days. "
    "Private sessions are supported. "
    "Minimum support activity: $5 per session."
)

st.progress(
    0,
    text="Requirement progress — 0 of 2 sessions completed"
)

st.subheader("Live Session Center")

a, b = st.columns(2)

with a:
    st.markdown("### 🔴 Session 01")
    st.write("Private Live")
    st.caption("No public audience required.")

    if st.button("🎥 Start Private Live", use_container_width=True):
        st.info("Prototype action.")

with b:
    st.markdown("### 📅 Session 02")
    st.write("Private Live")
    st.caption("No public audience required.")

    if st.button("📅 Schedule Session", use_container_width=True):
        st.info("Prototype action.")


st.divider()

st.caption(
    "LiveMind AI · Prototype interface · Sample financial figures"
)
