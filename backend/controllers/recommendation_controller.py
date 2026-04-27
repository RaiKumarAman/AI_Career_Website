from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.database import get_db
from security import get_current_user

from models.test_model import Test
from models.response_model import Response
from models.psychometric_model import PsychometricResult
from models.recommendation_model import Recommendation

from schemas.recommendation_schema import RecommendationRequest
from services.ai_service import generate_recommendation

router = APIRouter(prefix="/recommend", tags=["Recommendation"])


@router.post("/")
def recommend(
    data: RecommendationRequest,
    language: str = Query("English", description="Language for recommendations: English or Hindi"),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # Validate language
    if language not in ["English", "Hindi"]:
        language = "English"
    
    # 🔹 Get test
    test = db.query(Test).filter(Test.id == data.test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")

    # 🔹 Get response
    response = db.query(Response).filter(Response.test_id == test.id).first()
    if not response:
        raise HTTPException(status_code=404, detail="Test not submitted")

    # 🔹 Get psychometric result
    psych = db.query(PsychometricResult).filter(
        PsychometricResult.user_id == current_user.id
    ).order_by(PsychometricResult.id.desc()).first()

    if not psych:
        raise HTTPException(status_code=400, detail="Psychometric not done")

    # 🔹 Generate AI recommendation with language
    result = generate_recommendation(
        psych.top_1,
        psych.top_2,
        response.score,
        test.subjects,
        language=language
    )

    if not result:
        raise HTTPException(status_code=500, detail="AI failed")

    rec = Recommendation(
        user_id=current_user.id,
        test_id=test.id,
        career=result.get("career"),
        secondary_careers=result.get("secondary_careers"),
        exams=result.get("exams"),
        feedback=result.get("feedback")
    )

    db.add(rec)
    db.commit()

    return {
        **result,
        "language": language
    }