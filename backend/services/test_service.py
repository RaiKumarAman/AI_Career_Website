from services.ai_service import generate_questions_for_subject, generate_recommendation

def generate_test(subjects: list, language: str = "English"):
    """
    Generate test questions for given subjects in specified language.
    
    Args:
        subjects: List of subject names
        language: Language for questions (English or Hindi)
    """
    all_questions = []

    for subject in subjects:
        questions = generate_questions_for_subject(subject, language=language)

        for q in questions:
            q["subject"] = subject  

        all_questions.extend(questions)

    return all_questions


def evaluate_test(questions: list, user_answers: dict) -> dict:
    """
    Evaluate user answers against correct answers.
    
    Args:
        questions: List of test questions with correct answers
        user_answers: Dict with question_index as key and user's answer as value
    
    Returns:
        {
            "score": int,
            "total": int,
            "accuracy": str,
            "feedback": str,
            "passed": bool,
            "subject_wise_performance": dict
        }
    """
    score = 0
    total = len(questions)
    subject_scores = {}
    
    for idx, question in enumerate(questions):
        user_answer = user_answers.get(str(idx), "").strip().upper()
        correct_answer = question.get("answer", "").strip().upper()
        subject = question.get("subject", "General")
        
        if subject not in subject_scores:
            subject_scores[subject] = {"correct": 0, "total": 0}
        
        subject_scores[subject]["total"] += 1
        
        if user_answer == correct_answer:
            score += 1
            subject_scores[subject]["correct"] += 1
    
    accuracy = (score / total * 100) if total > 0 else 0
    passed = score >= (total * 0.5)  # 50% is pass
    
    # Generate feedback based on performance
    if accuracy >= 80:
        feedback = "Excellent performance! You have a strong grasp of the subjects."
    elif accuracy >= 60:
        feedback = "Good performance. With more practice, you can improve further."
    elif accuracy >= 40:
        feedback = "Average performance. Focus on weak areas and practice more."
    else:
        feedback = "Consider reviewing the basics and attempting again."
    
    return {
        "score": score,
        "total": total,
        "accuracy": f"{accuracy:.1f}%",
        "feedback": feedback,
        "passed": passed,
        "subject_wise_performance": subject_scores
    }


def get_recommendations(test_id: int, db, language: str = "English") -> dict:
    """
    Generate career recommendations based on test performance in specified language.
    
    Args:
        test_id: ID of the test
        db: Database session
        language: Language for recommendations (English or Hindi)
    """
    from models.test_model import Test
    from models.response_model import Response
    
    test = db.query(Test).filter(Test.id == test_id).first()
    response = db.query(Response).filter(Response.test_id == test_id).first()
    
    if not test or not response:
        return {}
    
    score = (response.score / response.total_questions * 100) if response.total_questions > 0 else 0
    passed = score >= 50
    
    # Default recommendations
    subjects = test.subjects if test.subjects else ["General"]
    top_subject = subjects[0] if subjects else "General"
    
    recommendation_data = generate_recommendation(
        top_1=top_subject,
        top_2=subjects[1] if len(subjects) > 1 else "Science",
        score=int(score),
        subjects=subjects,
        language=language
    )
    
    return {
        **recommendation_data,
        "score": int(score),
        "passed": passed,
        "language": language
    }