from pydantic import BaseModel, Field


class QuizQuestion(BaseModel):
    question: str
    options: list[str] = Field(..., min_length=4, max_length=4)
    correct_answer: str
    explanation: str


class QuizResponse(BaseModel):
    title: str
    questions: list[QuizQuestion] = Field(
        ...,
        min_length=3,
        max_length=3
    )


class LearningStep(BaseModel):
    stage: str
    topics: list[str]
    timeline: str
    activities: list[str]
    resources: list[str]


class LearningPathResponse(BaseModel):
    topic: str
    learner_level: str
    overview: str
    steps: list[LearningStep]
    study_tips: list[str]