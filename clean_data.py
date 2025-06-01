import pandas as pd

# Load the dataset
df = pd.read_csv("marketing_campaign.csv", sep='\t')

# Drop duplicates
df.drop_duplicates(inplace=True)

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Fill missing income with median
if df['Income'].isnull().sum() > 0:
    df['Income'].fillna(df['Income'].median(), inplace=True)

# Convert date column to datetime format
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')

# Standardize text columns
df['Education'] = df['Education'].str.strip().str.lower()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.lower()

# Rename column headers
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Convert data types
df['year_birth'] = df['year_birth'].astype(int)
df['income'] = df['income'].astype(float)

# Save cleaned dataset
df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("✅ Cleaned dataset saved as 'cleaned_marketing_campaign.csv'")
