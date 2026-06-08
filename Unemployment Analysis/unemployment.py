import pandas as pd

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# First 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset shape
print("\nRows and Columns:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistics on unemployment rate
print("\nUnemployment Statistics:")
print("Average:", df["Estimated Unemployment Rate (%)"].mean())
print("Maximum:", df["Estimated Unemployment Rate (%)"].max())
print("Minimum:", df["Estimated Unemployment Rate (%)"].min())
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

state_unemployment = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean()

top10 = state_unemployment.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top10.plot(kind="bar")

plt.title("Top 10 States by Average Unemployment Rate")
plt.xlabel("State")
plt.ylabel("Average Unemployment Rate (%)")

plt.show()
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
print(df["Date"].head())
monthly_unemployment = df.groupby("Date")["Estimated Unemployment Rate (%)"].mean()

print(monthly_unemployment.head())
plt.figure(figsize=(12,5))

monthly_unemployment.plot()

plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Average Unemployment Rate (%)")

plt.show()
print("\nHighest Unemployment Month:")
print(monthly_unemployment.idxmax())

print("\nHighest Unemployment Rate:")
print(monthly_unemployment.max())
area_unemployment = df.groupby("Area")["Estimated Unemployment Rate (%)"].mean()

print("\nUrban vs Rural:")
print(area_unemployment)

area_unemployment.plot(kind="bar")

plt.title("Average Unemployment Rate: Urban vs Rural")
plt.xlabel("Area")
plt.ylabel("Average Unemployment Rate (%)")

plt.show()