import pandas as pd
import kagglehub
import os

path = kagglehub.dataset_download("pauloarruda/customer-personality-analysis")
df = pd.read_csv(os.path.join(path, "marketing_campaign.csv"), sep="\t")

print(f"Shape: {df.shape}")
print(df.isnull().sum())
print(df.describe())

before = len(df)
df = df.drop_duplicates()
print(f"Duplicates Removed: {before - len(df)}")

numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

text_cols = df.select_dtypes(include='object').columns
df[text_cols] = df[text_cols].fillna("Unknown")
df[text_cols] = df[text_cols].apply(lambda col: col.str.strip().str.title())

if 'Dt_Customer' in df.columns:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], dayfirst=True)

if 'Year_Birth' in df.columns:
    df['Age'] = 2025 - df['Year_Birth']

def remove_outliers(df, col):
    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    IQR = Q3 - Q1
    return df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

for col in ['Income', 'Age']:
    if col in df.columns:
        df = remove_outliers(df, col)

print(f"Final Shape: {df.shape}")
print(f"Missing Values: {df.isnull().sum().sum()}")

df.to_csv("cleaned_dataset.csv", index=False)
print("Saved as cleaned_dataset.csv")
