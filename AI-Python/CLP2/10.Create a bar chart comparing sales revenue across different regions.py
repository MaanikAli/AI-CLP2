import pandas as pd
import matplotlib.pyplot as plt

# Load CSV and clean column names
file_path = r"D:\AI-Python\CLP2\file\sales_data2.csv"
df = pd.read_csv(file_path, encoding="utf-8")
df.columns = df.columns.str.strip()  # Remove extra spaces

# Ensure Region and Revenue exist
if "Region" not in df.columns or "Revenue" not in df.columns:
    print("Error: 'Region' or 'Revenue' column not found in CSV.")
    print("Available columns:", df.columns)
else:
    # Convert Revenue to numeric
    df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")

    # Drop missing values
    df = df.dropna(subset=["Region", "Revenue"])

    # Compute total revenue per region
    total_revenue_per_region = df.groupby("Region")["Revenue"].sum()

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    total_revenue_per_region.plot(kind='bar', color='skyblue', edgecolor="black")
    plt.title('Total Sales Revenue by Region', fontsize=14, fontweight='bold')
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Total Revenue', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    # Save the plot
    output_path = r"D:\AI-Python\CLP2\file\total_revenue_by_region.png"
    plt.savefig(output_path, dpi=300)
    
    # Show the plot
    plt.show()
    
    print("Bar chart created and saved to", output_path)
