import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/airline_passengers.csv")

# Convert year and month into a proper date
df["date"] = pd.to_datetime(
    df["month"] + " " + df["year"].astype(str),
    format="%B %Y"
)

# Sort observations chronologically
df = df.sort_values("date")

# Display the first five observations
print(df.head())

# Display basic dataset information
print("\nDataset information:")
print(df.info())

# Plot the time series
plt.figure(figsize=(12, 6))

plt.plot(
    df["date"],
    df["passengers"],
    marker="o"
)

plt.title("Monthly Airline Passengers (1949–1960)")
plt.xlabel("Year")
plt.ylabel("Number of Passengers (Thousands)")
plt.grid(True)

plt.tight_layout()
plt.show()
