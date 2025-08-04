import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🎨 LLM Creative Research Assistant")
topic = st.text_input("Enter a creative topic or research question:")
submit = st.button("Generate Insights")

if submit and topic:
    with open("prompts/idea_prompt.txt", "r") as file:
        prompt_template = file.read()

    full_prompt = prompt_template.replace("<<TOPIC>>", topic)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": full_prompt}],
            max_tokens=700
        )
        result = response.choices[0].message.content
        st.markdown("### ✨ AI-Powered Insight and Idea")
        st.write(result)
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")