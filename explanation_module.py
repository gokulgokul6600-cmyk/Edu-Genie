from gemini_client import generate_text


def explain_topic(topic: str, level: str = "beginner") -> str:
    prompt = f"""
You are EduGenie, an AI educational assistant.

Explain the following topic to a student.

Topic:
{topic}

Learner level:
{level}

Structure the explanation using these sections:

1. Simple Definition
2. How It Works
3. Concrete Example
4. Common Mistake or Misconception
5. One-Sentence Recap

Instructions:
- Use clear and simple language.
- Adapt the explanation to the learner level.
- Explain technical terms when they first appear.
- Use examples where helpful.
- Do not invent facts, statistics, citations, or sources.
- Make the explanation educational and easy to understand.
"""

    return generate_text(prompt)