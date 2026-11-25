
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# 1. Load the dataset
df = pd.read_csv("data/airline_passengers.csv")

# 2. Create a date column
df["date"] = pd.to_datetime(
    df["month"] + " " + df["year"].astype(str),
    format="%B %Y"
)

# 3. Sort chronologically and set date as index
df = df.sort_values("date")
df = df.set_index("date")
df = df.asfreq("MS")

# 4. Extract the passenger series
passengers = df["passengers"]


# 5. Define a function to perform the ADF test
def test_stationarity(series, name):
    result = adfuller(series.dropna())

    print(f"\n{name}")
    print("-" * 40)
    print("ADF Statistic:", round(result[0], 4))
    print("p-value:", round(result[1], 4))
    print("Critical Values:")

    for key, value in result[4].items():
        print(f"{key}: {value:.4f}")

    if result[1] < 0.05:
        print("Conclusion: Evidence supports stationarity.")
    else:
        print("Conclusion: Insufficient evidence of stationarity.")


# 6. Create different versions of the series
first_difference = passengers.diff(1)

seasonal_difference = passengers.diff(12)

combined_difference = passengers.diff(1).diff(12)


# 7. Test each version
test_stationarity(passengers, "Original Series")
test_stationarity(first_difference, "First Difference")
test_stationarity(seasonal_difference, "Seasonal Difference")
test_stationarity(combined_difference, "Combined Difference")


# 8. Visualize the transformations
fig, axes = plt.subplots(4, 1, figsize=(12, 12))

axes[0].plot(passengers)
axes[0].set_title("Original Series")

axes[1].plot(first_difference)
axes[1].set_title("First-Order Difference")

axes[2].plot(seasonal_difference)
axes[2].set_title("Seasonal Difference (12 months)")

axes[3].plot(combined_difference)
axes[3].set_title("Combined Difference")

for ax in axes:
    ax.grid(True)

plt.tight_layout()
plt.show()