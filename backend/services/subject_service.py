from ria_sec_mapping import RIASEC_SUBJECT_MAP, DEFAULT_MAPPING

def get_subjects(top_1: str, top_2: str):

    # normalize order
    pair = tuple(sorted([top_1, top_2]))

    if pair in RIASEC_SUBJECT_MAP:
        return RIASEC_SUBJECT_MAP[pair]

    # fallback
    subjects = list(set(
        DEFAULT_MAPPING[top_1] + DEFAULT_MAPPING[top_2]
    ))

    return subjects