import os
from datetime import datetime
from states.market_state import MarketState
from utils.llm import get_groq_llm
from config import OUTPUT_DIR

def report_node(state: MarketState) -> dict:
    print("📝 Report Agent çalışıyor...")

    errors = state.get('errors', [])
    hallucination_error = next((err for err in errors if "HALLUCINATION GUARD" in err), None)

    if hallucination_error:
        return {"final_report": f"# 🛑 Araştırma Durduruldu\n{hallucination_error}", "report_path": ""}

    llm = get_groq_llm()
    context = f"İçgörüler: {state.get('insights')}\nStratejiler: {state.get('automation')}\nTrendler: {state.get('trends')}\nRakipler: {state.get('competitors')}"
    prompt = f"Sen kıdemli bir E-Ticaret Veri Bilimcisisin. Aşağıdaki analizleri kullanarak profesyonel rapor yaz:\n\n{context}"

    try:
        result = llm.invoke(prompt)
        report_text = result.content

        # Dosya yolu oluşturma
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(OUTPUT_DIR, f"report_{timestamp}.md")

        # Markdown dosyasını kaydet
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_text)

        return {
            "final_report": report_text,
            "report_path": os.path.abspath(report_path)
        }
    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        return {"errors": [f"Report Agent Hatası: {str(e)}"]}