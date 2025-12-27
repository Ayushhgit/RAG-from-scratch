def build_prompt(context: str, query: str) -> str:
    return f"""
You are a factual assistant.

Use ONLY the information provided in the context below.
If the answer cannot be found in the context, reply with:
"I don't know based on the provided context."

Context:
{context}

Question:
{query}

Answer:
"""
