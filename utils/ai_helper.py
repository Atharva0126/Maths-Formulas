from openai import OpenAI
import streamlit as st


def ask_ai(question):

    try:

        client = OpenAI(
            api_key=st.secrets["OPENAI_API_KEY"]
        )

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are a professional Mathematics Tutor.

                    Rules:
                    1. Simple explanation
                    2. Maximum 100 words
                    3. Give one example
                    4. Student friendly
                    """
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"
