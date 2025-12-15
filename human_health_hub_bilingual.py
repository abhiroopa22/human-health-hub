import streamlit as st
from PIL import Image

# ---------- APP CONFIG ----------
st.set_page_config(
    page_title="Human Health Hub",
    page_icon="🩺",
    layout="centered"
)

# ---------- BROWSER VOICE FUNCTION ----------
def speak(text, lang='en-US'):
    text = text.replace('"', '\\"')  # Escape quotes
    js = f"""
    <script>
    var msg = new SpeechSynthesisUtterance("{text}");
    msg.lang = '{lang}';
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js)

# ---------- LANGUAGE SELECTION ----------
language = st.sidebar.selectbox("Select Language / மொழி தேர்வு செய்யவும்", ["English", "தமிழ்"])

# ---------- TEXT DICTIONARIES ----------
text_dict = {
    "English": {
        "home_title": "🏠 Welcome",
        "home_text": "This app helps students and people understand health easily. You can read or listen. Useful for everyone.",
        "health_title": "🩺 Health Doubts",
        "health_problems": ["Fever", "Headache", "Cold", "Body Pain", "Eye Problem"],
        "health_answers": {
            "Fever": "Fever means body temperature is high. Drink water and take rest.",
            "Headache": "Headache can happen due to stress or less sleep.",
            "Cold": "Cold happens due to virus or dust allergy.",
            "Body Pain": "Body pain happens due to tiredness or fever.",
            "Eye Problem": "Eye redness can be due to dust or infection."
        },
        "student_title": "🎓 Student Health Help",
        "student_tips": "Sleep well. Eat healthy food. Drink enough water. Exercise daily.",
        "mental_title": "🧠 Mental Support",
        "mental_moods": ["Happy", "Sad", "Stress", "Tired"],
        "mental_support": {
            "Happy": "Good. Keep smiling and stay positive.",
            "Sad": "It is okay to feel sad. Talk to someone you trust.",
            "Stress": "Take deep breath. Relax your mind.",
            "Tired": "Rest well. Sleep is important for health."
        },
        "camera_title": "📷 Camera Awareness",
        "camera_text": "Redness may mean irritation. Swelling may mean inflammation. This is not a medical diagnosis.",
        "listen": "🔊 Listen",
        "info": "If problem continues, please consult a doctor."
    },
    "தமிழ்": {
        "home_title": "🏠 வரவேற்பு",
        "home_text": "இந்த பயன்பாடு மாணவர்களுக்கும் மக்களுக்கும் சுகாதாரத்தை எளிதாக புரிந்து கொள்ள உதவுகிறது. நீங்கள் வாசிக்கவும் கேட்கவும் முடியும். அனைவருக்கும் பயன்படும்.",
        "health_title": "🩺 சுகாதார சந்தேகம்",
        "health_problems": ["காய்ச்சல்", "தலைவலி", "சளி", "உடல் வலி", "கண் பிரச்சனை"],
        "health_answers": {
            "காய்ச்சல்": "காய்ச்சல் என்பது உடலின் வெப்பநிலை அதிகரிப்பாகும். தண்ணீர் குடித்து ஓய்வெடுக்கவும்.",
            "தலைவலி": "தலைவலி மன அழுத்தம் அல்லது தூக்கம் குறைவினால் ஏற்படலாம்.",
            "சளி": "சளி வைரஸ் அல்லது தூசி அலெர்ஜியால் ஏற்படும்.",
            "உடல் வலி": "உடல் வலி சோர்வு அல்லது காய்ச்சலால் ஏற்படும்.",
            "கண் பிரச்சனை": "கண்களில் சிவப்பு தூசி அல்லது தொற்று காரணமாக ஏற்படலாம்."
        },
        "student_title": "🎓 மாணவர் சுகாதார உதவி",
        "student_tips": "நன்றாக உறங்குங்கள். ஆரோக்கிய உணவு உண்ணுங்கள். போதுமான தண்ணீர் குடிக்கவும். தினமும் பயிற்சி செய்யவும்.",
        "mental_title": "🧠 மனநலம்",
        "mental_moods": ["மகிழ்ச்சி", "சோகம்", "மனஅழுத்தம்", "சோர்வு"],
        "mental_support": {
            "மகிழ்ச்சி": "நன்றாக உள்ளது! சிரித்து முன்னேறுங்கள்.",
            "சோகம்": "சோகம் இருப்பது இயல்பானது. நம்பிக்கையுள்ள ஒருவரிடம் பேசுங்கள்.",
            "மனஅழுத்தம்": "ஆழமாக சுவாசியுங்கள். மனதை அமைதியாக்குங்கள்.",
            "சோர்வு": "நன்றாக ஓய்வெடுக்கவும். தூக்கம் முக்கியம்."
        },
        "camera_title": "📷 கேமரா கவனம்",
        "camera_text": "சிவப்பு என்பது குறிப்பு: இடர்பாடாக இருக்கலாம். வளர்ச்சி வீக்கம் இருந்தால் கவனம் தேவை. இது மருத்துவ பரிசோதனை அல்ல.",
        "listen": "🔊 கேளுங்கள்",
        "info": "சிக்கல் நீடித்தால், மருத்துவரை அணுகவும்."
    }
}

lang_data = text_dict[language]
voice_lang = 'ta-IN' if language == "தமிழ்" else 'en-US'

# ---------- SIDEBAR MENU ----------
menu = st.sidebar.radio(
    "Choose Service / சேவை தேர்வு செய்யவும்",
    ["Home / முகப்பு", "Health Doubts / சுகாதார சந்தேகம்", "Student Health / மாணவர் சுகாதாரம்",
     "Mental Support / மனநலம்", "Camera / கேமரா"]
)

# ---------- HOME ----------
if "Home" in menu or "முகப்பு" in menu:
    st.header(lang_data["home_title"])
    st.write(lang_data["home_text"])
    if st.button(lang_data["listen"]):
        speak(lang_data["home_text"], lang=voice_lang)

# ---------- HEALTH DOUBTS ----------
elif "Health Doubts" in menu or "சுகாதார சந்தேகம்" in menu:
    st.header(lang_data["health_title"])
    problem = st.selectbox("Select Problem / சிக்கலை தேர்வு செய்யவும்", lang_data["health_problems"])
    st.success(lang_data["health_answers"][problem])
    if st.button(lang_data["listen"]):
        speak(lang_data["health_answers"][problem], lang=voice_lang)
    st.info(lang_data["info"])

# ---------- STUDENT HEALTH ----------
elif "Student Health" in menu or "மாணவர் சுகாதாரம்" in menu:
    st.header(lang_data["student_title"])
    st.write(lang_data["student_tips"])
    if st.button(lang_data["listen"]):
        speak(lang_data["student_tips"], lang=voice_lang)

# ---------- MENTAL SUPPORT ----------
elif "Mental Support" in menu or "மனநலம்" in menu:
    st.header(lang_data["mental_title"])
    mood = st.selectbox("Select Mood / உங்கள் மனநிலை எப்படி உள்ளது?", lang_data["mental_moods"])
    st.success(lang_data["mental_support"][mood])
    if st.button(lang_data["listen"]):
        speak(lang_data["mental_support"][mood], lang=voice_lang)

# ---------- CAMERA CHECK ----------
elif "Camera" in menu or "கேமரா" in menu:
    st.header(lang_data["camera_title"])
    image = st.camera_input("Take Photo / புகைப்படம் எடுக்கவும்")
    if image:
        img = Image.open(image)
        st.image(img, caption="Captured Image / புகைப்படம் பிடிக்கப்பட்டது")
        st.info(lang_data["camera_text"])
        if st.button(lang_data["listen"]):
            speak(lang_data["camera_text"], lang=voice_lang)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Human Health Hub | Bilingual Voice Enabled | Single File App")
