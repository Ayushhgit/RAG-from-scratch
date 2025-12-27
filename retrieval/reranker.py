from sentence_transformers import CrossEncoder
from typing import List, Dict

class CrossEncoderReranker:

    def __init__(
        self,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    ):
        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        documents: List[Dict],
        top_n: int = 5
    ) -> List[Dict]:

        # Build (query, document) pairs
        pairs = [
            (query, doc["text"])
            for doc in documents
        ]

        # Cross-encoder scoring
        scores = self.model.predict(pairs)

        # Attach scores to documents
        for doc, score in zip(documents, scores):
            doc["rerank_score"] = float(score)

        # Sort by score (descending)
        documents.sort(
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return documents[:top_n]
