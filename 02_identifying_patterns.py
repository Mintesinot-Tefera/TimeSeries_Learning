
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/airline_passengers.csv")

# Create a date column
df["date"] = pd.to_datetime(
    df["month"] + " " + df["year"].astype(str),
    format="%B %Y"
)

df = df.sort_values("date")

# Calculate average passengers per year
annual_average = df.groupby("year")["passengers"].mean()

print("Average passengers per year:")
print(annual_average)

# Visualize annual averages
plt.figure(figsize=(12, 5))

plt.plot(
    annual_average.index,
    annual_average.values,
    marker="o"
)

plt.title("Average Airline Passengers Per Year")
plt.xlabel("Year")
plt.ylabel("Average Passengers (Thousands)")
plt.grid(True)

plt.tight_layout()
plt.show()


#########


# Calculate average passengers for each month
monthly_average = df.groupby("month")["passengers"].mean()

# Ensure months are displayed in calendar order
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_average = monthly_average.reindex(month_order)

print("\nAverage passengers by month:")
print(monthly_average)

# Visualize monthly averages
plt.figure(figsize=(12, 5))

plt.plot(
    monthly_average.index,
    monthly_average.values,
    marker="o"
)

plt.title("Average Airline Passengers by Month (1949–1960)")
plt.xlabel("Month")
plt.ylabel("Average Passengers (Thousands)")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()

