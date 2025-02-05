import pandas as pd

# Load the CSV file
file_path = r"D:\AI-Python\CLP2\file\sales_data.csv" 
df = pd.read_csv(file_path)

# Compute total revenue per product
total_revenue = df.groupby("Product")["Revenue"].sum()

# Format and print results
print("\nTotal Revenue by Product:")
print("------------------------")
# Convert to DataFrame and format as currency
revenue_df = total_revenue.to_frame().round(2)
pd.options.display.float_format = '${:,.2f}'.format
print(revenue_df.to_string(header=False))