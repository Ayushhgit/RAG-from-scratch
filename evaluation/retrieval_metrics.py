def recall_at_k(retrieved_docs, relevant_docs, k):
    retrieved = retrieved_docs[:k]
    hits = sum(1 for doc in retrieved if doc in relevant_docs)
    return hits / len(relevant_docs)


def hit_rate(retrieved_docs, relevant_docs):
    return any(doc in relevant_docs for doc in retrieved_docs)
