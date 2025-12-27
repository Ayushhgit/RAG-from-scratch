from ingestion.embedder import Embedder
from vectorstore.faiss_store import FAISSVectorStore
from config import TOP_K_RETRIEVAL

class Retriever:
    def __init__(self, vector_store: FAISSVectorStore):
        self.embedder = Embedder()
        self.vector_store = vector_store

    def retrieve(self, query: str, k: int = TOP_K_RETRIEVAL):
        query_embedding = self.embedder.embed([query])[0]
        return self.vector_store.search(query_embedding, k)
