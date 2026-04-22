from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    test_id: int