def evaluate_test(questions, user_answers):

    correct = 0

    # map question → correct answer
    answer_map = {q["question"]: q["answer"] for q in questions}

    for ans in user_answers:
        correct_answer = answer_map.get(ans.question)

        if correct_answer and ans.selected_option == correct_answer:
            correct += 1

    total = len(questions)
    score = (correct / total) * 100 if total > 0 else 0

    return score, total