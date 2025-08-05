import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('data/processed/clinvar_cleaned.csv')

# Separate label
y = df['label']
X = df.drop(columns=['label'])

# Optionally drop non-useful fields like 'POS' if you think it adds noise
X = X.drop(columns=['POS'])

# One-hot encode categorical columns
X_encoded = pd.get_dummies(X, columns=['GENE', 'MC', 'CLNVC', 'CLNREVSTAT'])

# Add label back
X_encoded['label'] = y

# Save to CSV
X_encoded.to_csv('data/processed/clinvar_encoded.csv', index=False)
print(f"Encoded dataset saved with {X_encoded.shape[0]} rows and {X_encoded.shape[1]} columns.")
