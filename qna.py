from gemini_service import generate_text

SYSTEM = """
You are EduGenie, a student-friendly educational assistant.
Answer the user's academic question accurately and clearly.
Use simple language, short sections and bullet points when useful.
If a question is ambiguous, state the assumption briefly.
Do not invent citations or sources.
"""

def answer_question(question: str) -> str:
    prompt = f"""{SYSTEM}

Question:
{question}

Give a concise but useful answer suitable for a learner."""
    return generate_text(prompt)
