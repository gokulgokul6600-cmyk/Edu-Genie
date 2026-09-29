from gemini_client import generate_text


def summarize_text(text: str, max_words: int = 150) -> str:
    prompt = f"""
You are EduGenie, an AI educational assistant.

Summarize the following educational content for a student.

Content:
{text}

Maximum length:
{max_words} words

Instructions:
- Preserve the central ideas and important facts.
- Remove repetition and minor details.
- Use clear and simple language.
- Keep the summary coherent and easy to study.
- Do not add facts that are not present in the original content.
- Do not add citations, references, or information from outside the provided content.
- Return only the summary.
"""

    return generate_text(prompt)