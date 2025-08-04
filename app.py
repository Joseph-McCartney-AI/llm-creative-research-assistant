import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load your API key from a .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit page config
st.set_page_config(page_title="LLM Creative Research Assistant", page_icon=None)

st.title("LLM Creative Research Assistant")
st.subheader("Discover innovative AI-driven ideas for arts, media, and cultural sectors.")

st.markdown("""
Examples of prompts you can enter:
- How can music festivals use AI to create immersive audience experiences?
- Using AI for museum curation and interpretation
- Creative ways publishers could integrate generative AI tools
- How might galleries explore new forms of digital storytelling with AI?
""")

# Input form
with st.form(key="query_form"):
    user_prompt = st.text_area("Enter a creative topic or research question:", height=150)
    submit_button = st.form_submit_button(label="Generate Ideas")

# Load the system prompt
def load_prompt_template():
    with open("prompts/idea_prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

if submit_button and user_prompt:
    with st.spinner("Generating ideas..."):
        try:
            system_prompt = load_prompt_template().replace("<<TOPIC>>", user_prompt)

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.8,
                max_tokens=800
            )

            result = response['choices'][0]['message']['content']
            st.markdown("### Output")
            st.markdown(result)

        except Exception as e:
            st.error(f"An error occurred: {e}")

