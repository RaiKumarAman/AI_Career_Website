from pydantic import BaseModel
from typing import List, Dict

class TestCreate(BaseModel):
    subjects: List[str]

class TestSubmit(BaseModel):
    test_id: int
    user_answers: Dict[str, str]  # {question_index: answer}