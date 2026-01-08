from pydantic import BaseModel, Field
from typing import Optional

class UserProfile(BaseModel):
    eta: Optional[int] = None
    reddito_annuo: Optional[float] = None
    budget_investimento: Optional[float] = None
    conoscenza_settore: Optional[str] = None # Es: Principiante, Intermedio, Avanzato
    propensione_rischio: Optional[str] = None # Es: Bassa, Media, Alta
    obiettivo: Optional[str] = None # Es: Pensione, Speculazione, Risparmio

    def is_complete(self) -> bool:
        fields = [self.eta, self.reddito_annuo, self.budget_investimento, 
                  self.conoscenza_settore, self.propensione_rischio, self.obiettivo]
        return all(f is not None for f in fields)

    def get_missing_fields(self):
        missing = []
        if not self.eta: missing.append("Età")
        if not self.reddito_annuo: missing.append("Reddito Annuo")
        if not self.budget_investimento: missing.append("Budget da Investire")
        if not self.conoscenza_settore: missing.append("Livello di conoscenza finanziaria")
        if not self.propensione_rischio: missing.append("Tolleranza al rischio (MiFID)")
        if not self.obiettivo: missing.append("Obiettivo finanziario")
        return missing

def format_profile_for_prompt(profile: UserProfile):
    return f"""
    PROFILO UTENTE ATTUALE:
    - Età: {profile.eta or 'Sconosciuta'}
    - Reddito: {profile.reddito_annuo or 'Sconosciuto'}
    - Budget: {profile.budget_investimento or 'Sconosciuto'}
    - Rischio: {profile.propensione_rischio or 'Sconosciuto'}
    - Esperienza: {profile.conoscenza_settore or 'Sconosciuta'}
    """
