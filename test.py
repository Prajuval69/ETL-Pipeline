import sqlite3
import pandas as pd

DB_PATH = "U:\\vs\\pipeline\\finance.db"

# Connect to database
conn = sqlite3.connect(DB_PATH)

# Read the data into a Pandas DataFrame
df = pd.read_sql("SELECT * FROM exchange_rates ORDER BY Date DESC", conn)

# Print the data
print(df)

conn.close()
