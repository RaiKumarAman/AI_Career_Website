from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from security import get_current_user
from models.psychometric_model import PsychometricResult
from services.subject_service import get_subjects

router = APIRouter(prefix="/subjects", tags=["Subjects"])


@router.get("/suggest")
def suggest_subjects(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    result = db.query(PsychometricResult).filter(
        PsychometricResult.user_id == current_user.id
    ).order_by(PsychometricResult.id.desc()).first()

    if not result:
        raise HTTPException(
            status_code=400,
            detail="Complete psychometric test first"
        )

    subjects = get_subjects(result.top_1, result.top_2)

    return {
        "top_interests": [result.top_1, result.top_2],
        "subjects": subjects
    }