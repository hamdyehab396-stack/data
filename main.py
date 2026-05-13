import pandas as pd
from line import line_chart as l
from bar import bar_chart as b
from pie import pie_chart as p
df = pd.read_csv("messy_sales_data.csv")
df = df.drop_duplicates()
df = df.fillna({"city": "Unknown",
                "price": 0,
                "quantity": 0,
                "product": "Unknown",
                "customer_name": "Unknown",
                "order_id": 0})
df["city"] = df["city"].str.title()
df["customer_name"] = df["customer_name"].str.title()
df["price"] = df["price"].abs()
df['order_date'] = pd.to_datetime(df['order_date'], format="mixed", errors='coerce')
df['order_date'] = df['order_date'].fillna(pd.Timestamp('1900-01-01'))
df["product"] = df["product"].str.title()
df["product"] = df["product"].str.strip()
df["price"] = pd.to_numeric(df["price"], errors="coerce")
total_sales = df["price"].sum()
top_product = df.groupby("product")["quantity"].sum().idxmax()
avg_price = df["price"].mean()
top_city = df.groupby("city")["price"].sum().idxmax()
top_5_product = df.groupby("product")["quantity"].sum().sort_values(ascending=False).iloc[0:5]
df["month"]= df["order_date"].dt.month
sales_by_month = df.groupby("month")["price"].sum()
print(sales_by_month)
with open("report.txt", "w", encoding="UTF-8") as f:
    f.write("sales anlaysis report\n")
    f.write("======================\n\n")
    f.write(f"total sales: {total_sales}\n")
    f.write(f"top product: {top_product}\n")
    f.write(f"avg price: {avg_price}\n")
    f.write(f"top city: {top_city}\n")
l(sales_by_month, "Sales Per Month", "Month", "Sales")    
   

