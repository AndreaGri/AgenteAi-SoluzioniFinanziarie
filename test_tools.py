from tools import get_stock_info

def test_yfinance():
    print("Test recupero dati per NVIDIA (NVDA)...")
    result = get_stock_info.run("NVDA")
    print(f"Risultato: {result}")
    
    if isinstance(result, dict) and "prezzo_attuale" in result:
        print("\n--- TOOL TEST SUCCESS ---")
    else:
        print("\n--- TOOL TEST FAILED ---")

if __name__ == "__main__":
    test_yfinance()
