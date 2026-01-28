def build_prompt(question: str, context: str) -> str:
    return f"""
You are a question-answering assistant.

Rules:
- Answer ONLY the question.
- Use ONLY the provided context.
- Do NOT repeat the context.
- Do NOT explain your reasoning.
- If the answer is not in the context, say: "I don't have enough information to answer that."

Context:
{context}

Question:
{question}

Answer:
""".strip()
