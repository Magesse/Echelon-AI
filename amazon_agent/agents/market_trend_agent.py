from states.market_state import MarketState, TrendData
from utils.llm import get_groq_llm

def trend_node(state: MarketState) -> dict:
    """Toplanan ham veriyi analiz edip trend skorlarını çıkarır."""
    print("📈 Trend Agent çalışıyor...")
    
    if not state.get("raw_web_data"):
        return {"errors": ["Trend Agent: İncelenecek ham veri bulunamadı."]}
        
    llm = get_groq_llm(schema=TrendData)
    prompt = f"Şu veriye dayanarak Amazon pazar trend analizi yap:\n{state['raw_web_data']}"
    
    try:
        result = llm.invoke(prompt)
        return {"trends": result}
    except Exception as e:
        return {"errors": [f"Trend Agent Hatası: {str(e)}"]}