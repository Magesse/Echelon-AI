from tavily import TavilyClient as _TavilyClient
from config import settings

class TavilyClient:
    def __init__(self):
        self.client = _TavilyClient(api_key=settings.tavily_api_key.get_secret_value())
        self.cache = {}

    def search(self, query: str, max_results: int = settings.max_research_results, 
               include_domains: list | None = None) -> list[dict]:
        
        # Cache anahtarı (Aynı aramayı tekrar tekrar API'ye sormamak için)
        cache_key = (query, max_results, tuple(include_domains or []))
        if cache_key in self.cache:
            return self.cache[cache_key]

        kwargs = {"query": query, "max_results": max_results, "search_depth": "advanced"}
        if include_domains:
            kwargs["include_domains"] = include_domains

        try:
            response = self.client.search(**kwargs)
            results = response.get("results", [])
            self.cache[cache_key] = results
            return results
        except Exception as e:
            print(f"[Tavily] Arama hatası: {e}")
            return []

    # Önceden olan amazon, reddit, news gibi spesifik aramaları
    # ajanların içinde dinamik yapacağız, bu yüzden burayı sadeleştirdik.