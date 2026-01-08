import yfinance as yf
from langchain_core.tools import tool
from duckduckgo_search import DDGS

@tool
def web_search(query: str):
    """
    Cerca informazioni aggiornate sul web (es. tassi di interesse, news finanziarie).
    """
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=3)]
            if not results:
                return "Nessun risultato trovato sul web."
            
            formatted_results = ""
            for r in results:
                formatted_results += f"Titolo: {r['title']}\nSnippet: {r['body']}\n\n"
            return formatted_results
    except Exception as e:
        return f"Errore nella ricerca web: {e}. Consiglia all'utente di verificare i tassi sui siti ufficiali delle banche."

@tool
def get_stock_info(ticker: str):
    """
    Ottiene dati finanziari per un ticker azionario (es. AAPL, ISP.MI).
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            "prezzo": info.get("currentPrice"),
            "target": info.get("targetMeanPrice"),
            "raccomandazione": info.get("recommendationKey"),
            "valuta": info.get("currency")
        }
    except Exception as e:
        return f"Errore nel recupero dati per {ticker}: {e}"

financial_tools = [get_stock_info, web_search]
