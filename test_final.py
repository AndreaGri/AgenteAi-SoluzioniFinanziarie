try:
    from agent import get_financial_agent
    from langchain_core.prompts import PromptTemplate
    print("✅ TUTTI GLI IMPORT SONO CORRETTI!")
    print("Inizializzazione agente...")
    agent = get_financial_agent()
    print("✅ AGENTE PRONTO!")
except Exception as e:
    print(f"❌ ERRORE: {e}")
