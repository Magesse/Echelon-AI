from states.market_state import MarketState, ReviewData
from utils.llm import get_groq_llm

def review_node(state: MarketState) -> dict:
    """Müşteri şikayetlerini ve beklentilerini analiz eder."""
    print("⭐ Review Agent çalışıyor...")
    
    if not state.get("raw_web_data"):
        return {"errors": ["Review Agent: İncelenecek ham veri bulunamadı."]}
        
    llm = get_groq_llm(schema=ReviewData)
    prompt = f"Şu verideki müşteri yorumlarını, genel hissiyatı ve en sık karşılaşılan şikayetleri analiz et:\n{state['raw_web_data']}"
    
    try:
        result = llm.invoke(prompt)
        return {"reviews": result}
    except Exception as e:
        return {"errors": [f"Review Agent Hatası: {str(e)}"]}