import pandas as pd
from pathlib import Path

# Dataset source
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"

# Load dataset
df = pd.read_csv(url)

# Create data directory if it does not exist
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Save dataset locally
output_path = data_dir / "airline_passengers.csv"
df.to_csv(output_path, index=False)

print("Dataset downloaded successfully!")
print(f"Saved to: {output_path}")

print("\nFirst five records:")
print(df.head())

print("\nDataset shape:")
print(df.shape)
