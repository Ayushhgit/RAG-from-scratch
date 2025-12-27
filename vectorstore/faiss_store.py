import faiss
import numpy as np
from typing import List

class FAISSVectorStore:
    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatIP(embedding_dim)
        self.texts: List[str] = []
        self.metadata: List[dict] = []

    def add(self, embeddings: np.ndarray, texts: List[str], metadata: List[dict]):
        self.index.add(embeddings)
        self.texts.extend(texts)
        self.metadata.extend(metadata)

    def search(self, query_embedding: np.ndarray, k: int):
        scores, indices = self.index.search(
            np.array([query_embedding]), k
        )

        results = []
        for idx in indices[0]:
            results.append({
                "text": self.texts[idx],
                "metadata": self.metadata[idx]
            })

        return results
