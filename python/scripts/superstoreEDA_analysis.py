import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ====================== LOAD DATA ======================
print("Loading cleaned data...")
df = pd.read_csv(r'C:\Projects\Superstore_Sales_Analytics\sql\loader\superstore_clean.csv')

print(f"✅ Data Loaded Successfully! Total Rows: {len(df)}")

# Calculate Profit Margin (if not already present)
if 'Profit_Margin' not in df.columns:
    df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100

print("\nColumn Names:", df.columns.tolist())

# ====================== ADVANCED ANALYSIS ======================

print("\n" + "="*60)
print("🔥 ADVANCED BUSINESS INSIGHTS")
print("="*60)

# 1. Top 10 Products by Sales
print("\n1. Top 10 Products by Sales:")
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)

# 2. Top 10 Most Profitable Products
print("\n2. Top 10 Most Profitable Products:")
top_profitable = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
print(top_profitable)

# 3. Sales by Region
print("\n3. Total Sales by Region:")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

# 4. Profit by Category
print("\n4. Total Profit by Category:")
print(df.groupby('Category')['Profit'].sum().sort_values(ascending=False))

# 5. Profit Margin by Category
print("\n5. Average Profit Margin by Category:")
print(df.groupby('Category')['Profit_Margin'].mean().sort_values(ascending=False))

# ====================== VISUALIZATIONS + SAVE AS IMAGES ======================
plt.figure(figsize=(18, 12))

plt.subplot(2, 2, 1)
top_products.plot(kind='barh', color='skyblue')
plt.title('Top 10 Products by Sales')
plt.xlabel('Sales')

plt.subplot(2, 2, 2)
df.groupby('Region')['Sales'].sum().plot(kind='bar', color='lightblue')
plt.title('Total Sales by Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)

plt.subplot(2, 2, 3)
df.groupby('Category')['Profit'].sum().plot(kind='bar', color='green')
plt.title('Total Profit by Category')
plt.ylabel('Profit')
plt.xticks(rotation=45)

plt.subplot(2, 2, 4)
df.groupby('Category')['Profit_Margin'].mean().plot(kind='bar', color='purple')
plt.title('Average Profit Margin by Category')
plt.ylabel('Profit Margin %')
plt.xticks(rotation=45)

plt.tight_layout()

# ==================== SAVE CHARTS AS IMAGES ====================
save_folder = r'C:\Projects\Superstore_Sales_Analytics\python'

plt.savefig(save_folder + r'\sales_visualizations.png', dpi=300, bbox_inches='tight')
plt.savefig(save_folder + r'\sales_visualizations.jpg', dpi=300, bbox_inches='tight')

print("\n✅ Charts Saved Successfully as Images!")
print(f"1. sales_visualizations.png  (High Quality)")
print(f"2. sales_visualizations.jpg")
print(f"Location: {save_folder}")

plt.show()
# ====================== SAVE REPORT ======================
summary = df.groupby(['Region', 'Category']).agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum',
    'Profit_Margin': 'mean'
}).round(2)

summary.to_csv(r'C:\Projects\Superstore_Sales_Analytics\salesEDA_summary_report.csv', index=True)

print("\n✅ Advanced Summary Report Saved Successfully!")
print("Location: C:\\Projects\\Superstore_Sales_Analytics\\salesEDA_summary_report.csv")

print("\n🎉 Advanced Python Analysis Completed!")