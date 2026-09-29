from pydantic import BaseModel, Field


class QnARequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=12000)


class ExplanationRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=12000)
    level: str = Field(default="beginner", min_length=1, max_length=50)


class QuizRequest(BaseModel):
    text: str = Field(..., min_length=20, max_length=30000)


class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=20, max_length=50000)
    max_words: int = Field(default=150, ge=30, le=500)


class LearningPathRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=500)
    level: str = Field(default="beginner", min_length=1, max_length=50)
    weeks: int = Field(default=8, ge=1, le=52)