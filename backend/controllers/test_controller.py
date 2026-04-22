from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from security import get_current_user
from services.test_service import generate_test
from models.test_model import Test
from schemas.test_schema import TestCreate

router = APIRouter(prefix="/test", tags=["Test"])


@router.post("/generate")
def create_test(
    data: TestCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    questions = generate_test(data.subjects)

    if not questions:
        raise HTTPException(status_code=500, detail="Failed to generate test")

    test = Test(
        user_id=current_user.id,
        subjects=data.subjects,
        questions=questions
    )

    db.add(test)
    db.commit()
    db.refresh(test)

    return {
        "test_id": test.id,
        "questions": questions
    }