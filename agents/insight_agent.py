from states.market_state import MarketState, InsightData
from utils.llm import get_groq_llm

def insight_node(state: MarketState) -> dict:
    """Trend, Rakip ve Review verilerini sentezleyip gizli fırsatları bulur."""
    print("💡 Insight Agent çalışıyor...")
    
    llm = get_groq_llm(schema=InsightData)
    context = f"Trendler: {state.get('trends')}\nRakipler: {state.get('competitors')}\nYorumlar: {state.get('reviews')}"
    prompt = f"Aşağıdaki sentezlenmiş Amazon pazar verilerine dayanarak gizli fırsatları ve farklılaşma stratejilerini çıkar:\n{context}"
    
    try:
        result = llm.invoke(prompt)
        return {"insights": result}
    except Exception as e:
        return {"errors": [f"Insight Agent Hatası: {str(e)}"]}