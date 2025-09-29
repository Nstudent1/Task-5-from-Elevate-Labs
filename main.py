import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV using Pandas
# Make sure the 'sales_data.csv' file is in the same directory as your script.
try:
    df = pd.read_csv('sales_data.csv')
    print("CSV file loaded successfully.")
except FileNotFoundError:
    print("Error: 'sales_data.csv' not found. Please ensure the file is in the correct directory.")
    exit()

# Convert the 'Date' column to datetime objects for proper time-series analysis.
df['Date'] = pd.to_datetime(df['Date'])

# Display the first few rows of the DataFrame to verify it was loaded correctly.
print("\nFirst 5 rows of the sales data:")
print(df.head())
print("\nData types:")
print(df.info())

# 2. Use groupby(), sum(), and plot() for analysis

# Analysis 1: Total Revenue by Product Category
print("\nTotal Revenue by Product Category:")
category_revenue = df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
print(category_revenue)

# Plotting the total revenue by category
plt.figure(figsize=(10, 6))
category_revenue.plot(kind='bar', color='skyblue')
plt.title('Total Revenue by Product Category')
plt.xlabel('Category')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Analysis 2: Total Quantity Sold by Product
print("\nTotal Quantity Sold by Product:")
product_quantity = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print(product_quantity)

# Plotting the total quantity sold by product
plt.figure(figsize=(12, 7))
product_quantity.plot(kind='barh', color='lightgreen')
plt.title('Total Quantity Sold by Product')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Analysis 3: Daily Sales Revenue
print("\nDaily Sales Revenue:")
daily_revenue = df.groupby('Date')['Revenue'].sum()
print(daily_revenue)

# Plotting the daily sales revenue trend
plt.figure(figsize=(14, 7))
daily_revenue.plot(kind='line', marker='o', color='coral')
plt.title('Daily Sales Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Total Revenue ($)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
