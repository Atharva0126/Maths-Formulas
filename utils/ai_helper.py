from openai import OpenAI
import streamlit as st

client = OpenAI(
api_key=st.secrets["OPENAI_API_KEY"]
)

def ask_ai(question):

```
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role":"system",
            "content":"""
            You are a Mathematics Tutor.

            Explain:
            - Simple language
            - Maximum 100 words
            - Give one example
            - Student friendly
            """
        },
        {
            "role":"user",
            "content":question
        }
    ]
)

return response.choices[0].message.content
```

