from states.market_state import MarketState
from utils.llm import get_gemini_llm


def prompt_node(state: MarketState) -> dict:
    """Kullanıcının sorgusunu profesyonel bir Amazon araştırma sorgusuna çevirir."""
    print("🪄 Prompt Enhancer çalışıyor...")
    llm = get_gemini_llm()

    prompt = f"""
    Sen uzman bir Amazon FBA araştırmacısın. 
    Aşağıdaki kullanıcı sorgusunu detaylı, İngilizce ve pazar araştırmasına uygun tek satırlık bir sorguya çevir. 
    Sadece zenginleştirilmiş sorguyu döndür.

    Kullanıcı Sorgusu: {state['query']}
    """

    result = llm.invoke(prompt)
    return {"enhanced_query": result.content.strip()}