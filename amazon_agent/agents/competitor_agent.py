from states.market_state import MarketState, CompetitorList
from utils.llm import get_groq_llm

def competitor_node(state: MarketState) -> dict:
    """Verilerdeki rakipleri, fiyat aralıklarını ve zayıf yönlerini bulur."""
    print("🏢 Competitor Agent çalışıyor...")
    
    if not state.get("raw_web_data"):
        return {"errors": ["Competitor Agent: İncelenecek ham veri bulunamadı."]}
        
    llm = get_groq_llm(schema=CompetitorList)
    prompt = f"Şu verideki rakipleri, tahmini fiyatlarını ve müşteri şikayetlerine dayalı zayıf yönlerini analiz et:\n{state['raw_web_data']}"
    
    try:
        result = llm.invoke(prompt)
        # result.items bir liste döndürür. operator.add sayesinde State'teki listeye otomatik eklenir.
        return {"competitors": result.items} 
    except Exception as e:
        return {"errors": [f"Competitor Agent Hatası: {str(e)}"]}