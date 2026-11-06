import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)



amazon=pd.read_csv("amazon.csv")
print(amazon.shape)
print(amazon.head())
print(amazon.info())
print(amazon.describe())


print(amazon.isnull().sum)
print(amazon.drop_duplicates())

print("--------------------------------------------------------------------------------------------")
# ── SALES ANALYSIS ──────────────────────────────

# Convert OrderDate to datetime
amazon['OrderDate'] = pd.to_datetime(amazon['OrderDate'])

#  Month and Year
amazon['Month'] = amazon['OrderDate'].dt.month
amazon['Year'] = amazon['OrderDate'].dt.year
amazon['MonthYear'] = amazon['OrderDate'].dt.to_period('M')

# Total Earnings
print("Total Revenue:", amazon['TotalAmount'].sum())

# Monthly Earnings
monthly_sales = amazon.groupby('MonthYear')['TotalAmount'].sum()
print(monthly_sales)
print("---------------------------------------------------------------------------------------------")


# ── PRODUCT ANALYSIS ────────────────────────────

# Top 5 Categories by Revenue
top_categories = amazon.groupby('Category')['TotalAmount'].sum().sort_values(ascending=False).head(5)
print("Top 5 Categories by Revenue:")
print(top_categories)

# Top 5 Brands by Revenue
top_brands = amazon.groupby('Brand')['TotalAmount'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Brands by Revenue:")
print(top_brands)

# Top 5 Best Selling Products
top_products = amazon.groupby('ProductName')['Quantity'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Best Selling Products :")
print(top_products)

print("--------------------------------------------------------------------------------------------------------")

# ── CUSTOMER ANALYSIS ───────────────────────────

# Top 5 Customers by Revenue
top_customers = amazon.groupby('CustomerName')['TotalAmount'].sum().sort_values(ascending=False).head(5)
print("Top 5 Customers by Revenue:")
print(top_customers)

# Payment Method breakdown
payment_counts = amazon['PaymentMethod'].value_counts()
print("\nPayment Method Breakdown:")
print(payment_counts)

# ── ORDER ANALYSIS ──────────────────────────────

# Order Status breakdown
order_status = amazon['OrderStatus'].value_counts()
print("\nOrder Status Breakdown:")
print(order_status)

# Cancellation rate
cancel_rate = (amazon['OrderStatus'] == 'Cancelled').sum() / len(amazon) * 100
print(f"\nCancellation Rate: {cancel_rate:.2f}%")
print("----------------------------------------------------------------------------------------------")


# ── COUNTRY AND STATE ANALYSIS ─────────────────────────

# Top 5 Countries by Revenue
top_countries = amazon.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False)
print("Revenue by Country:")
print(top_countries)

# Top 5 States by Revenue
top_states = amazon.groupby('State')['TotalAmount'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 States by Revenue:")
print(top_states)

# Top 5 Cities by Revenue
top_cities = amazon.groupby('City')['TotalAmount'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Cities by Revenue:")
print(top_cities)
print("-------------------------------------------------------------------------------------------------------")


# Chart 1 - LINE CHART FOR MONTHLY SALES
plt.figure(figsize=(16, 5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, color='blue', linewidth=1.5)
plt.title('Monthly Sales Revenue (2020-2024)')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('monthly_sales.png')
plt.show()



# Chart 2 - Bar Chart FOR CATEGORIES
plt.figure(figsize=(8, 5))
plt.bar(top_categories.index, top_categories.values, color='orange')
plt.title('Top 5 Categories by Revenue')
plt.xlabel('Category')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.savefig('top_categories.png')
plt.show()


# Chart 3 -Bar Chart FOR BRRANDS
plt.figure(figsize=(8, 5))
plt.bar(top_brands.index, top_brands.values, color='green')
plt.title('Top 5 Brands by Revenue')
plt.xlabel('Brand')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.savefig('top_brands.png')
plt.show()


# Chart 4 - Pie Chart For PAYMENTS METHODS
plt.figure(figsize=(7, 7))
plt.pie(payment_counts.values, labels=payment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Payment Method Breakdown')
plt.tight_layout()
plt.savefig('payment_methods.png')
plt.show()


# Chart 5 - Pie Chart For ORDER STATUS
plt.figure(figsize=(7, 7))
plt.pie(order_status.values, labels=order_status.index, autopct='%1.1f%%', startangle=140)
plt.title('Order Status Breakdown')
plt.tight_layout()
plt.savefig('order_status.png')
plt.show()


# Chart 6 - Top 5 Countries Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(top_countries.index, top_countries.values, color='purple')
plt.title('Revenue by Country')
plt.xlabel('Country')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.savefig('top_countries.png')
plt.show()

# Chart 7 - Top 5 Cities Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(top_cities.index, top_cities.values, color='red')
plt.title('Top 5 Cities by Revenue')
plt.xlabel('City')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.savefig('top_cities.png')
plt.show()

print("ALL CHARTS ARE PROVIDED FOR ANALYSIS")