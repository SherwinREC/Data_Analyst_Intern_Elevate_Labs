import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

path = kagglehub.dataset_download("ishanshrivastava28/superstore-sales")
df = pd.read_csv(os.path.join(path, "Superstore_Sales.csv"), encoding='latin1')

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Month-Year'] = df['Order Date'].dt.to_period('M').astype(str)
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Quarter'] = df['Order Date'].dt.quarter
df['Day of Week'] = df['Order Date'].dt.day_name()
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Profit Margin %'] = round((df['Profit'] / df['Sales']) * 100, 2)
df['Revenue per Unit'] = round(df['Sales'] / df['Quantity'], 2)
df['Profit Status'] = df['Profit'].apply(lambda x: 'Profitable' if x > 0 else 'Loss')
df['Discount Band'] = pd.cut(df['Discount'], bins=[-1, 0, 0.2, 0.4, 1.0],
                              labels=['No Discount', 'Low', 'Medium', 'High'])

df = df[df['Sales'] > 0].drop_duplicates()

print(df.shape)
print(df.isnull().sum())
print(df[['Sales', 'Profit', 'Quantity', 'Discount', 'Shipping Days']].describe())
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))
print(df.groupby('Category')[['Sales', 'Profit']].sum())
print(df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head())
print(df.groupby('Year')['Sales'].sum())
print(round(df['Shipping Days'].mean(), 2))
print(round((df['Profit'].sum() / df['Sales'].sum()) * 100, 2))

monthly_sales = df.groupby('Month-Year')['Sales'].sum().reset_index()
plt.figure(figsize=(14, 5))
plt.plot(monthly_sales['Month-Year'], monthly_sales['Sales'], marker='o', color='steelblue')
plt.title("Monthly Sales Trend")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

df.groupby('Region')['Sales'].sum().sort_values().plot(kind='barh', color='coral', figsize=(8, 5))
plt.title("Sales by Region")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

df.groupby('Category')['Profit'].sum().sort_values().plot(kind='barh', color='seagreen', figsize=(8, 5))
plt.title("Profit by Category")
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()

df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).plot(kind='bar', color='mediumpurple', figsize=(10, 5))
plt.title("Sales by Sub-Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_by_subcategory.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='Discount', y='Profit', hue='Category', data=df, alpha=0.6)
plt.title("Discount vs Profit")
plt.tight_layout()
plt.savefig("discount_vs_profit.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Year', y='Sales', data=df, palette='Set2')
plt.title("Sales Distribution by Year")
plt.tight_layout()
plt.savefig("sales_by_year.png")
plt.show()

df.groupby('Quarter')['Sales'].sum().plot(kind='bar', color='darkorange', figsize=(8, 5))
plt.title("Sales by Quarter")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_quarter.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.heatmap(df[['Sales', 'Profit', 'Quantity', 'Discount', 'Shipping Days', 'Profit Margin %']].corr(),
            annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

df[[
    'Order Date', 'Ship Date', 'Month-Year', 'Year', 'Month', 'Quarter',
    'Day of Week', 'Shipping Days', 'Region', 'Category', 'Sub-Category',
    'Sales', 'Profit', 'Quantity', 'Discount', 'Profit Margin %',
    'Revenue per Unit', 'Profit Status', 'Discount Band'
]].to_csv("Cleaned_Superstore_Sales.csv", index=False)

print("Saved as Cleaned_Superstore_Sales.csv")
