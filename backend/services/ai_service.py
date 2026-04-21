from openai import OpenAI
import json
# from prompts import PSYCHOMETRIC_PROMPT
# from config import api_key
import os
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=os.getenv("GROQ_BASE_URL")
)

PSYCHOMETRIC_PROMPT = """
Generate 18 psychometric questions for students.

Requirements:
- Cover all RIASEC categories:
  realistic, investigative, artistic, social, enterprising, conventional
- Each question must include:
  id, question, type

Return STRICT JSON only:
[
  {
    "id": 1,
    "question": "...",
    "type": "realistic"
  }
]
"""

def generate_psychometric_questions():
    response = llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role":"user","content":PSYCHOMETRIC_PROMPT}]
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return []

# print(generate_psychometric_questions())