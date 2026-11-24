
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose

# Load the dataset
df = pd.read_csv("data/airline_passengers.csv")

# Create a proper monthly date column
df["date"] = pd.to_datetime(
    df["month"] + " " + df["year"].astype(str),
    format="%B %Y"
)

# Set date as the index
df = df.sort_values("date")
df = df.set_index("date")

# Tell pandas that observations are monthly
df = df.asfreq("MS")

# Select the time series
passengers = df["passengers"]

# Perform additive decomposition
decomposition = seasonal_decompose(
    passengers,
    model="additive",
    period=12
)

# Display the four components
decomposition.plot()

plt.suptitle(
    "Additive Time-Series Decomposition",
    fontsize=14
)

plt.tight_layout()
plt.show()

# Display the first few values of each component
print("Trend component:")
print(decomposition.trend.head(15))

print("\nSeasonal component:")
print(decomposition.seasonal.head(15))

print("\nResidual component:")
print(decomposition.resid.head(15))
