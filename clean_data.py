# clean_data.py

import pandas as pd

# Load the data (replace with your own file or use sample_data.csv)
df = pd.read_csv("sample_data.csv")

# Show original info
print("\nOriginal Data Info:")
print(df.info())
print("\nFirst few rows:")
print(df.head())

# Step 1: Drop duplicates
df = df.drop_duplicates()

# Step 2: Handle missing values (example: fill with median or drop)
df = df.fillna(df.median(numeric_only=True))

# Step 3: Convert data types if needed (example: convert 'date' column)
# df['date'] = pd.to_datetime(df['date'])

# Step 4: Rename columns to lowercase and replace spaces
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 5: Export cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved as 'cleaned_data.csv'")
