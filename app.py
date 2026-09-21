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
# DATA
# =========================================================

ACCOUNT_ID = "LM-784521"
ACCOUNT_OWNER = "Ayman Mansour"

BALANCE = 402580.00

REQUIRED_STREAMS = 2
COMPLETED_STREAMS = 0

DAYS_LEFT = 30
MIN_SUPPORT = 5.00


# =========================================================
# CSS
# =========================================================

st.markdown(
"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: "Cairo", "Inter", sans-serif;
}

.stApp {

    background:
        radial-gradient(
            circle at 15% 0%,
            rgba(103, 38, 255, 0.28),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 5%,
            rgba(0, 190, 255, 0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 50% 90%,
            rgba(255, 0, 200, 0.10),
            transparent 30%
        ),
        #030713;

    color: #ffffff;
}

.block-container {
    max-width: 1500px;
    padding-top: 25px;
    padding-bottom: 50px;
}


/* =========================================================
   TOP BRAND
========================================================= */

.brand-box {
    padding: 18px 22px;
    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(18, 25, 55, .95),
            rgba(5, 9, 25, .95)
        );

    border: 1px solid rgba(0, 200, 255, .18);

    box-shadow:
        0 0 35px rgba(0, 120, 255, .10);
}

.brand-title {
    font-size: 34px;
    font-weight: 900;
    letter-spacing: -1px;
}

.brand-ai {
    color: #00c8ff;
}

.owner {
    color: #9ba9c9;
    font-size: 14px;
    margin-top: 4px;
}


/* =========================================================
   SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #030816,
            #05091a
        );

    border-right:
        1px solid rgba(0, 200, 255, .12);
}

.sidebar-brand {
    text-align: center;
    padding: 15px 5px 25px;
}

.sidebar-name {
    font-size: 22px;
    font-weight: 900;
}

.sidebar-ai {
    color: #00c8ff;
}

.sidebar-owner {
    color: #8996b7;
    font-size: 12px;
    margin-top: 5px;
}


/* =========================================================
   HERO
========================================================= */

.hero {

    position: relative;

    overflow: hidden;

    border-radius: 28px;

    padding: 38px 35px;

    margin-top: 20px;

    background:
        linear-gradient(
            120deg,
            rgba(8, 19, 49, .98),
            rgba(21, 6, 48, .95)
        );

    border:
        1px solid rgba(104, 66, 255, .30);

    box-shadow:
        0 0 50px rgba(76, 0, 255, .12);
}

.hero:after {

    content: "";

    position: absolute;

    width: 300px;
    height: 300px;

    right: -100px;
    top: -150px;

    background:
        radial-gradient(
            circle,
            rgba(0, 210, 255, .22),
            transparent 70%
        );
}

.hero-small {

    color: #00c8ff;

    font-size: 13px;

    font-weight: 700;

    letter-spacing: 1px;
}

.hero-title {

    font-size: 38px;

    font-weight: 900;

    margin-top: 5px;

    line-height: 1.25;
}

.hero-title span {

    color: #8b5cf6;
}

.hero-text {

    color: #aeb9d2;

    font-size: 15px;

    margin-top: 10px;

    max-width: 750px;
}


/* =========================================================
   OWNER CARD
========================================================= */

.owner-card {

    margin-top: 20px;

    border-radius: 20px;

    padding: 18px 22px;

    background:
        linear-gradient(
            135deg,
            rgba(16, 25, 57, .95),
            rgba(8, 12, 30, .95)
        );

    border:
        1px solid rgba(0, 210, 255, .18);
}

.owner-label {

    color: #7e8cab;

    font-size: 11px;

    letter-spacing: 1px;
}

.owner-name {

    font-size: 23px;

    font-weight: 800;

    color: #ffffff;
}

.account-id {

    color: #00c8ff;

    font-size: 12px;
}


/* =========================================================
   SECTION
========================================================= */

.section-title {

    font-size: 23px;

    font-weight: 800;

    margin-top: 28px;

    margin-bottom: 14px;
}


/* =========================================================
   STAT CARDS
========================================================= */

.stat-card {

    min-height: 170px;

    border-radius: 22px;

    padding: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(15, 23, 50, .97),
            rgba(5, 9, 24, .98)
        );

    border:
        1px solid rgba(112, 130, 190, .17);

    box-shadow:
        0 12px 35px rgba(0, 0, 0, .30);

    transition: .2s;
}

