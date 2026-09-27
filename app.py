import streamlit as st

st.set_page_config(
    page_title="حالة الحساب",
    page_icon="🔒",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 50% 15%, #202938 0%, #0c1018 45%, #05070b 100%);
    color: white;
}

.block-container {
    max-width: 650px;
    padding-top: 12vh;
}

.account-card {
    background: rgba(20, 26, 38, 0.95);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 26px;
    padding: 50px 30px;
    text-align: center;
    box-shadow:
        0 25px 80px rgba(0,0,0,0.55),
        inset 0 1px 0 rgba(255,255,255,0.04);
}

.lock-circle {
    width: 95px;
    height: 95px;
    margin: 0 auto 28px auto;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(145deg, #263246, #111722);
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow:
        0 0 0 8px rgba(255,255,255,0.025),
        0 0 40px rgba(100,150,255,0.12);
}

.lock {
    font-size: 42px;
}

.title {
    font-size: 28px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 18px;
}

.message {
    font-size: 18px;
    line-height: 2;
    color: #c8ced9;
    margin-bottom: 28px;
}

.message strong {
    color: #ffffff;
}

.status {
    display: inline-block;
    padding: 8px 20px;
    border-radius: 30px;
    background: rgba(255, 190, 50, 0.10);
    border: 1px solid rgba(255, 190, 50, 0.22);
    color: #ffc857;
    font-size: 14px;
    font-weight: 700;
}

.footer {
    text-align: center;
    color: #687181;
    font-size: 12px;
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)


# اسم صاحب الحساب
OWNER_NAME = "صاحب الحساب"


st.markdown(
    f"""
    <div class="account-card" dir="rtl">

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

    <div class="footer" dir="rtl">
        حالة الحساب • تم تحديثها مؤخرًا
    </div>
    """,
    unsafe_allow_html=True
)
