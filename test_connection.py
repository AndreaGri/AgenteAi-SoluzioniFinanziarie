import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def test_llm():
    # Utilizziamo il modello più recente disponibile su Groq
    MODEL = "llama-3.3-70b-versatile" 
    
    try:
        llm = ChatGroq(
            temperature=0,
            model_name=MODEL,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        response = llm.invoke("Ciao, sono l'ingegnere di sistema. Conferma la tua operatività.")
        print("\n--- TEST SUCCESS ---")
        print(f"Modello Utilizzato: {MODEL}")
        print(f"Risposta LLM: {response.content}")
        return True
    except Exception as e:
        print("\n--- TEST FAILED ---")
        print(f"Errore: {e}")
        return False

if __name__ == "__main__":
    test_llm()
