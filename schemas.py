from pydantic import BaseModel, Field


class QARequest(BaseModel):
    question: str = Field(..., min_length=2, max_length=5000)


class ExplainRequest(BaseModel):
    topic: str = Field(..., min_length=2, max_length=1000)


class QuizRequest(BaseModel):
    text: str = Field(..., min_length=20, max_length=12000)


class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=20, max_length=20000)


class LearningPathRequest(BaseModel):
    topic: str = Field(..., min_length=2, max_length=1000)
    level: str = Field(default="Beginner", max_length=50)
