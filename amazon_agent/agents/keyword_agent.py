from states.market_state import MarketState, KeywordData
from utils.llm import get_groq_llm


def keyword_node(state: MarketState) -> dict:
    """SEO ve pazar analizi için yapılandırılmış anahtar kelimeler üretir."""
    print("🔑 Keyword Agent çalışıyor...")

    # Model artık sadece KeywordData şemasına göre cevap verebilir.
    # Araya laf karıştıramaz, JSON dışına çıkamaz.
    llm = get_groq_llm(schema=KeywordData)
    query = state.get("enhanced_query") or state["query"]

    prompt = f"Generate Turkish, English, and long-tail SEO keywords for this Amazon product query: {query}"

    try:
        result = llm.invoke(prompt)
        return {"keywords": result}
    except Exception as e:
        return {"errors": [f"Keyword Agent Hatası: {str(e)}"]}