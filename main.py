from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import (
    LearningPathRequest,
    QnARequest,
    QuizRequest,
    SummaryRequest,
    ExplanationRequest,
)

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations
from config import settings


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="EduGenie",
    description="Google Gemini powered learning assistant.",
    version="1.0.0",
)


# ---------------------------------------------------------
# Static files
# ---------------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


# ---------------------------------------------------------
# Templates
# ---------------------------------------------------------

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# ---------------------------------------------------------
# Frontend
# ---------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "app": "EduGenie",
        "gemini_configured": bool(settings.gemini_api_key),
        "model": settings.gemini_model,
    }


# ---------------------------------------------------------
# Question Answering
# ---------------------------------------------------------

@app.post("/qa")
async def qa(payload: QnARequest):

    answer = answer_question(
        payload.question
    )

    return {
        "answer": answer
    }


# ---------------------------------------------------------
# Concept Explanation
# ---------------------------------------------------------

@app.post("/explain")
async def explain(payload: ExplanationRequest):

    answer = explain_topic(
        payload.topic,
        payload.level
    )

    return {
        "answer": answer
    }


# ---------------------------------------------------------
# Quiz Generation
# ---------------------------------------------------------

@app.post("/quiz")
async def quiz(payload: QuizRequest):

    result = generate_quiz(
        payload.text
    )

    return result.model_dump()


# ---------------------------------------------------------
# Summarization
# ---------------------------------------------------------

@app.post("/summarize")
async def summarize(payload: SummaryRequest):

    summary = summarize_text(
        payload.text,
        payload.max_words
    )

    return {
        "summary": summary
    }


# ---------------------------------------------------------
# Learning Recommendations
# ---------------------------------------------------------

@app.post("/learn/recommendations")
async def recommendations(
    payload: LearningPathRequest
):

    result = get_learning_recommendations(
        payload.topic,
        payload.level,
        payload.weeks
    )

    return {
        "learning_path": result
    }