ETL Pipeline: Financial Transactions Data Processing

📌 Project Overview

This project is an ETL (Extract, Transform, Load) pipeline built using Python, Pandas, and SQLite. It automates the ingestion, transformation, and storage of financial transactions data and integrates with an external API to fetch real-time exchange rates.

🚀 Features

Extracts financial transactions from a CSV file.

Cleans and transforms data using Pandas.

Stores processed data into an SQLite database.

Fetches real-time exchange rates from an external API.

Automates data ingestion using Windows Task Scheduler.

🛠️ Tech Stack

Programming Language: Python

Libraries: Pandas, SQLite3, Requests

Database: SQLite

Automation: Windows Task Scheduler

Version Control: Git & GitHub

🔧 Setup Instructions

1️⃣ Install Dependencies

Ensure you have Python 3+ installed, then run:

pip install -r requirements.txt

2️⃣ Configure API (Optional)

If fetching exchange rates, update config.json with your API key.

3️⃣ Run the ETL Pipeline

python first.py

4️⃣ Automate with Windows Task Scheduler

Open Task Scheduler (taskschd.msc).

Create a new task:

Trigger: Daily or Hourly

Action: Run "C:\Users\praju\AppData\Local\Programs\Python\Python312\python.exe"

Arguments: "U:\vs\pipeline\first.py"

Save and enable the task.
