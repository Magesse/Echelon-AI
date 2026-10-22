from langgraph.graph import StateGraph, START, END
from states.market_state import MarketState

# Ajanları import et (diğerleri aynı, sadece validator ve route ekliyoruz)
from agents.prompt_enhancer import prompt_node
from agents.research_agent import research_node
from agents.validator_agent import validator_node
from agents.keyword_agent import keyword_node
from agents.market_trend_agent import trend_node
from agents.competitor_agent import competitor_node
from agents.review_agent import review_node
from agents.insight_agent import insight_node
from agents.automation_agent import automation_node
from agents.report_agent import report_node


def route_after_validation(state):
    # Eğer errors listesi doluysa, ürünü bulamadık veya uydurma tespit ettik
    if state.get("errors"):
        return "report"
    return "keyword"


def build_market_graph():
    builder = StateGraph(MarketState)

    # Düğümler
    builder.add_node("prompt", prompt_node)
    builder.add_node("research", research_node)
    builder.add_node("validator", validator_node)
    builder.add_node("keyword", keyword_node)
    builder.add_node("trend", trend_node)
    builder.add_node("competitor", competitor_node)
    builder.add_node("review", review_node)
    builder.add_node("insight", insight_node)
    builder.add_node("automation", automation_node)
    builder.add_node("report", report_node)

    # Akış
    builder.add_edge(START, "prompt")
    builder.add_edge("prompt", "research")
    builder.add_edge("research", "validator")  # <-- Önce doğrula!

    # Karar anı: Geçerse keyword'e, kalırsa rapor'a
    builder.add_conditional_edges(
        "validator",
        route_after_validation,
        {"report": "report", "keyword": "keyword"}
    )

    builder.add_edge("keyword", "trend")
    builder.add_edge("keyword", "competitor")
    builder.add_edge("keyword", "review")

    builder.add_edge(["trend", "competitor", "review"], "insight")
    builder.add_edge("insight", "automation")
    builder.add_edge("automation", "report")
    builder.add_edge("report", END)

    return builder.compile()


market_graph = build_market_graph()