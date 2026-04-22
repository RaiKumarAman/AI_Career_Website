from pydantic import BaseModel
from typing import List

class TestCreate(BaseModel):
    subjects: List[str]