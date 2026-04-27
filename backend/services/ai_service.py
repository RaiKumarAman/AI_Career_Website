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

# Language templates for prompts
LANGUAGE_INSTRUCTIONS = {
    "English": "Respond ONLY in English. Use clear, professional language.",
    "Hindi": "आप केवल हिंदी में जवाब दें। सरल, स्पष्ट हिंदी का उपयोग करें।"
}

PSYCHOMETRIC_PROMPT_TEMPLATE = """
Generate 18 psychometric questions for students.

LANGUAGE: {language_instruction}

Requirements:
- Cover all RIASEC categories:
  realistic, investigative, artistic, social, enterprising, conventional
- Each question must include:
  id, question, type

Return STRICT JSON only (with English keys):
[
  {{
    "id": 1,
    "question": "...",
    "type": "realistic"
  }}
]

IMPORTANT: Keep JSON keys in English. Only translate the question text.
"""

def generate_psychometric_questions(language: str = "English"):
    lang_instruction = LANGUAGE_INSTRUCTIONS.get(language, LANGUAGE_INSTRUCTIONS["English"])
    prompt = PSYCHOMETRIC_PROMPT_TEMPLATE.format(language_instruction=lang_instruction)
    
    response = llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role":"user","content":prompt}]
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return []


TEST_PROMPT_TEMPLATE = """
You are an exam generator for Indian students.

LANGUAGE: {language_instruction}

Generate 5 MCQ questions for subject: {subject}

Level: Class 11-12 (India)

Each question must include:
- question (in {language})
- 4 options (in {language})
- correct answer

Return STRICT JSON (with English keys):
[
  {{
    "question": "...",
    "options": ["A", "B", "C", "D"],
    "answer": "correct option"
  }}
]

IMPORTANT: Keep JSON keys in English. Only translate question and options to {language}.
"""

def generate_questions_for_subject(subject: str, language: str = "English"):
    lang_instruction = LANGUAGE_INSTRUCTIONS.get(language, LANGUAGE_INSTRUCTIONS["English"])
    prompt = TEST_PROMPT_TEMPLATE.format(
        language_instruction=lang_instruction,
        subject=subject,
        language=language
    )

    response = llm.chat.completions.create(
      model="openai/gpt-oss-120b",
      messages=[{"role":"user","content":prompt}]
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return []


RECOMMENDATION_PROMPT_TEMPLATE = """
You are a career advisor for Indian students.

LANGUAGE: {language_instruction}

Input:
Top Interests: {top_1}, {top_2}
Score: {score}%
Subjects: {subjects}

Tasks:
1. Suggest ONE primary career (in {language})
2. Suggest 2 secondary career options (in {language})
3. Suggest relevant Indian exams (keep exam names in English or standard format)
4. Explain WHY this career suits the student (in {language})

Respond STRICT JSON (with English keys):
{{
  "career": "...",
  "secondary_careers": ["...", "..."],
  "exams": ["...", "..."],
  "feedback": "..."
}}

IMPORTANT: Keep JSON keys in English. Translate career names, feedback, and recommendations to {language}.
"""

def generate_recommendation(top_1, top_2, score, subjects, language: str = "English"):
    lang_instruction = LANGUAGE_INSTRUCTIONS.get(language, LANGUAGE_INSTRUCTIONS["English"])
    prompt = RECOMMENDATION_PROMPT_TEMPLATE.format(
        language_instruction=lang_instruction,
        top_1=top_1,
        top_2=top_2,
        score=score,
        subjects=", ".join(subjects),
        language=language
    )

    response = llm.chat.completions.create(
      model="openai/gpt-oss-120b",
      messages=[{"role":"user","content":prompt}]
    )

    import json, re

    text = response.choices[0].message.content.strip()
    text = re.sub(r"```json|```", "", text)

    try:
        return json.loads(text)
    except:
        return {}