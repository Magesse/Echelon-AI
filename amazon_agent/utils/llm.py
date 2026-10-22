from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from config import settings

def get_groq_llm(schema: type[BaseModel] | None = None):
    """
    Groq modelini (Llama 3) döndürür.
    Eğer bir Pydantic şeması verilirse, ÇIKTIYI KESİNLİKLE O ŞEMAYA ZORLAR (No Hallucination).
    """
    llm = ChatGroq(
        api_key=settings.groq_api_key.get_secret_value(),
        model=settings.groq_model,
        temperature=0, # JSON uydurmasını engellemek için 0 olmalı
        max_retries=2
    )
    if schema:
        return llm.with_structured_output(schema)
    return llm

def get_gemini_llm():
    """
    Prompt iyileştirme için Gemini modelini döndürür.
    Bunda JSON zorlaması yok, sadece yaratıcı metin üretecek.
    """
    return ChatGoogleGenerativeAI(
        api_key=settings.gemini_api_key.get_secret_value(),
        model=settings.gemini_model,
        temperature=0.2
    )