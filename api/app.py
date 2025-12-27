from fastapi import FastAPI
from retrieval.retriever import Retriever
from generation.generator import generate_answer
from vectorstore.faiss_store import FAISSVectorStore

app = FastAPI()

vector_store = FAISSVectorStore(embedding_dim=384)
retriever = Retriever(vector_store)

@app.post("/query")
def query_rag(query: str):
    retrieved = retriever.retrieve(query)

    context = "\n".join([doc["text"] for doc in retrieved])
    answer = generate_answer(context, query)

    return {
        "query": query,
        "answer": answer,
        "sources": retrieved
    }
