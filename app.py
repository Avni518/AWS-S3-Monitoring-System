import streamlit as st
import requests
from streamlit_js_eval import streamlit_js_eval
import json

# ===========================
# 🔗 YOUR API URL
# ===========================
API_URL = "https://9t149jcte1.execute-api.ap-south-1.amazonaws.com/login"

# ===========================
# 🎨 PAGE SETTINGS
# ===========================
st.set_page_config(page_title="AWS Dashboard", layout="wide")

st.title("☁ AWS Security + Attendance Dashboard")
st.write("Login + Location + OTP + S3 Monitoring")

# ===========================
# 📌 TABS
# ===========================
tab1, tab2 = st.tabs(["🔐 Login System", "🛡 S3 Monitoring"])

# ==========================================================
# 🔐 TAB 1: LOGIN SYSTEM (NO CHANGE)
# ==========================================================
with tab1:

    st.subheader("🔐 Student Login")

    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")

    # 📍 AUTO LOCATION
    coords = streamlit_js_eval(js_expressions="""
        new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    resolve({
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude
                    });
                },
                (error) => {
                    resolve(null);
                }
            );
        });
    """)

    if coords:
        latitude = coords["latitude"]
        longitude = coords["longitude"]
        st.success("📍 Location detected")
        st.write(f"Lat: {latitude}")
        st.write(f"Lon: {longitude}")
    else:
        st.warning("⚠ Allow location access in browser")
        latitude = None
        longitude = None

    # 🔑 OTP
    otp = st.text_input("OTP (if received)")

    # 🔘 LOGIN BUTTON
    if st.button("Login"):

        if not user_id or not password:
            st.error("Enter User ID & Password")

        elif latitude is None:
            st.error("Location not detected")

        else:
            try:
                payload = {
                    "user_id": user_id,
                    "password": password,
                    "latitude": str(latitude),
                    "longitude": str(longitude),
                    "otp": otp if otp else None
                }

                response = requests.post(API_URL, json=payload)
                result = response.json()

                st.success("Response:")
                st.json(result)

            except Exception as e:
                st.error(f"Error: {str(e)}")


# ==========================================================
# 🛡 TAB 2: S3 MONITORING (UPDATED)
# ==========================================================
with tab2:

    st.subheader("📁 Upload AWS S3 Log File")

    uploaded_file = st.file_uploader(
        "Upload log file",
        type=["txt", "log", "json"]  # ✅ supports JSON now
    )

    if uploaded_file:

        file_name = uploaded_file.name

        # ==================================================
        # 📄 JSON FILE HANDLING (FROM LAMBDA)
        # ==================================================
        if file_name.endswith(".json"):

            content = uploaded_file.read().decode("utf-8")
            data = json.loads(content)

            st.subheader("📜 JSON Log Data")
            st.json(data)

            status = data.get("status", "")

            total = 1
            success = 1 if status == "Access granted" else 0
            denied = 0 if status == "Access granted" else 1

        # ==================================================
        # 📄 TXT / LOG FILE HANDLING (S3 ACCESS LOGS)
        # ==================================================
        else:

            content = uploaded_file.read().decode("utf-8")
            lines = content.split("\n")

            total = len(lines)
            success = sum(1 for l in lines if "200" in l)
            denied = sum(1 for l in lines if "403" in l)

            st.subheader("📜 Log Preview")
            st.text(content[:1500])

        # ==================================================
        # 📊 METRICS
        # ==================================================
        col1, col2, col3 = st.columns(3)

        col1.metric("Total Requests", total)
        col2.metric("Success", success)
        col3.metric("Denied", denied)

        # ==================================================
        # 🚨 SUSPICIOUS DETECTION
        # ==================================================
        if denied > 0:
            st.error("⚠ Suspicious Activity Detected!")
        else:
            st.success("✅ No suspicious activity")