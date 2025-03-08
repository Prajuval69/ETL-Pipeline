import requests
import pandas as pd
import sqlite3
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(filename="U:\\vs\\pipeline\\ingestion.log", 
                    level=logging.INFO, 
                    format="%(asctime)s - %(message)s")

# API URL for exchange rates
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# SQLite database path
DB_PATH = "U:\\vs\\pipeline\\finance.db"

def create_database():
    """Create database and table if they don’t exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Currency TEXT,
            Exchange_Rate REAL,
            Date TEXT
        )
    """)

    conn.commit()
    conn.close()
    logging.info("✅ Database and table ensured.")

def fetch_and_store():
    """Fetch exchange rates from API and store them in SQLite."""
    logging.info("🔄 Fetching exchange rates...")

    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)

        data = response.json()
        exchange_rates = data["rates"]

        # Convert API data to Pandas DataFrame
        df = pd.DataFrame(list(exchange_rates.items()), columns=["Currency", "Exchange_Rate"])

        # Add timestamp for historical tracking
        df["Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Connect to SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Check if today's data already exists
        cursor.execute("SELECT COUNT(*) FROM exchange_rates WHERE Date LIKE ?", 
                       (datetime.now().strftime("%Y-%m-%d") + "%",))
        count = cursor.fetchone()[0]

        if count == 0:
            # Append new data (store historical rates)
            df.to_sql("exchange_rates", conn, if_exists="append", index=False)
            logging.info("✅ Exchange rates successfully stored in SQLite!")
        else:
            logging.info("⚠️ Today's exchange rates already exist. Skipping update.")

        conn.commit()
        conn.close()

    except Exception as e:
        logging.error(f"❌ Error fetching/storing data: {e}")

# Run the functions
create_database()
fetch_and_store()
print(df)