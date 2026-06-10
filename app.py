import streamlit as st
from formulas.anova import show_anova
from utils.ai_helper import ask_ai

st.set_page_config(
page_title="Maths Formulas",
page_icon="📚",
layout="wide"
)

# Load CSS

with open("assets/style.css") as f:
st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1>📚 Maths Formulas</h1>", unsafe_allow_html=True)
st.markdown("### Learn • Practice • Understand")

topic = st.sidebar.selectbox(
"Select Topic",
[
"ANOVA",
"Regression (Coming Soon)",
"Probability (Coming Soon)"
]
)

if topic == "ANOVA":
show_anova()

st.divider()

st.subheader("✨ Ask AI")

question = st.text_input(
"Ask any question related to the selected topic"
)

if st.button("Get Explanation"):
if question:
response = ask_ai(question)
st.success(response)

