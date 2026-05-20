import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# ====================== LOAD DATA ======================
print("Loading cleaned data...")

df = pd.read_csv(r'C:\Projects\Superstore_Sales_Analytics\sql\loader\superstore_clean.csv')

print(f"✅ Data Loaded Successfully! Total Rows: {len(df)}")

# Calculate Profit Margin (if not present)
if 'Profit_Margin' not in df.columns:
    df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100

print("\nExact Column Names:")
print(df.columns.tolist())

# ====================== ANALYSIS ======================
print("\n=== Total Sales by Region ===")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

print("\n=== Total Profit by Category ===")
print(df.groupby('Category')['Profit'].sum().sort_values(ascending=False))

print("\n=== Average Profit Margin by Category ===")
print(df.groupby('Category')['Profit_Margin'].mean().sort_values(ascending=False))

# ====================== VISUALIZATIONS ======================
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
df.groupby('Region')['Sales'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Sales by Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)

plt.subplot(2, 2, 2)
df.groupby('Category')['Profit'].sum().plot(kind='bar', color='green')
plt.title('Total Profit by Category')
plt.ylabel('Profit')
plt.xticks(rotation=45)

plt.subplot(2, 2, 3)
sns.histplot(df['Profit_Margin'], kde=True, color='purple')
plt.title('Profit Margin Distribution')

plt.tight_layout()
plt.show()

# ====================== SAVE SUMMARY REPORT ======================
summary = df.groupby(['Region', 'Category']).agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum',
    'Profit_Margin': 'mean'
}).round(2)

# Save in main project folder
save_path = r'C:\Projects\Superstore_Sales_Analytics\sales_summary_report.csv'

summary.to_csv(save_path, index=True)

print("\n✅ Summary Report Saved Successfully!")
print(f"Saved Location: {save_path}")
print("You can now open this file in Excel.")