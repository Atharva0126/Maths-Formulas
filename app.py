import streamlit as st
import os

from formulas.anova import show_anova
from utils.ai_helper import ask_ai

st.set_page_config(
    page_title="Maths Formulas",
    page_icon="📚",
    layout="wide"
)

# Load CSS
css_file = "assets/style.css"

if os.path.exists(css_file):
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

st.markdown(
    """
    <h1 style='text-align:center'>
        📚 Maths Formulas
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center'>Learn • Practice • Understand</h4>",
    unsafe_allow_html=True
)

st.sidebar.title("Topics")

topic = st.sidebar.selectbox(
    "Select Topic",
    [
        "ANOVA",
        "Regression (Coming Soon)",
        "Probability (Coming Soon)",
        "Statistics (Coming Soon)"
    ]
)

if topic == "ANOVA":
    show_anova()

st.divider()

st.subheader("✨ AI Tutor")

question = st.text_input(
    "Ask any question related to this topic"
)

if st.button("Get Explanation"):

    if question.strip():

        with st.spinner("Generating answer..."):

            answer = ask_ai(question)

            st.success(answer)

    else:
        st.warning("Please enter a question.")
