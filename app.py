import streamlit as st
import json
from agent import FinancialAgent, extract_user_data
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="AI Financial Advisor", layout="wide")

# Inizializzazione Stato
if "messages" not in st.session_state:
    st.session_state.messages = []
if "profile_data" not in st.session_state:
    st.session_state.profile_data = {"eta": "Non nota", "reddito": "Non noto", "risparmi": "Non noti", "rischio": "Non definito"}
if "agent" not in st.session_state:
    st.session_state.agent = FinancialAgent()

# SIDEBAR (Viene renderizzata ad ogni esecuzione)
with st.sidebar:
    st.header("📊 Profilo MiFID Live")
    # Formattazione carina per il profilo
    st.info(f"**Età:** {st.session_state.profile_data.get('eta')}")
    st.info(f"**Reddito:** {st.session_state.profile_data.get('reddito')}")
    st.info(f"**Risparmi:** {st.session_state.profile_data.get('risparmi')}")
    st.info(f"**Rischio:** {st.session_state.profile_data.get('rischio')}")
    
    if st.button("Reset"):
        st.session_state.messages = []
        st.session_state.profile_data = {"eta": "Non nota", "reddito": "Non noto", "risparmi": "Non noti", "rischio": "Non definito"}
        st.rerun()

st.title("🏦 Senior Financial Agent")

# Visualizzazione messaggi
for msg in st.session_state.messages:
    with st.chat_message("user" if isinstance(msg, HumanMessage) else "assistant"):
        st.markdown(msg.content)

# Gestione Input
if user_input := st.chat_input("Scrivi qui..."):
    # 1. ESTRAZIONE IMMEDIATA
    old_profile = st.session_state.profile_data.copy()
    new_profile = extract_user_data(user_input, old_profile)
    
    # 2. Se il profilo è cambiato, lo salviamo e forziamo il rerun per aggiornare la sidebar subito
    st.session_state.profile_data = new_profile
    
    # Aggiungiamo il messaggio dell'utente
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Risposta dell'Agente
    with st.chat_message("assistant"):
        history_str = "\n".join([f"{'User' if isinstance(m, HumanMessage) else 'AI'}: {m.content}" for m in st.session_state.messages[:-1]])
        with st.spinner("Analisi mercati e profilo..."):
            answer = st.session_state.agent.run(
                user_input, 
                history_str, 
                json.dumps(st.session_state.profile_data)
            )
            st.markdown(answer)
            st.session_state.messages.append(AIMessage(content=str(answer)))
    
    # Forziamo il refresh finale per mostrare i dati estratti nella sidebar
    st.rerun()
