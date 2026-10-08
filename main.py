import pandas as pd

# 1. Load dataset
file_path = "diabetes_dataset.csv"
df = pd.read_csv(file_path)

# 2. Basic information
print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# 3. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Check zeros
print("\nZero values:")
print((df == 0).sum())

# 5. Check duplicates
print("\nDuplicate rows:", df.duplicated().sum())

# 6. Check statistics BEFORE cleaning
print("\nStatistics BEFORE cleaning:")
print(df.describe())

# 7. Clean invalid zeros
columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

df_clean = df.copy()

df_clean[columns] = df_clean[columns].replace(0, pd.NA)

# Fill missing values with median
for column in columns:
    df_clean[column] = df_clean[column].fillna(df_clean[column].median())

# Remove duplicate rows
df_clean = df_clean.drop_duplicates()

# 8. Check AFTER cleaning
print("\nMissing values AFTER cleaning:")
print(df_clean.isnull().sum())

print("\nDuplicate rows AFTER cleaning:")
print(df_clean.duplicated().sum())

print("\nDataset shape AFTER cleaning:", df_clean.shape)

# 9. Statistics AFTER cleaning
print("\nStatistics AFTER cleaning:")
print(df_clean.describe())

# 10. Save clean dataset
df_clean.to_csv("diabetes_clean.csv", index=False)

print("\nClean dataset saved!")