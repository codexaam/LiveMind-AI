import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="حالة الحساب",
    page_icon="🔒",
    layout="centered"
)

OWNER_NAME = "صاحب الحساب"

html = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">

<style>

* {{
    box-sizing: border-box;
}}

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100vh;
}}

body {{
    background:
        radial-gradient(
            circle at 50% 10%,
            #1b2940 0%,
            #090f1b 45%,
            #030509 100%
        );

    font-family: Arial, Tahoma, sans-serif;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 25px;
}}

.container {{
    width: 100%;
    max-width: 620px;
}}

.card {{
    background:
        linear-gradient(
            145deg,
            #1c2534,
            #0c111b
        );

    border: 1px solid rgba(255,255,255,0.09);

    border-radius: 28px;

    padding: 55px 28px;

    text-align: center;

    box-shadow:
        0 25px 70px rgba(0,0,0,0.65),
        inset 0 1px 1px rgba(255,255,255,0.05);
}}

.lock {{
    width: 100px;
    height: 100px;

    margin: 0 auto 28px;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #141e2d;

    border: 1px solid rgba(255,255,255,0.12);

    box-shadow:
        0 0 0 9px rgba(255,255,255,0.025),
        0 0 35px rgba(90,130,190,0.15);

    font-size: 43px;
}}

.title {{
    color: white;

    font-size: 28px;

    font-weight: 700;

    margin-bottom: 20px;
}}

.message {{
    color: #c9d0db;

    font-size: 18px;

    line-height: 2;

    margin-bottom: 28px;
}}

.name {{
    color: white;
    font-weight: 700;
}}

.status {{
    display: inline-block;

    color: #ffc857;

    background: rgba(255,193,7,0.08);

    border: 1px solid rgba(255,193,7,0.22);

    border-radius: 50px;

    padding: 9px 20px;

    font-size: 14px;

    font-weight: 600;
}}

.footer {{
    text-align: center;

    color: #6c7686;

    font-size: 12px;

    margin-top: 22px;
}}

@media (max-width: 500px) {{

    body {{
        padding: 15px;
    }}

    .card {{
        padding: 45px 20px;
        border-radius: 24px;
    }}

    .lock {{
        width: 88px;
        height: 88px;
        font-size: 38px;
    }}

    .title {{
        font-size: 24px;
    }}

    .message {{
        font-size: 16px;
    }}
}}

</style>
</head>

<body>

<div class="container">

    <div class="card">

        <div class="lock">
            🔒
        </div>

        <div class="title">
            تم إغلاق الحساب مؤقتًا
        </div>

        <div class="message">
            قام
            <span class="name">{OWNER_NAME}</span>
            بإغلاق حسابه مؤقتًا.
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

</div>

</body>
</html>
"""

components.html(
    html,
    height=650,
    scrolling=False
)
