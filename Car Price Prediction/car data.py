import pandas as pd

df = pd.read_csv("car data.csv")

print("First 5 Rows:")
print(df.head())

print("\nRows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.hist(df["Selling_Price"], bins=20)

plt.title("Distribution of Car Selling Prices")
plt.xlabel("Selling Price (Lakhs)")
plt.ylabel("Frequency")

plt.show()
print("\nCar Price Statistics:")

print("Average:", df["Selling_Price"].mean())
print("Maximum:", df["Selling_Price"].max())
print("Minimum:", df["Selling_Price"].min())
print("\nAverage Price by Fuel Type:")
print(df.groupby("Fuel_Type")["Selling_Price"].mean())
plt.figure(figsize=(8,5))

plt.scatter(df["Present_Price"], df["Selling_Price"])

plt.title("Present Price vs Selling Price")
plt.xlabel("Present Price (Lakhs)")
plt.ylabel("Selling Price (Lakhs)")

plt.show()
df = pd.get_dummies(df, drop_first=True)

print(df.head())
df = pd.read_csv("car data.csv")

df = df.drop("Car_Name", axis=1)

df = pd.get_dummies(df, drop_first=True)

print(df.head())
X = df.drop("Selling_Price", axis=1)

Y = df["Selling_Price"]

print("X Shape:", X.shape)
print("Y Shape:", Y.shape)
from sklearn.model_selection import train_test_split

X = df.drop("Selling_Price", axis=1)
Y = df["Selling_Price"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)
from sklearn.linear_model import LinearRegression
print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, Y_train)

print("Model Trained Successfully!")
predictions = model.predict(X_test)

print(predictions[:5])
from sklearn.metrics import r2_score

score = r2_score(Y_test, predictions)

print("R2 Score:", score)