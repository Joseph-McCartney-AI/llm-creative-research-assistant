# LLM-Powered Research Assistant for Creative Industries

This is a custom GPT-4-powered assistant that helps professionals in media, arts, broadcast, and culture explore how Artificial Intelligence can inspire real-world innovation.

**Built by Joseph McCartney – Created as part of my application for an AI apprenticeship**

---

## What It Does

Users enter a topic (e.g. "AI in museums", "independent cinema", "immersive digital theatre") and the assistant:

1. Summarizes relevant trends and AI innovations in that space  
2. Suggests one or two creative project ideas tailored for organisations like museums, studios, or festivals  
3. Outputs an easy-to-read insight and idea summary

This tool blends creative thinking, AI prompt engineering, and practical application for the industries Peak Signal works with.

---

## Example Use Case

**Topic entered:** `AI in classical music performance`  

**Output:**
- Summary of how orchestras are using generative music, real-time visualisation, and AI-enhanced audience experiences  
- Creative idea: "Conductor Companion" – an AI assistant that adapts live music interpretation and engages audience members through mobile prompts

---

## Tech Stack

- Python  
- OpenAI GPT-4  
- Streamlit  
- Prompt templating  

---

## Project Structure

```
llm-creative-research-assistant/
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── prompts/
│   └── idea_prompt.txt  # Custom LLM prompt template
└── README.md            # This file
```

---

## How to Run It Locally

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/llm-creative-research-assistant.git
cd llm-creative-research-assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

You’ll need an OpenAI API key. Add this line at the top of `app.py`:
```python
openai.api_key = "your_openai_api_key_here"
```

---

## Why I Built This

This project is designed to address a real-world challenge:  
**How can creative organisations explore and apply AI in ways that are meaningful and useful?**

It demonstrates:
- My ability to apply AI tools to solve real problems  
- Understanding of GPT-based systems  
- Clear thinking and initiative  
- A focus on real-world use cases in creative sectors  

---

## Contact

Joseph McCartney  
📧 mccartneyjoseph580@gmail.com
