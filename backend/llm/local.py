from .base import BaseLLM

class LocalLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        # For now: return prompt directly (acts like "no LLM")
        return prompt
