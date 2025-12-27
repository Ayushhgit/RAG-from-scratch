from pathlib import Path
from typing import List, Dict

def load_documents(path: str) -> List[Dict]:
    documents = []

    for file_path in Path(path).glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "text": text,
            "source": file_path.name
        })

    return documents
