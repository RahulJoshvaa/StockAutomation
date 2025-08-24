import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

def fetchStock():
    symbol = "AAPL"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()


        if "Time Series (Daily)" not in data:
            return {"Error": data.get("Note", data.get("Error Message", "No data returned"))}

        latest_date = list(data["Time Series (Daily)"].keys())[0]
        latest_data = data["Time Series (Daily)"][latest_date]

        dataDictionary = {
            'StockName': 'Apple',
            'Open': float(latest_data.get('1. open', 0)),
            'High': float(latest_data.get('2. high', 0)),
            'Low': float(latest_data.get('3. low', 0)),
            'Close': float(latest_data.get('4. close', 0))
        }

        return dataDictionary

    except Exception as e:
        return {"Error from data_fetch": str(e)}



