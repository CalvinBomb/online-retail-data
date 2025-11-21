import pandas as pd
import os

# Full paths to your CSVs
file1 = r"C:\Users\bucky\OneDrive\Desktop\online-retail-analytics data\data\raw\online_retail_2009_2010.csv"
file2 = r"C:\Users\bucky\OneDrive\Desktop\online-retail-analytics data\data\raw\online_retail_2010_2011.csv"

# Check if files exist
if not os.path.exists(file1):
    print(f"File not found: {file1}")
if not os.path.exists(file2):
    print(f"File not found: {file2}")

# Load CSVs
print("Loading first CSV...")
df1 = pd.read_csv(file1, encoding='ISO-8859-1')
print(f"First CSV loaded, shape: {df1.shape}")

print("Loading second CSV...")
df2 = pd.read_csv(file2, encoding='ISO-8859-1')
print(f"Second CSV loaded, shape: {df2.shape}")

# Combine
df = pd.concat([df1, df2], ignore_index=True)
print(f"Combined dataframe shape: {df.shape}")

# Clean data
df = df.dropna(subset=["Customer ID"])
df = df[df["Quantity"] > 0]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["TotalPrice"] = df["Quantity"] * df["Price"]
df["InvoiceYearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# Save cleaned CSV
output_path = r"C:\Users\bucky\OneDrive\Desktop\online-retail-analytics data\data\processed\cleaned_online_retail.csv"
df.to_csv(output_path, index=False)
print(f"Cleaned CSV saved at: {output_path}")
