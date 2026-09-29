import json

from google.genai import types

from gemini_client import get_client
from config import settings
from schemas import QuizResponse


def generate_quiz(text: str) -> QuizResponse:
    prompt = f"""
You are EduGenie, an AI educational assistant.

Create a quiz based ONLY on the educational content below.

Content:
{text}

Requirements:
- Create exactly 3 multiple-choice questions.
- Each question must have exactly 4 options.
- Exactly one option must be correct.
- Include a clear explanation for each answer.
- Questions must test understanding of the provided content.
- Do not introduce facts that are unrelated to the content.
- The correct_answer field must exactly match one of the four options.
- Return only data matching the requested structured schema.
"""

    client = get_client()

    try:
        response = client.models.generate_content(
            model=settings.gemini_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=QuizResponse,
            ),
        )
    except Exception as exc:
        raise RuntimeError(f"Gemini quiz generation failed: {exc}") from exc

    raw = (response.text or "").strip()

    if not raw:
        raise RuntimeError("Gemini returned an empty quiz response.")

    try:
        data = json.loads(raw)
        return QuizResponse.model_validate(data)
    except Exception as exc:
        raise RuntimeError(
            f"Gemini returned invalid quiz data: {exc}"
        ) from exc