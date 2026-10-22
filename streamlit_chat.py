import streamlit as st
import os
from graphs.market_graph import market_graph

# 1. Sayfa Yapılandırması
st.set_page_config(
    page_title="Echelon AI",
    page_icon="assets/echolonlogo.png",
    layout="wide"
)

# 2. CSS Tasarımı
st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: #E0E0E0; }
    .stSidebar { background-color: #161a22; }
    .stButton>button { background: linear-gradient(90deg, #9b5de5 0%, #c77dff 100%); color: white; border: none; }
</style>
""", unsafe_allow_html=True)

# Session State (PDF izleri silindi)
if "messages" not in st.session_state: st.session_state.messages = []
if "history" not in st.session_state: st.session_state.history = []

# --- SIDEBAR ---
with st.sidebar:
    # width=None yerine width='stretch' veya belirli bir sayı veriyoruz
    st.image("assets/logo.png", width=250)
    st.title("Echelon AI")

    if st.button("➕ Yeni Araştırma", type="primary"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.subheader("🕒 Geçmiş Konuşmalar")
    for item in st.session_state.history:
        st.markdown(f"**{item['title']}**")

# --- ANA EKRAN ---
st.title("Echelon AI - Pazar Araştırması")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Echelon AI ile pazar analizi yapın...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Echelon AI analiz ediyor..."):
            try:
                result = market_graph.invoke({
                    "query": query,
                    "raw_web_data": [],
                    "competitors": [],
                    "errors": []
                })

                if "errors" in result and result["errors"]:
                    st.error("Report Agent'tan Hata Döndü:")
                    st.write(result["errors"])

                report = result.get("final_report", "Rapor oluşturulamadı.")

                st.session_state.history.append({"title": query[:15] + "..."})
                st.markdown(report)
                st.session_state.messages.append({"role": "assistant", "content": report})

            except Exception as e:
                st.error(f"Sistem Hatası: {str(e)}")
                import traceback

                st.code(traceback.format_exc())