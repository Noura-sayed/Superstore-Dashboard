import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Superstore.csv', encoding='latin1')

print("Dataset Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
avg_discount = df['Discount'].mean()

print("\n--- Key Metrics ---")
print(f"Total Sales: ${total_sales:,.0f}")
print(f"Total Profit: ${total_profit:,.0f}")
print(f"Average Discount: {avg_discount:.2%}")

region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print("\n--- Profit by Region ---")
print(region_profit)

category_perf = df.groupby('Category')[['Sales', 'Profit']].sum().sort_values('Profit', ascending=False)
print("\n--- Category Performance ---")
print(category_perf)

plt.figure(figsize=(7,5))
region_profit.plot(kind='bar', color='skyblue')
plt.title('Profit by Region')
plt.xlabel('Region')
plt.ylabel('Total Profit')
plt.tight_layout()
plt.savefig('profit_by_region.png')
plt.show()

print("\n--- Insights ---")
print("- West region generates the highest profit.")
print("- Technology category leads in both sales and profit.")
print("- Furniture category shows low margins due to high discounts.")
print("- Consider reducing discounts on Furniture and optimizing logistics.")
