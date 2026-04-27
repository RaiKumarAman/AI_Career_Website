from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.database import get_db
from security import get_current_user
from services.ai_service import generate_psychometric_questions
from services.psychometric_service import calculate_scores
from schemas.psychometric_schema import PsychometricSubmit
from models.psychometric_model import PsychometricResult

router = APIRouter(prefix="/psychometric", tags=["Psychometric"])


# ✅ STEP 1: Generate Questions
@router.get("/generate")
def generate_test(
    language: str = Query("English", description="Language for questions: English or Hindi"),
    current_user = Depends(get_current_user)
):
    # Validate language
    if language not in ["English", "Hindi"]:
        language = "English"
    
    questions = generate_psychometric_questions(language=language)

    if not questions:
        raise HTTPException(status_code=500, detail="Failed to generate questions")

    return {"questions": questions, "language": language}


# ✅ STEP 2: Submit Answers
@router.post("/submit")
def submit_test(
    data: PsychometricSubmit,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    scores, top_1, top_2 = calculate_scores(data.questions, data.answers)

    result = PsychometricResult(
        user_id=current_user.id,
        realistic=scores["realistic"],
        investigative=scores["investigative"],
        artistic=scores["artistic"],
        social=scores["social"],
        enterprising=scores["enterprising"],
        conventional=scores["conventional"],
        top_1=top_1,
        top_2=top_2
    )

    db.add(result)
    db.commit()

    return {
        "scores": scores,
        "top_1": top_1,
        "top_2": top_2
    }