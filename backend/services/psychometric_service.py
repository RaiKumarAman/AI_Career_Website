def calculate_scores(questions, answers):
    scores = {
        "realistic": 0,
        "investigative": 0,
        "artistic": 0,
        "social": 0,
        "enterprising": 0,
        "conventional": 0
    }

    # map question id → type
    q_map = {q.id: q.type for q in questions}

    for ans in answers:
        q_type = q_map.get(ans.question_id)
        if q_type:
            scores[q_type] += ans.rating

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top_1 = sorted_scores[0][0]
    top_2 = sorted_scores[1][0]

    return scores, top_1, top_2