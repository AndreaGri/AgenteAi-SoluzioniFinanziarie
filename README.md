# 🏦 Agente Finanziario Intelligente (AI Engineering - Cap. 6)

Questo progetto implementa un **Agente Finanziario Agentico** basato sull'architettura descritta nel libro "AI Engineering". L'applicazione è progettata per operare su GitHub Codespaces e utilizza LLM all'avanguardia per la consulenza finanziaria personalizzata.

## 🚀 Architettura del Sistema
Il sistema segue il pattern **ReAct (Reasoning and Acting)** per minimizzare le allucinazioni e massimizzare l'accuratezza dei dati:

1.  **Core Reasoning**: Llama 3.3-70B (via Groq) gestisce la logica di pensiero e la decisione sull'uso dei tool.
2.  **Dynamic Profiling**: Un modulo di *Information Extraction* (Llama 3.1-8B) analizza la chat in tempo reale per popolare un profilo utente compatibile con la normativa MiFID.
3.  **Tool Integration**:
    *   `Yahoo Finance`: Per dati azionari e ticker.
    *   `DuckDuckGo Search`: Per ricerca tassi bancari e news in tempo reale (Anti-allucinazione).
4.  **State Management**: Streamlit gestisce la persistenza del profilo utente e della cronologia conversazionale.

## 🛠️ Stack Tecnologico
- **Backend**: Python 3.12
- **Orchestrazione**: LangChain-Core (Pattern ReAct manuale per stabilità)
- **LLM**: Groq (Llama 3.3-70B & 3.1-8B)
- **Frontend**: Streamlit
- **Dati**: YFinance & DuckDuckGo Search

## 📦 Installazione e Setup

1. **Clona il repository**:
   ```bash
   git clone <tuo-repo>
   cd AgenteAi-SoluzioniFinanziarie
pip install -r requirements.txt
GROQ_API_KEY=tua_api_key_qui
streamlit run app.py --server.port 8501
Sicurezza e MiFID
L'agente è istruito per:
Identificare la vulnerabilità degli utenti (es. pensionati).
Evitare consigli ad alto rischio per profili conservativi.
Non inventare mai tassi di interesse (obbligo di ricerca web).
Sviluppato seguendo rigorosamente i principi di AI Engineering per applicazioni enterprise.
