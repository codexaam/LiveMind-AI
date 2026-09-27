import streamlit as st # ========================= # Page Configuration # ========================= st.set_page_config( page_title="حالة الحساب", page_icon="🔒", layout="centered" ) # ========================= # Custom CSS # ========================= st.markdown(""" <style> @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap'); html, body, [class*="css"] { font-family: 'Cairo', sans-serif; } .stApp { background: radial-gradient(circle at 50% 20%, #1d2635 0%, #0b0f16 45%, #05070b 100%); color: white; } .block-container { max-width: 650px; padding-top: 12vh; } /* Main Card */ .account-card { background: rgba(18, 24, 35, 0.92); border: 1px solid rgba(255,255,255,0.08); border-radius: 25px; padding: 50px 35px; text-align: center; box-shadow: 0 25px 80px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.04); } /* Lock Circle */ .lock-circle { width: 92px; height: 92px; margin: 0 auto 28px auto; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: linear-gradient( 145deg, #202b3d, #111722 ); border: 1px solid rgba(255,255,255,0.10); box-shadow: 0 0 0 8px rgba(255,255,255,0.025), 0 0 40px rgba(100,150,255,0.12); } .lock { font-size: 43px; } /* Title */ .title { font-size: 28px; font-weight: 800; margin-bottom: 15px; color: #ffffff; } /* Message */ .message { font-size: 18px; line-height: 2; color: #c7ced9; margin-bottom: 25px; } /* Status */ .status { display: inline-block; padding: 8px 18px; border-radius: 30px; background: rgba(255, 180, 0, 0.10); border: 1px solid rgba(255, 180, 0, 0.20); color: #ffc857; font-size: 14px; font-weight: 700; } /* Footer */ .footer { text-align: center; color: #6f7887; font-size: 13px; margin-top: 25px; } </style> """, unsafe_allow_html=True) # ========================= # Account Information # ========================= OWNER_NAME = "صاحب الحساب" # ========================= # Main UI # ========================= st.markdown(f""" <div class="account-card"> <div class="lock-circle"> <div class="lock">🔒</div> </div> <div class="title"> تم إغلاق الحساب مؤقتًا </div> <div class="message"> قام <strong>{OWNER_NAME}</strong> بإغلاق حسابه مؤقتًا. <br> لا يمكن الوصول إلى محتوى الحساب في الوقت الحالي. </div> <div class="status"> الحساب غير متاح مؤقتًا </div> </div> <div class="footer"> حالة الحساب • تم تحديثها مؤخرًا </div> """, unsafe_allow_html=True) على GitHub 

اعمل Repository جديد، وحط فيه ملف واحد باسم:

app.py 

وبعدين في Streamlit اختار الـRepository والملف app.py.

ولو عايز تغير الاسم، عدّل السطر:

OWNER_NAME = "صاحب الحساب" 

مثلاً:

OWNER_NAME = "Ayman Mansour" 

فيظهر:

قام Ayman Mansour بإغلاق حسابه مؤقتًا.

