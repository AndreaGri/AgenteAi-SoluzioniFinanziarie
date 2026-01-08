try:
    from agent import get_financial_agent
    print("✅ Importazione riuscita! AgentExecutor trovato.")
except Exception as e:
    print(f"❌ Errore persistente: {e}")
