import operator
from typing import Annotated, TypedDict
from pydantic import BaseModel, Field

# ==========================================
# AJAN ÇIKTILARI İÇİN KESİN ŞEMALAR (No Hallucination)
# ==========================================

class KeywordData(BaseModel):
    turkish_keywords: list[str] = Field(default_factory=list)
    english_keywords: list[str] = Field(default_factory=list)
    long_tail_keywords: list[str] = Field(default_factory=list)
    trend_keywords: list[str] = Field(default_factory=list)

class TrendData(BaseModel):
    trend_strength: int = Field(description="1 ile 100 arası trend puanı")
    opportunity_score: int = Field(description="1 ile 100 arası fırsat puanı")
    trend_status: str = Field(description="hot, promising veya weak")
    growth_opportunities: list[str] = Field(description="Büyüme fırsatları")

class CompetitorData(BaseModel):
    name: str = Field(description="Rakip adı veya markası")
    price_range: str = Field(description="Tahmini fiyat aralığı")
    weaknesses: list[str] = Field(description="Müşteri şikayetlerine dayalı zayıf yönler")

class ReviewData(BaseModel):
    overall_sentiment: str = Field(description="Pozitif, Negatif veya Nötr")
    top_complaints: list[str] = Field(default_factory=list)
    customer_wants: list[str] = Field(default_factory=list)

class InsightData(BaseModel):
    hidden_opportunities: list[str] = Field(description="Pazardaki gizli fırsatlar")
    differentiation_angles: list[str] = Field(description="Farklılaşma stratejileri")

class AutomationData(BaseModel):
    top_product_opportunities: list[str]
    immediate_next_steps: list[str]
    risks: list[str]

# Ajanların liste dönebilmesi için sarmalayıcı model
class CompetitorList(BaseModel):
    items: list[CompetitorData] = Field(default_factory=list)

# ==========================================
# LANGGRAPH STATE TANIMI
# ==========================================

class MarketState(TypedDict):
    """
    Sistemin merkezi hafızası.
    Annotated[list, operator.add] kullanımı, ajanların verileri 
    birbirinin üzerine yazmasını engeller, listeye ekler.
    """
    query: str
    enhanced_query: str
    
    # Araştırma ve doğruluğu
    raw_web_data: Annotated[list[str], operator.add]
    source_count: int
    entity_exists: bool
    
    # Ajan Çıktıları
    keywords: KeywordData | None
    trends: TrendData | None
    competitors: Annotated[list[CompetitorData], operator.add]
    reviews: ReviewData | None
    insights: InsightData | None
    automation: AutomationData | None
    
    # Sonuçlar ve Hatalar
    final_report: str
    report_path: str
    errors: Annotated[list[str], operator.add]