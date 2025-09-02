#Extract
import mysql.connector
import pandas as pd

con = mysql.connector.connect(host='localhost', user='root', password='root', database='superstore_db')

query = 'select * from superstore_dataset'

df = pd.read_sql_query(query, con)
print(df.head())

#Transform
import numpy as np

df = df.dropna()

df["Revenue"] = df["Sales"] * df["Quantity"]

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

df["ProfitFlag"] = np.where(df["Profit"] > 0, "High Profit", "Low Profit")

#Load
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transformed_ds (
    OrderID VARCHAR(20),
    CustomerName VARCHAR(100),
    Category VARCHAR(50),
    SubCategory VARCHAR(50),
    Sales FLOAT,
    Quantity INT,
    Revenue FLOAT,
    Profit FLOAT,
    ProfitFlag VARCHAR(20),
    Region VARCHAR(50),
    OrderDate DATE,
    Year INT,
    Month INT
);
""")

for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO transformed_ds (
            OrderID, CustomerName, Category, SubCategory, Sales, Quantity,
            Revenue, Profit, ProfitFlag, Region, OrderDate, Year, Month
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row["Order ID"],
        row["Customer Name"],
        row["Category"],
        row["Sub-Category"],
        row["Sales"],
        row["Quantity"],
        row["Revenue"],
        row["Profit"],
        row["ProfitFlag"],
        row["Region"],
        row["Order Date"],
        row["Year"],
        row["Month"]
    ))

con.commit()
con.close()