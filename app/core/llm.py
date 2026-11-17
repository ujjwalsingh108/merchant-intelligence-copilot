from langchain_groq import ChatGroq
from app.core.config import settings

def get_llm():
    """
    Initializes the Groq LLM. 
    """
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=settings.GROQ_MODEL, 
        temperature=0.0, # Strict zero for deterministic SQL generation
        max_tokens=2048,
        model_kwargs={
            "top_p": 0.95,
        }
    )