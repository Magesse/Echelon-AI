from states.market_state import MarketState
from utils.tavily_client import TavilyClient


def research_node(state: MarketState) -> dict:
    """Tavily üzerinden interneti tarar ve ham verileri toplar."""
    print("🔍 Research Agent çalışıyor...")

    tavily = TavilyClient()

    # Sorguyu al (Enhanced varsa onu, yoksa ana query'yi kullan)
    query = state.get("enhanced_query") or state.get("query", "")

    # Amazon odaklı tam sorguyu oluştur
    search_query = f"Amazon market analysis for {query}"

    # EMNİYET SİBOBU: Tavily limit kontrolü (400 karakter sınırı)
    if len(search_query) > 400:
        print(f"⚠️ Sorgu çok uzun ({len(search_query)} karakter), kırpılıyor...")
        search_query = search_query[:400]

    try:
        # İnterneti tara
        results = tavily.search(query=search_query, max_results=8)

        # Sadece içerik dolu olanları topla
        raw_texts = [r.get("content", "") for r in results if r.get("content")]

        # Veri bulundu mu kontrol et
        return {
            "raw_web_data": raw_texts,
            "source_count": len(raw_texts),
            "entity_exists": len(raw_texts) > 0
        }
    except Exception as e:
        print(f"❌ [Tavily] Arama hatası: {str(e)}")
        return {
            "errors": [f"Research Agent Hatası: {str(e)}"],
            "entity_exists": False
        }