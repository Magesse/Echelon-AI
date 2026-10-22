from states.market_state import MarketState, AutomationData
from utils.llm import get_groq_llm

def automation_node(state: MarketState) -> dict:
    """Somut aksiyon adımları ve risk analizi üretir."""
    print("⚙️ Automation Agent çalışıyor...")
    
    llm = get_groq_llm(schema=AutomationData)
    context = f"İçgörüler: {state.get('insights')}\nTrendler: {state.get('trends')}"
    prompt = f"Bu Amazon verilerine dayanarak en iyi ürün fırsatlarını, olası riskleri ve hemen atılması gereken adımları listele:\n{context}"
    
    try:
        result = llm.invoke(prompt)
        return {"automation": result}
    except Exception as e:
        return {"errors": [f"Automation Agent Hatası: {str(e)}"]}