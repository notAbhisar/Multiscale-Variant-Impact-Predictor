import pandas as pd

df = pd.read_csv('data/processed/clinvar_features.csv')

# Normalize labels
def normalize_label(clnsig):
    clnsig = str(clnsig).lower()
    if 'pathogenic' in clnsig:
        return 1
    elif 'benign' in clnsig:
        return 0
    else:
        return None  # uncertain, conflicting, etc.

df['label'] = df['CLNSIG'].apply(normalize_label)

# Drop rows with missing label or essential features
df = df.dropna(subset=['label', 'GENE', 'MC'])

# Optional: drop CLNSIG column if you just want to keep label
# df = df.drop(columns=['CLNSIG'])

df.to_csv('data/processed/clinvar_cleaned.csv', index=False)
print(f"Saved cleaned data with {len(df)} rows.")