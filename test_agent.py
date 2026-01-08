from agent import get_financial_agent
from profile_manager import UserProfile, format_profile_for_prompt

def test_agent_behavior():
    agent_executor = get_financial_agent()
    
    # Simuliamo un profilo vuoto
    empty_profile = UserProfile()
    context = format_profile_for_prompt(empty_profile)
    
    print("\n--- TEST 1: Richiesta consigli senza profilo ---")
    response = agent_executor.invoke({
        "input": "Ciao, quali azioni mi consigli di comprare oggi?",
        "chat_history": [],
        "profile_context": context
    })
    print(f"Risposta Agente: {response['output']}")
    
    # Verifica se l'agente sta facendo domande invece di dare consigli
    if "reddito" in response['output'].lower() or "rischio" in response['output'].lower() or "età" in response['output'].lower():
        print("\n✅ RISULTATO: L'agente ha correttamente identificato la mancanza di dati MiFID.")
    else:
        print("\n❌ RISULTATO: L'agente ha risposto senza profilazione (ERRORE).")

if __name__ == "__main__":
    test_agent_behavior()
