import streamlit as st
import textwrap

st.set_page_config(
    page_title="حالة الحساب",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# CSS
# =========================

css = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

* {
    box-sizing: border-box;
}

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif !important;
}

.stApp {
    background:
        radial-gradient(
            circle at 50% 10%,
            #18243a 0%,
            #080d17 42%,
            #030509 100%
        );
    min-height: 100vh;
}

header {
    visibility: hidden;
}

.block-container {
    max-width: 680px !important;
    padding-top: 80px !important;
    padding-bottom: 40px !important;
}

/* CARD */

.account-card {
    direction: rtl;
    text-align: center;

    background:
        linear-gradient(
            145deg,
            rgba(28, 36, 52, 0.96),
            rgba(10, 14, 22, 0.98)
        );

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 30px;

    padding: 55px 30px;

    box-shadow:
        0 30px 90px rgba(0,0,0,0.65),
        inset 0 1px 1px rgba(255,255,255,0.04);
}

/* LOCK */

.lock-circle {
    width: 105px;
    height: 105px;

    margin: 0 auto 30px auto;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    background:
        radial-gradient(
            circle,
            #26344b 0%,
            #121a28 65%,
            #0b1019 100%
        );

    border: 1px solid rgba(255,255,255,0.10);

    box-shadow:
        0 0 0 10px rgba(255,255,255,0.025),
        0 0 45px rgba(70,120,200,0.16);
}

.lock {
    font-size: 45px;
    line-height: 1;
}

/* TITLE */

.title {
    color: #ffffff;

    font-size: 29px;
    font-weight: 800;

    margin-bottom: 18px;
}

/* MESSAGE */

.message {
    color: #c7ceda;

    font-size: 18px;
    font-weight: 400;

    line-height: 2;

    margin-bottom: 30px;
}

.message strong {
    color: #ffffff;
    font-weight: 800;
}

/* STATUS */

.status {
    display: inline-block;

    color: #ffc857;

    background: rgba(255,190,50,0.08);

    border: 1px solid rgba(255,190,50,0.20);

    border-radius: 50px;

    padding: 9px 22px;

    font-size: 14px;
    font-weight: 700;
}

/* FOOTER */

.footer {
    direction: rtl;

    text-align: center;

    color: #697386;

    font-size: 12px;

    margin-top: 24px;
}

/* MOBILE */

@media (max-width: 600px) {

    .block-container {
        padding-top: 45px !important;
        padding-left: 18px !important;
        padding-right: 18px !important;
    }

    .account-card {
        padding: 45px 20px;
        border-radius: 25px;
    }

    .lock-circle {
        width: 90px;
        height: 90px;
    }

    .lock {
        font-size: 39px;
    }

    .title {
        font-size: 25px;
    }

    .message {
        font-size: 16px;
    }
}

</style>
"""

st.markdown(css, unsafe_allow_html=True)


# =========================
# Account Name
# =========================

OWNER_NAME = "صاحب الحساب"


# =========================
# Main Card
# =========================

html = f"""
<div class="account-card">

    <div class="lock-circle">
        <div class="lock">🔒</div>
    </div>

    <div class="title">
        تم إغلاق الحساب مؤقتًا
    </div>

    <div class="message">
        قام <strong>{OWNER_NAME}</strong> بإغلاق حسابه مؤقتًا.
        <br>
        لا يمكن الوصول إلى محتوى الحساب في الوقت الحالي.
    </div>

    <div class="status">
        الحساب غير متاح مؤقتًا
    </div>

</div>

<div class="footer">
    حالة الحساب • تم تحديثها مؤخرًا
</div>
"""

st.markdown(
    textwrap.dedent(html),
    unsafe_allow_html=True
)
