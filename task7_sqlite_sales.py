import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS sales")
cursor.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")

data = [
    ("Laptop", 5, 700),
    ("Laptop", 3, 750),
    ("Phone", 10, 300),
    ("Phone", 6, 280),
    ("Tablet", 4, 250),
    ("Tablet", 7, 230),
    ("Headphones", 12, 50),
    ("Headphones", 8, 55)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", data)
conn.commit()

query = """
SELECT 
    product,
    SUM(quantity) AS total_qty,
    ROUND(AVG(price), 2) AS avg_price,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
"""

df = pd.read_sql_query(query, conn)
conn.close()

print(df)
print(f"\nTotal Revenue: {df['revenue'].sum()}")
print(f"Best Selling Product: {df.loc[df['total_qty'].idxmax(), 'product']}")
print(f"Highest Revenue Product: {df.loc[df['revenue'].idxmax(), 'product']}")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].bar(df['product'], df['revenue'], color='steelblue')
axes[0].set_title("Revenue by Product")
axes[0].set_xlabel("Product")
axes[0].set_ylabel("Revenue")
axes[0].tick_params(axis='x', rotation=45)

axes[1].bar(df['product'], df['total_qty'], color='coral')
axes[1].set_title("Total Quantity Sold by Product")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Quantity")
axes[1].tick_params(axis='x', rotation=45)

axes[2].bar(df['product'], df['avg_price'], color='seagreen')
axes[2].set_title("Average Price by Product")
axes[2].set_xlabel("Product")
axes[2].set_ylabel("Avg Price")
axes[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
