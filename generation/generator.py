from openai import OpenAI
from generation.prompt import build_prompt
from config import LLM_MODEL_NAME

client = OpenAI()

def generate_answer(context: str, query: str) -> str:
    prompt = build_prompt(context, query)

    response = client.chat.completions.create(
        model=LLM_MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )

    return response.choices[0].message.content.strip()