.stat-card:hover {

    transform: translateY(-3px);

    border-color:
        rgba(0, 200, 255, .40);

    box-shadow:
        0 0 30px rgba(0, 150, 255, .13);
}

.stat-icon {

    font-size: 25px;

    margin-bottom: 8px;
}

.stat-label {

    color: #8592b0;

    font-size: 12px;

    font-weight: 600;
}

.stat-value {

    font-family: "Inter", sans-serif;

    font-size: 27px;

    font-weight: 900;

    margin-top: 8px;
}

.green {
    color: #35f59b;
}

.gold {
    color: #ffca4b;
}

.blue {
    color: #29d8ff;
}

.purple {
    color: #bd7cff;
}

.stat-description {

    color: #71809e;

    font-size: 11px;

    margin-top: 6px;
}


/* =========================================================
   REQUIREMENT
========================================================= */

.requirement {

    border-radius: 24px;

    padding: 25px;

    background:
        linear-gradient(
            120deg,
            rgba(50, 19, 110, .65),
            rgba(5, 28, 65, .85)
        );

    border:
        1px solid rgba(120, 75, 255, .30);

    box-shadow:
        0 0 40px rgba(90, 0, 255, .10);
}

.requirement-title {

    font-size: 21px;

    font-weight: 800;
}

.requirement-text {

    color: #adb9d0;

    line-height: 1.8;

    font-size: 14px;

    margin-top: 7px;
}

.highlight {

    color: #00d9ff;

    font-weight: 800;
}


/* =========================================================
   LIVE CARDS
========================================================= */

.live-card {

    border-radius: 24px;

    padding: 25px;

    min-height: 280px;

    background:
        linear-gradient(
            145deg,
            rgba(12, 21, 48, .98),
            rgba(5, 8, 23, .98)
        );

    border:
        1px solid rgba(100, 120, 200, .18);

    box-shadow:
        0 12px 35px rgba(0, 0, 0, .25);
}

.live-number {

    font-size: 12px;

    color: #7685a6;

    letter-spacing: 1px;
}

.live-title {

    font-size: 22px;

    font-weight: 800;

    margin-top: 7px;
}

.live-status {

    display: inline-block;

    margin-top: 10px;

    padding: 5px 11px;

    border-radius: 30px;

    background: rgba(255, 60, 80, .12);

    border:
        1px solid rgba(255, 60, 80, .30);

    color: #ff7180;

    font-size: 11px;
}

.check {

    color: #43f5a0;

    margin-top: 12px;

    font-size: 13px;
}


/* =========================================================
   QUOTE
========================================================= */

.quote {

    margin-top: 25px;

    padding: 28px;

    border-radius: 24px;

    text-align: center;

    background:
        linear-gradient(
            120deg,
            rgba(27, 15, 74, .85),
            rgba(7, 31, 59, .90)
        );

    border:
        1px solid rgba(100, 100, 255, .22);
}

.quote-main {

    font-size: 23px;

    font-weight: 800;
}

.quote-sub {

    color: #8290ad;

    font-size: 13px;

    margin-top: 6px;
}


/* =========================================================
   BUTTONS
========================================================= */

div.stButton > button {

    border-radius: 14px;

    min-height: 48px;

    font-family: "Cairo", sans-serif;

    font-weight: 800;

    border:
        1px solid rgba(0, 200, 255, .25);

    background:
        linear-gradient(
            90deg,
            #6d28d9,
            #2563eb
        );

    color: white;
}

div.stButton > button:hover {

    border-color: #00d9ff;

    box-shadow:
        0 0 25px rgba(0, 200, 255, .25);
}


/* =========================================================
   FOOTER
========================================================= */

.footer {

    text-align: center;

    margin-top: 40px;

    padding-top: 20px;

    border-top:
        1px solid rgba(100, 120, 180, .12);

    color: #63708c;

    font-size: 11px;
}

</style>
""",
unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    logo = Path("Logo.png")

    if logo.exists():

        st.image(
            str(logo),
            use_container_width=True
        )

    else:

        st.markdown(
            """
<div class="sidebar-brand">

    <div class="sidebar-name">
        LiveMind <span class="sidebar-ai">AI</span>
    </div>

