import streamlit as st
from PIL import Image
import pyttsx3

# ---------- TEXT TO SPEECH SETUP ----------
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------- APP CONFIG ----------
st.set_page_config(
    page_title="Human Health Hub",
    page_icon="🩺",
    layout="centered"
)

# ---------- DISCLAIMER ----------
st.warning(
    "⚠️ This app is for education & awareness only. "
    "It does NOT replace doctor advice."
)

# ---------- TITLE ----------
st.title("🩺 HUMAN HEALTH HUB")
st.subheader("Easy Health Help • Read & Listen")

# ---------- SIDEBAR ----------
menu = st.sidebar.radio(
    "Choose Option",
    ["Home", "Health Doubts", "Student Health", "Mental Support", "Camera Check"]
)

# ---------- HOME ----------
if menu == "Home":
    st.header("🏠 Welcome")

    text = (
        "This app helps students and people understand health easily. "
        "You can read or listen. This app is useful for everyone."
    )

    st.write(text)

    if st.button("🔊 Listen"):
        speak(text)

# ---------- HEALTH DOUBTS ----------
elif menu == "Health Doubts":
    st.header("🩺 Health Doubts")

    problem = st.selectbox(
        "Choose problem",
        ["Fever", "Headache", "Cold", "Body Pain", "Eye Problem"]
    )

    answers = {
        "Fever": "Fever means body temperature is high. Drink water and take rest.",
        "Headache": "Headache can happen due to stress or less sleep.",
        "Cold": "Cold happens due to virus or dust allergy.",
        "Body Pain": "Body pain happens due to tiredness or fever.",
        "Eye Problem": "Eye redness can be due to dust or infection."
    }

    st.success(answers[problem])

    if st.button("🔊 Read Aloud"):
        speak(answers[problem])

    st.info("If problem continues, please consult a doctor.")

# ---------- STUDENT HEALTH ----------
elif menu == "Student Health":
    st.header("🎓 Student Health Help")

    tips = (
        "Sleep well. Eat healthy food. "
        "Drink enough water. Exercise daily."
    )

    st.write(tips)

    if st.button("🔊 Listen"):
        speak(tips)

# ---------- MENTAL SUPPORT ----------
elif menu == "Mental Support":
    st.header("🧠 Mental Support")

    mood = st.selectbox(
        "How do you feel?",
        ["Happy", "Sad", "Stress", "Tired"]
    )

    support = {
        "Happy": "Good. Keep smiling and stay positive.",
        "Sad": "It is okay to feel sad. Talk to someone you trust.",
        "Stress": "Take deep breath. Relax your mind.",
        "Tired": "Rest well. Sleep is important for health."
    }

    st.success(support[mood])

    if st.button("🔊 Listen"):
        speak(support[mood])

# ---------- CAMERA CHECK ----------
elif menu == "Camera Check":
    st.header("📷 Camera Awareness")

    image = st.camera_input("Take photo (skin or eye only)")

    if image:
        img = Image.open(image)
        st.image(img, caption="Captured Image")

        cam_text = (
            "Redness may mean irritation. "
            "Swelling may mean inflammation. "
            "This is not a medical diagnosis."
        )

        st.info(cam_text)

        if st.button("🔊 Listen"):
            speak(cam_text)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Human Health Hub | Single File App | Voice Enabled")
