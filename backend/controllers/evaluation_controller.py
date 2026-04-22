from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from security import get_current_user
from models.test_model import Test
from models.response_model import Response
from schemas.evaluation_schema import SubmitTest
from services.evaluation_service import evaluate_test

router = APIRouter(prefix="/test", tags=["Evaluation"])


@router.post("/submit")
def submit_test(
    data: SubmitTest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    test = db.query(Test).filter(Test.id == data.test_id).first()

    if not test:
        raise HTTPException(status_code=404, detail="Test not found")

    score, total = evaluate_test(test.questions, data.answers)

    response = Response(
        test_id=test.id,
        user_answers=[a.dict() for a in data.answers],
        score=score,
        total_questions=total
    )

    db.add(response)
    db.commit()

    return {
        "score": score,
        "total_questions": total
    }