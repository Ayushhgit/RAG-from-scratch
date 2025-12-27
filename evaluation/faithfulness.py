def is_faithful(answer: str, context: str) -> bool:
    answer_sentences = [s.strip() for s in answer.split(".") if s.strip()]
    context_lower = context.lower()

    for sentence in answer_sentences:
        if sentence.lower() not in context_lower:
            return False

    return True
