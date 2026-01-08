from agent import get_financial_agent

def quick_test():
    print("Inizializzazione Agente...")
    try:
        agent = get_financial_agent()
        print("Agente creato. Invio richiesta...")
        res = agent.invoke({
            "input": "Ciao, chi sei?",
            "chat_history": [],
            "profile_context": "Nessun dato disponibile"
        })
        print(f"RISPOSTA: {res['output']}")
        print("\n✅ AGENTE FUNZIONANTE!")
    except Exception as e:
        print(f"\n❌ ERRORE: {e}")

if __name__ == "__main__":
    quick_test()
