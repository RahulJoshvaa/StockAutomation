import yfinance as yf

def fetchStock():
    ticker = yf.Ticker("RELIANCE.NS")
    try:
        #1d in both so that just 1 row is returned
        data = ticker.history(period="1d", interval="1d")
        if not data.empty:
            dataDictionary = {
                'StockName': 'Reliance',
                'Open': data['Open'].iloc[0],
                'High': data['High'].iloc[0],
                'Low': data['Low'].iloc[0],
                'Close': data['Close'].iloc[0]
            }
            return dataDictionary
        else:
            return {"Error": "No data returned"}
    except Exception as e:
        return {"Error": str(e)}

