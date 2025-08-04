import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("LLM Creative Research Assistant")

st.markdown("""
Discover how artificial intelligence can unlock bold, practical, and imaginative opportunities across the creative industries.

**Try entering a topic like:**  
- How museums can use AI to reach new audiences  
- The role of generative AI in independent film  
- Immersive theatre and real-time AI interaction  
""")

topic = st.text_input("Enter your creative topic or research question:")
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
        st.markdown("### ✨ AI-Powered Insight and Project Ideas")
        st.write(result)
    except Exception as e:
        st.error(f"❌ An error occurred:\n\n{str(e)}")
