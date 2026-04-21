from pydantic import BaseModel, conint
from typing import List

class Question(BaseModel):
    id: int
    type: str

class Answer(BaseModel):
    question_id: int
    rating: conint(ge=1, le=5)

class PsychometricSubmit(BaseModel):
    questions: List[Question]
    answers: List[Answer]