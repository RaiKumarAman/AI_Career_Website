from services.ai_service import generate_questions_for_subject

def generate_test(subjects: list):

    all_questions = []

    for subject in subjects:
        questions = generate_questions_for_subject(subject)

        for q in questions:
            q["subject"] = subject  

        all_questions.extend(questions)

    return all_questions