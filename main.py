import pandas as pd

file_path = "diabetes_dataset.csv"
df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nZero values:")
print((df == 0).sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nStatistics BEFORE cleaning:")
print(df.describe())

columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

df_clean = df.copy()

df_clean[columns] = df_clean[columns].replace(0, pd.NA)

for column in columns:
    df_clean[column] = df_clean[column].fillna(df_clean[column].median())

df_clean = df_clean.drop_duplicates()

print("\nMissing values AFTER cleaning:")
print(df_clean.isnull().sum())

print("\nDuplicate rows AFTER cleaning:")
print(df_clean.duplicated().sum())

print("\nDataset shape AFTER cleaning:", df_clean.shape)

print("\nStatistics AFTER cleaning:")
print(df_clean.describe())

df_clean.to_csv("diabetes_clean.csv", index=False)

print("\nClean dataset saved!")