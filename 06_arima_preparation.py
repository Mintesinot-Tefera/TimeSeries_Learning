
import pandas as pd
import matplotlib.pyplot as plt

# Load the Airline Passengers dataset
df = pd.read_csv("data/airline_passengers.csv")

# Create a date column
df["date"] = pd.to_datetime(
    df["month"] + " " + df["year"].astype(str),
    format="%B %Y"
)

# Sort data chronologically
df = df.sort_values("date")

# Set date as index
df = df.set_index("date")

# Set monthly frequency
df = df.asfreq("MS")

# Extract passenger values
passengers = df["passengers"]

# Display dataset information
print("Dataset shape:", df.shape)

print("\nFirst five observations:")
print(passengers.head())

print("\nLast five observations:")
print(passengers.tail())

# Visualize the original series
plt.figure(figsize=(12, 5))

plt.plot(passengers)

plt.title("Monthly Airline Passengers")
plt.xlabel("Year")
plt.ylabel("Passengers (Thousands)")
plt.grid(True)

plt.tight_layout()
plt.show()
