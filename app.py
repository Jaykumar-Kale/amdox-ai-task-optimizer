import streamlit as st
import pickle

st.set_page_config(page_title="Amdox AI Task Optimizer")

# Load model
model, vectorizer = pickle.load(open("model/emotion_model.pkl", "rb"))

st.title("Amdox AI-Powered Task Optimizer")

text = st.text_area("Enter employee message:")

task_map = {
    "happy": "Assign creative or leadership tasks",
    "calm": "Assign planning or analytical work",
    "sad": "Assign light tasks or team discussions",
    "stress": "Suggest break or reduce workload",
    "angry": "Assign solo tasks and cooldown time"
}

if st.button("Analyze"):
    vec = vectorizer.transform([text])
    emotion = model.predict(vec)[0]

    st.subheader(f"Detected Emotion: {emotion.upper()}")
    st.success(f"Recommended Action: {task_map[emotion]}")

    if emotion == "stress":
        st.warning("⚠️ HR Alert: Employee may need support")
