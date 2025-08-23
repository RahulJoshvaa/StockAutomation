import psycopg2
from data_fetch import fetchStock
import os 
from dotenv import load_dotenv
import time
load_dotenv()
def insert_stock():
    try:
        # Connection to Postgres
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            port=os.getenv("DB_PORT")
        )
        cur = conn.cursor()

        # Insert query
        insert_query = """
        INSERT INTO stocks (stock_name, open, high, low, close)
        VALUES (%s, %s, %s, %s, %s);
        """
        # data = fetchStock()
        # values = (
        #     data["StockName"],
        #     data["Open"],
        #     data["High"],
        #     data["Low"],
        #     data["Close"]
        # )
        values = (
            "StockName",
            "120",
            "125",
            "118",
            "124"
        )

        cur.execute(insert_query, values)
        conn.commit()   # save changes

        print("✅ Data inserted successfully")

        cur.close()
        conn.close()

    except Exception as e:
        print("❌ Error:", e)
i = 0
while i < 5:
    insert_stock()
    time.sleep(5)
    i += 1