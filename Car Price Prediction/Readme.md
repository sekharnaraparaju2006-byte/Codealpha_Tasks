# 🚗 Car Price Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict the selling price of used cars using Machine Learning techniques. Various car features such as year of manufacture, present showroom price, fuel type, transmission type, ownership status, and kilometers driven are used to estimate the resale value of a car.

---

## 🎯 Objective

To build a machine learning model that can accurately predict the selling price of a used car based on its features.

---

## 📂 Dataset Information

The dataset contains information about used cars, including:

- Car Name
- Year
- Selling Price
- Present Price
- Driven Kilometers
- Fuel Type
- Selling Type
- Transmission
- Owner

Total Records: **301**

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

### 1. Data Inspection
- Checked first 5 rows
- Identified dataset shape
- Examined column names
- Verified missing values

### 2. Distribution of Selling Prices
A histogram was used to visualize the distribution of car selling prices.

### 3. Fuel Type Analysis
Average selling prices were compared among:
- Petrol
- Diesel
- CNG

### 4. Present Price vs Selling Price
A scatter plot was created to study the relationship between showroom price and resale price.

**Observation:**
Cars with higher showroom prices generally have higher selling prices, showing a positive correlation.

---

## ⚙️ Data Preprocessing

- Removed unnecessary columns
- Converted categorical variables into numerical format using One-Hot Encoding (`get_dummies()`)
- Split data into training and testing sets

Training Data: **240 records**

Testing Data: **61 records**

---

## 🤖 Machine Learning Model

### Linear Regression

The Linear Regression algorithm was used to predict car selling prices.

```python
from sklearn.linear_model import LinearRegression
```

The model was trained using the training dataset and evaluated using unseen test data.

---

## 📈 Model Performance

### R² Score

```text
0.8489
```

The model explains approximately **84.89%** of the variation in car selling prices.

---

## 🔍 Key Insights

1. Present Price has a strong positive relationship with Selling Price.
2. Diesel cars generally have higher average selling prices compared to Petrol and CNG cars.
3. Car resale value decreases with age and increased usage.
4. The Linear Regression model achieved good predictive performance with an R² score of approximately 85%.

---

## 📷 Visualizations

- Selling Price Distribution Histogram
- Present Price vs Selling Price Scatter Plot

---

## 🚀 Conclusion

This project demonstrates how machine learning can be used to estimate used car prices effectively. Through data preprocessing, visualization, and Linear Regression modeling, a reliable prediction system was developed with strong performance.

---

## 👨‍💻 Author

**Sekhar Naraparaju**

CodeAlpha Data Science Internship Project