import pandas as pd

# Read CSV file
file_path = r"D:\AI-Python\CLP2\file\dataset.csv"
# Read CSV file into DataFrame
df = pd.read_csv(file_path)

# Display original data
print("Original DataFrame:")
print(df.to_string(index=False))

# Calculate column-wise means (excluding 'id' column)
means = df.drop('id', axis=1).mean(numeric_only=True)

# Fill missing values with column means
df_filled = df.fillna(means)

# Display filled DataFrame
print("\nDataFrame after filling missing values:")
print(df_filled.to_string(index=False))