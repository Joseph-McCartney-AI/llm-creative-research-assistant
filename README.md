# 🎨 LLM Creative Research Assistant

A simple and impressive Streamlit app that uses GPT-4 to generate creative insights and project ideas based on any input topic. Designed to showcase practical use of AI in creative research.

## 🚀 Features
- Clean Streamlit interface
- Uses OpenAI GPT-4
- Secure API key handling with `.env`
- Easily extendable

## 📂 File Structure
```
llm-creative-research-assistant/
├── app.py
├── prompts/
│   └── idea_prompt.txt
├── requirements.txt
├── .env.example
└── README.md
```

## 🛠 Setup

1. Clone this repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your OpenAI API key.
4. Run the app:
   ```
   streamlit run app.py
   ```

## 💡 Example Prompt
> How festivals can use AI to engage audiences

## 📌 Notes
- This project was built for a creative AI apprenticeship application.
- Fully local, no data is sent anywhere except to OpenAI via API.

---

🧠 Built with ❤️ to impress reviewers and show real technical skill in applied AI.