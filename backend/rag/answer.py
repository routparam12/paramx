def clean_answer(text: str) -> str:
    if not text:
        return ""

    # Remove markdown artifacts
    lines = text.strip().splitlines()

    # Take first meaningful block only
    cleaned = []
    for line in lines:
        if line.strip().startswith(("Context:", "Question:", "Rules:")):
            continue
        cleaned.append(line)

    return "\n".join(cleaned).strip()
