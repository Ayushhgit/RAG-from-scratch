from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
from config import EMBEDDING_MODEL_NAME

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    def embed(self, texts: List[str]) -> np.ndarray:
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=False
        )
        return embeddings