</div>
""",
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
<div class="sidebar-owner">

صاحب الحساب

<br>

<b style="color:white;font-size:15px;">
{ACCOUNT_OWNER}
</b>

<br>

<span style="color:#00c8ff;">
{ACCOUNT_ID}
</span>

</div>
""",
        unsafe_allow_html=True,
    )

    st.divider()

    st.button(
        "🏠  الرئيسية",
        use_container_width=True
    )

    st.button(
        "🔴  البث المباشر",
        use_container_width=True
    )

    st.button(
        "💰  الأرباح",
        use_container_width=True
    )

    st.button(
        "🛡️  متطلبات الحساب",
        use_container_width=True
    )

    st.button(
        "⚙️  الإعدادات",
        use_container_width=True
    )

    st.button(
        "❓  مركز المساعدة",
        use_container_width=True
    )

    st.divider()

    st.caption(
        "LiveMind AI"
    )

    st.caption(
        "منصة بث ذكية للمبدعين"
    )


# =========================================================
# BRAND HEADER
# =========================================================

logo = Path("Logo.png")

if logo.exists():

    logo_col, title_col = st.columns(
        [1, 6],
        vertical_alignment="center"
    )

    with logo_col:

        st.image(
            str(logo),
            width=105
        )

    with title_col:

        st.markdown(
            """
<div class="brand-box">

<div class="brand-title">
LiveMind <span class="brand-ai">AI</span>
</div>

<div class="owner">
منصة البث الذكي وصناعة المحتوى
</div>

</div>
""",
            unsafe_allow_html=True,
        )

else:

    st.markdown(
        """
<div class="brand-box">

<div class="brand-title">
LiveMind <span class="brand-ai">AI</span>
</div>

<div class="owner">
منصة البث الذكي وصناعة المحتوى
</div>

</div>
""",
        unsafe_allow_html=True,
    )


# =========================================================
# HERO
# =========================================================

st.markdown(
    f"""
<div class="hero">

<div class="hero-small">
مرحباً بك مجدداً 👋
</div>

<div class="hero-title">
أهلاً بك <span>{ACCOUNT_OWNER}</span>
</div>

<div class="hero-text">
إدارة جلسات البث الخاصة بك، متابعة متطلبات الحساب
وإدارة نشاط المنشئ من لوحة تحكم واحدة.
</div>

</div>
""",
    unsafe_allow_html=True,
)


# =========================================================
# OWNER
# =========================================================

st.markdown(
    f"""
<div class="owner-card">

<div class="owner-label">
صاحب الحساب
</div>

<div class="owner-name">
👤 {ACCOUNT_OWNER}
</div>

<div class="account-id">
رقم الحساب: {ACCOUNT_ID}
</div>

</div>
""",
    unsafe_allow_html=True,
)


# =========================================================
# ACCOUNT OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">نظرة عامة على الحساب</div>',
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.markdown(
        f"""
<div class="stat-card">

<div class="stat-icon">💳</div>

<div class="stat-label">
رصيد الحساب
</div>

<div class="stat-value green">
${BALANCE:,.2f}
</div>

<div class="stat-description">
قيمة تجريبية للحساب
</div>

</div>
""",
        unsafe_allow_html=True,
    )


with c2:

    st.markdown(
        """
<div class="stat-card">

<div class="stat-icon">🔒</div>

<div class="stat-label">
حالة الأموال
</div>

<div class="stat-value gold">
مقفلة
</div>

<div class="stat-description">
بانتظار استيفاء المتطلبات
</div>

</div>
""",
        unsafe_allow_html=True,
    )


with c3:

    st.markdown(
        f"""
<div class="stat-card">

<div class="stat-icon">🎥</div>

<div class="stat-label">
جلسات البث
</div>

<div class="stat-value blue">
{COMPLETED_STREAMS} / {REQUIRED_STREAMS}
</div>

<div class="stat-description">
الجلسات المطلوبة
</div>

</div>
""",
        unsafe_allow_html=True,
    )


with c4:

    st.markdown(
        f"""
<div class="stat-card">

<div class="stat-icon">📅</div>

<div class="stat-label">
المدة المتبقية
</div>

<div class="stat-value purple">
{DAYS_LEFT} يوم
</div>

<div class="stat-description">
من إجمالي الفترة المسموحة
</div>

</div>
""",
        unsafe_allow_html=True,
    )


# =========================================================
# REQUIREMENTS
# =========================================================

