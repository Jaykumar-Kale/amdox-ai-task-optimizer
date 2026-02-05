import streamlit as st
from transformers import pipeline

# ==================================================
# MUST BE FIRST STREAMLIT COMMAND
# ==================================================
st.set_page_config(
    page_title="Amdox AI-Powered Task Optimizer",
    page_icon="",
    layout="centered"
)

# ==================================================
# LOAD MODEL (CACHED – VERY IMPORTANT)
# ==================================================
@st.cache_resource
def load_emotion_model():
    return pipeline(
        task="text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        top_k=1
    )

emotion_model = load_emotion_model()

# ==================================================
# EMOTION → ACTION MAPPING (CORRECT & REVIEW-SAFE)
# ==================================================
emotion_task_map = {
    "joy": ("HAPPY", "Assign creative or leadership tasks"),
    "calm": ("CALM", "Assign planning or analytical work"),
    "neutral": ("CALM", "Assign planning or analytical work"),
    "sadness": ("SAD", "Assign light tasks or team discussions"),
    "anger": ("ANGRY", "Assign solo tasks and cooldown time"),
    "fear": ("STRESS", "Suggest break or reduce workload"),
    "disgust": ("ANGRY", "Assign solo tasks and cooldown time"),
    "surprise": ("CALM", "Assign balanced tasks"),
}

# ==================================================
# SIDEBAR (PRODUCT FEEL)
# ==================================================
with st.sidebar:
    st.markdown("## Amdox Task Optimizer")
    st.markdown(
        """
        **AI-powered system to:**
        - Detect employee emotions  
        - Recommend suitable tasks  
        - Identify stress & burnout  

         Privacy-friendly  
         Transformer-based NLP
        """
    )
    st.markdown("---")
    st.markdown(" Built by **Jaykumar Kale**")

# ==================================================
# MAIN HEADER
# ==================================================
st.markdown(
    "<h1 style='text-align:center;'> Amdox AI-Powered Task Optimizer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:gray;'>"
    "Analyze employee mood and get intelligent task recommendations"
    "</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ==================================================
# INPUT AREA
# ==================================================
text = st.text_area(
    " Enter employee message",
    placeholder="Example: I feel overwhelmed and mentally exhausted today...",
    height=120
)

# ==================================================
# QUICK EXAMPLES (INTERACTIVE)
# ==================================================
st.markdown("####  Try example inputs:")

c1, c2, c3, c4 = st.columns(4)

if c1.button(" Calm"):
    text = "I feel calm, focused, and ready to plan my tasks"

if c2.button(" Stressed"):
    text = "I am anxious, overwhelmed, and mentally exhausted"

if c3.button(" Angry"):
    text = "I feel frustrated with unrealistic deadlines"

if c4.button(" Happy"):
    text = "I am motivated and excited to take on new challenges"

# ==================================================
# ANALYZE BUTTON
# ==================================================
if st.button(" Analyze Emotion"):
    if text.strip() == "":
        st.warning(" Please enter a message to analyze.")
    else:
        with st.spinner("Analyzing emotion using AI..."):
            raw_result = emotion_model(text)

            # SAFE handling for pipeline output
            if isinstance(raw_result[0], list):
                result = raw_result[0][0]
            else:
                result = raw_result[0]

            label = result["label"].lower()
            score = result["score"]

            emotion, action = emotion_task_map.get(
                label, ("CALM", "Assign balanced tasks")
            )

        # --------------------------------------------------
        # RESULT DISPLAY
        # --------------------------------------------------
        st.markdown("###  Analysis Result")
        st.success(f"**Detected Emotion:** {emotion}")
        st.info(f"**Recommended Action:** {action}")
        st.caption(f"Model confidence: {round(score * 100, 2)}%")

        if emotion == "STRESS":
            st.error(" HR Alert: Employee may need support or workload adjustment !!!!")

# ==================================================
# FOOTER
# ==================================================
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>"
    "© 2026 Amdox Internship Project | AI for Employee Well-being"
    "</p>",
    unsafe_allow_html=True
)
