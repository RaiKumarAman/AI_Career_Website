from pydantic import BaseModel
from typing import List

class Answer(BaseModel):
    question: str
    selected_option: str

class SubmitTest(BaseModel):
    test_id: int
    answers: List[Answer]