st.markdown(
    '<div class="section-title">متطلبات الحساب</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="requirement">

<div class="requirement-title">
🎯 استكمال {REQUIRED_STREAMS} جلسات بث مباشر
</div>

<div class="requirement-text">

يُطلب إجراء جلستي بث مباشر خلال فترة
<b>{DAYS_LEFT} يوم</b>.

يمكن أن تكون الجلسات <span class="highlight">خاصة</span>
ولا تتطلب وجود جمهور عام.

الحد الأدنى لنشاط الدعم لكل جلسة:
<span class="highlight">${MIN_SUPPORT:.2f}</span>.

</div>

</div>
""",
    unsafe_allow_html=True,
)


# =========================================================
# PROGRESS
# =========================================================

progress = COMPLETED_STREAMS / REQUIRED_STREAMS

st.write("")

st.progress(
    progress,
    text=f"التقدم في المتطلبات — {COMPLETED_STREAMS} من {REQUIRED_STREAMS} جلسات مكتملة",
)


# =========================================================
# LIVE CENTER
# =========================================================

st.markdown(
    '<div class="section-title">🔴 مركز جلسات البث المباشر</div>',
    unsafe_allow_html=True,
)

live1, live2 = st.columns(2)


# =========================================================
# SESSION 1
# =========================================================

with live1:

    st.markdown(
        """
<div class="live-card">

<div class="live-number">
الجلسة 01
</div>

<div class="live-title">
🎥 جلسة بث خاصة
</div>

<div class="live-status">
● لم تبدأ
</div>

<br>

<div class="check">
✓ لا تتطلب جمهوراً عاماً
</div>

<div class="check">
✓ مناسبة لاستيفاء المتطلبات
</div>

<div class="check">
✓ الحد الأدنى للدعم: $5.00
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button(
        "📡 بدء البث الآن",
        key="session_1",
        use_container_width=True,
    ):

        st.info(
            "هذه واجهة Prototype. "
            "زر البث يحتاج ربطه بخدمة بث حقيقية."
        )


# =========================================================
# SESSION 2
# =========================================================

with live2:

    st.markdown(
        """
<div class="live-card">

<div class="live-number">
الجلسة 02
</div>

<div class="live-title">
🎥 جلسة بث خاصة
</div>

<div class="live-status">
● لم تبدأ
</div>

<br>

<div class="check">
✓ لا تتطلب جمهوراً عاماً
</div>

<div class="check">
✓ مناسبة لاستيفاء المتطلبات
</div>

<div class="check">
✓ الحد الأدنى للدعم: $5.00
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button(
        "📅 جدولة الجلسة",
        key="session_2",
        use_container_width=True,
    ):

        st.info(
            "هذه واجهة Prototype. "
            "زر الجدولة يحتاج ربطه بنظام حقيقي."
        )


# =========================================================
# EXTRA FEATURES
# =========================================================

st.markdown(
    '<div class="section-title">الخدمات</div>',
    unsafe_allow_html=True,
)

f1, f2, f3 = st.columns(3)


with f1:

    st.markdown(
        """
<div class="stat-card">

<div class="stat-icon">
📈
</div>

<div class="stat-label">
إدارة الأرباح
</div>

<div style="
font-size:17px;
font-weight:800;
margin-top:7px;
">
تابع نشاطك وإحصاءاتك
</div>

</div>
""",
        unsafe_allow_html=True,
    )


with f2:

    st.markdown(
        """
<div class="stat-card">

<div class="stat-icon">
🛡️
</div>

<div class="stat-label">
أمان الحساب
</div>

<div style="
font-size:17px;
font-weight:800;
margin-top:7px;
">
حسابك محمي وآمن
</div>

</div>
""",
        unsafe_allow_html=True,
    )


with f3:

    st.markdown(
        """
<div class="stat-card">

<div class="stat-icon">
⭐
</div>

<div class="stat-label">
دعم المبدعين
</div>

<div style="
font-size:17px;
font-weight:800;
margin-top:7px;
">
دعم على مدار الساعة
</div>

</div>
""",
        unsafe_allow_html=True,
    )


# =========================================================
# QUOTE
# =========================================================

st.markdown(
    """
<div class="quote">

<div class="quote-main">
ابدأ الآن... كل بث هو خطوة أقرب لهدفك 🚀
</div>

<div class="quote-sub">
استمر في الإبداع، اصنع محتواك، وابنِ مستقبلك.
</div>

</div>
""",
    unsafe_allow_html=True,
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    f"""
<div class="footer">

<b style="color:white;">
LiveMind <span style="color:#00c8ff;">AI</span>
</b>

<br>

منصة البث الذكي للمبدعين

<br><br>

صاحب الحساب:
<b style="color:#aeb9d2;">
{ACCOUNT_OWNER}
</b>

<br><br>

Prototype Interface · Sample financial figures

</div>
""",
    unsafe_allow_html=True,
)
