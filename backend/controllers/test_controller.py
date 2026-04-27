from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.database import get_db
from security import get_current_user
from services.test_service import generate_test, evaluate_test, get_recommendations
from models.test_model import Test
from models.response_model import Response
from models.recommendation_model import Recommendation
from schemas.test_schema import TestCreate, TestSubmit

router = APIRouter(prefix="/test", tags=["Test"])


@router.post("/generate")
def create_test(
    data: TestCreate,
    language: str = Query("English", description="Language for questions: English or Hindi"),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Generate test questions for selected subjects"""
    # Validate language
    if language not in ["English", "Hindi"]:
        language = "English"
    
    questions = generate_test(data.subjects, language=language)

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
        "questions": questions,
        "language": language
    }


@router.post("/submit")
def submit_test(
    data: TestSubmit,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Submit answers and get evaluation"""
    test = db.query(Test).filter(
        Test.id == data.test_id,
        Test.user_id == current_user.id
    ).first()
    
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    
    questions = test.questions
    evaluation = evaluate_test(questions, data.user_answers)
    
    # Store response
    response = Response(
        user_id=current_user.id,
        test_id=test.id,
        user_answers=data.user_answers,
        score=evaluation["score"],
        total_questions=evaluation["total"]
    )
    
    db.add(response)
    db.commit()
    db.refresh(response)
    
    return {
        "response_id": response.id,
        **evaluation
    }


@router.get("/results/{test_id}")
def get_test_results(
    test_id: int,
    language: str = Query("English", description="Language for recommendations: English or Hindi"),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get test results and career recommendations"""
    # Validate language
    if language not in ["English", "Hindi"]:
        language = "English"
    
    test = db.query(Test).filter(
        Test.id == test_id,
        Test.user_id == current_user.id
    ).first()
    
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    
    response = db.query(Response).filter(Response.test_id == test_id).first()
    
    if not response:
        raise HTTPException(status_code=404, detail="Response not found")
    
    # Check if recommendation already exists
    recommendation = db.query(Recommendation).filter(
        Recommendation.test_id == test_id
    ).first()
    
    if not recommendation:
        # Generate new recommendation with language
        rec_data = get_recommendations(test_id, db, language=language)
        
        if rec_data:
            recommendation = Recommendation(
                user_id=current_user.id,
                test_id=test_id,
                career=rec_data.get("career", ""),
                secondary_careers=rec_data.get("secondary_careers", []),
                exams=rec_data.get("exams", []),
                feedback=rec_data.get("feedback", "")
            )
            db.add(recommendation)
            db.commit()
            db.refresh(recommendation)
    
    return {
        "score": response.score,
        "total": response.total_questions,
        "accuracy": f"{(response.score / response.total_questions * 100):.1f}%",
        "passed": response.score >= (response.total_questions * 0.5),
        "career": recommendation.career if recommendation else "",
        "secondary_careers": recommendation.secondary_careers if recommendation else [],
        "exams": recommendation.exams if recommendation else [],
        "feedback": recommendation.feedback if recommendation else "",
        "language": language
    }