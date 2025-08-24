import os
from dotenv import load_dotenv
from typing import Optional

try:
    # Optional import; only needed if you want to create LLMs here
    from langchain_ollama import ChatOllama  # type: ignore
except Exception:  # pragma: no cover
    ChatOllama = None  # type: ignore


def load_env() -> None:
    """Load environment variables from a local .env file if present."""
    load_dotenv()


def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
    """Helper to fetch env vars with optional default."""
    return os.getenv(key, default)


def get_llm(model_env_key: str = "OLLAMA_MODEL", default_model: str = "deepseek-r1:7b"):
    """Return an Ollama Chat LLM using env or default model.

    Note: Requires langchain-ollama and a running Ollama instance.
    """
    if ChatOllama is None:
        raise ImportError(
            "langchain-ollama not installed or import failed. Add it to requirements.txt."
        )
    load_env()
    model = get_env(model_env_key, default_model)
    return ChatOllama(model=model)
