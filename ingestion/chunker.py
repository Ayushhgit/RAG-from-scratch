from typing import List

def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap
        if start < 0:
            start = 0

    return chunks
