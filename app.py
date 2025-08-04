import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="LLM Creative Research Assistant", layout="centered")
st.title("🎨 LLM Creative Research Assistant")
st.write("Explore creative AI ideas tailored for arts, media, and cultural innovation.")

topic = st.text_input("Enter a creative topic or research question:")
submit = st.button("Generate Insights")

if submit and topic:
    try:
        with open("prompts/idea_prompt.txt", "r", encoding="utf-8") as file:
            prompt_template = file.read()

        full_prompt = prompt_template.replace("<<TOPIC>>", topic.strip())

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": full_prompt}],
            max_tokens=700,
            temperature=0.8
        )

        result = response.choices[0].message.content
        st.markdown("### ✨ AI-Powered Insight and Idea")
        st.markdown(result)

    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
