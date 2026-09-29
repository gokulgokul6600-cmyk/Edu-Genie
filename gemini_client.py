from functools import lru_cache

from fastapi import HTTPException
from google import genai

from config import settings


@lru_cache
def get_client():
    if not settings.has_gemini:
        raise HTTPException(
            status_code=503,
            detail="GEMINI_API_KEY is not configured. Add it to the .env file.",
        )

    return genai.Client(api_key=settings.gemini_api_key)


def generate_text(prompt: str) -> str:
    client = get_client()

    try:
        response = client.models.generate_content(
            model=settings.gemini_model,
            contents=prompt,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Gemini API request failed: {exc}",
        ) from exc

    text = (response.text or "").strip()

    if not text:
        raise HTTPException(
            status_code=502,
            detail="Gemini returned an empty response.",
        )

    return text