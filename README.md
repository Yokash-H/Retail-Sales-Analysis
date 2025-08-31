# Retail Sales Analysis
ETL pipeline for retail sales data using Python, Pandas, and MySQL  

This is a simple **ETL project** I built to learn data engineering concepts.  
It takes sales data, cleans & transforms it using **Python + Pandas**, and then loads it into **MySQL** for analysis.  

## What it does
- Extracts data from MySQL  
- Transforms it (adds Revenue, Profit, Flags, Year, Month)  
- Loads the cleaned data back into MySQL  

## Tech used
- Python  
- Pandas  
- MySQL  

Run it
1. Clone the repo  
2. Install requirements → `pip install -r requirements.txt`  
3. Update your DB credentials in `Extract.py`  
4. Run → `python ETL/Extract.py`  

Just a small step towards real-world **data pipelines**
