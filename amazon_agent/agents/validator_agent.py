from pydantic import BaseModel, Field
from states.market_state import MarketState
from utils.llm import get_groq_llm


class RealityCheck(BaseModel):
    is_real: bool = Field(description="Bu ürün e-ticarette gerçek, satılabilir, mantıklı bir ürün mü?")
    reason: str = Field(description="Neden gerçek veya uydurma olduğu (kısa açıklama)")


def validator_node(state: MarketState) -> dict:
    print("🛡️ Validator (Early Check) çalışıyor...")

    # Araştırmadan gelen ham verileri al
    raw_data = str(state.get("raw_web_data", ""))[:3000]

    # LLM'e sor: Bu ürün gerçek mi yoksa alakasız kelimeler mi?
    llm = get_groq_llm(schema=RealityCheck)

    prompt = f"""
    Kullanıcının araştırdığı ürün: {state['query']}
    İnternetten toplanan ham veriler: {raw_data}

    Kritik Görev: Bu verileri incele. Kullanıcının aradığı ürün piyasada mantıklı bir karşılığı olan gerçek bir ürün mü? 
    Eğer ürün absürt, imkansız veya alakasız bir kombinasyon ise (örn: RGB ışıklı tahta kaşık) is_real=False dön.
    """

    try:
        result = llm.invoke(prompt)
        if not result.is_real:
            return {"errors": [f"🛑 HALLUCINATION GUARD AKTİF: {result.reason}"]}
        return {}  # Sorun yok, akışa devam et
    except Exception as e:
        return {"errors": [f"Validator Hatası: {str(e)}"]}