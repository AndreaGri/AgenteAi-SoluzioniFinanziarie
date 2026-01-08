import os
import json
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from tools import financial_tools

load_dotenv()

class FinancialAgent:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0, # Temperatura zero per massima precisione
            model_name="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        self.tools = {t.name: t for t in financial_tools}

    def run(self, user_input, chat_history, profile_context):
        system_prompt = f"""Sei un Senior Financial Advisor MiFID certificato.
        
REGOLE ANTI-ALLUCINAZIONE:
1. NON citare mai tassi di interesse, nomi di banche o prodotti specifici basandoti sulla tua memoria.
2. Se l'utente chiede "quale banca" o "migliori tassi", DEVI usare obbligatoriamente il tool 'web_search'.
3. Se il tool non restituisce dati chiari, ammetti di non saperlo e suggerisci all'utente di consultare i fogli informativi ufficiali.
4. I Buoni Fruttiferi Postali sono emessi SOLO da Cassa Depositi e Prestiti e distribuiti da Poste Italiane. Non confondere mai le banche con Poste.

PROFILO UTENTE: {profile_context}

FORMATO OBBLIGATORIO:
Thought: Devo cercare i tassi aggiornati perché non posso inventarli.
Action: web_search
Action Input: [query di ricerca specifica in italiano]
Observation: [risultato della ricerca]
...
Final Answer: [Risposta basata ESCLUSIVAMENTE sui dati dell'Observation]
"""
        current_prompt = f"{system_prompt}\n\nSTORIA:\n{chat_history}\n\nUser: {user_input}\n"
        
        for i in range(5):
            res = self.llm.invoke(current_prompt)
            text = res.content
            
            # Se il modello prova a rispondere senza usare tool per una domanda sui tassi
            if "Final Answer:" in text and ("%" in text or "banca" in text.lower()) and i == 0:
                current_prompt += f"\n{text}\nThought: Ho fornito dati senza verificare. Devo usare web_search per essere preciso.\n"
                continue

            if "Final Answer:" in text:
                return text.split("Final Answer:")[-1].strip()
            
            action_m = re.search(r"Action:\s*(.*)", text)
            input_m = re.search(r"Action Input:\s*(.*)", text)
            
            if action_m and input_m:
                action = action_m.group(1).strip()
                action_input = input_m.group(1).strip().strip('"').strip("'")
                
                if action in self.tools:
                    print(f"--- ESECUZIONE TOOL: {action} ---")
                    obs = self.tools[action].invoke(action_input)
                    current_prompt += f"\n{text}\nObservation: {obs}\nThought: "
                    continue
            
            if i == 4: # Se arriviamo alla fine senza Final Answer
                return text

        return "Mi dispiace, non sono riuscito a verificare i tassi attuali. Per sicurezza, ti consiglio di consultare il sito di Poste Italiane per i Buoni Fruttiferi o portali come Segugio.it per i conti deposito."

def extract_user_data(text, current_profile):
    from langchain_groq import ChatGroq
    llm = ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"), temperature=0)
    prompt = f"Estrai dati finanziari (eta, reddito, risparmi, rischio) in JSON. Testo: {text}. Attuali: {current_profile}."
    try:
        res = llm.invoke(prompt)
        match = re.search(r"\{.*\}", res.content, re.DOTALL)
        if match:
            new_data = json.loads(match.group())
            updated = current_profile.copy()
            for k in ["eta", "reddito", "risparmi", "rischio"]:
                if k in new_data and new_data[k] not in [None, "Non nota", "Non noto"]:
                    updated[k] = new_data[k]
            return updated
        return current_profile
    except: return current_profile
