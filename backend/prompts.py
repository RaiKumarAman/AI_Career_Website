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