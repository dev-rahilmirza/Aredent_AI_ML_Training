# 🏠 House Price Prediction — Linear Regression

A beginner-friendly Machine Learning project that trains a **Linear Regression** model to predict California house prices based on real-world features like number of rooms, area, and population. Built entirely in Python using the `scikit-learn` California Housing dataset.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Tech Stack](#-tech-stack)
- [Project Workflow](#-project-workflow)
- [Model Evaluation](#-model-evaluation)
- [Visualizations](#-visualizations)
- [Feature Importance](#-feature-importance)
- [Model Improvement](#-model-improvement)
- [Output](#-output)
- [Getting Started](#-getting-started)
- [File Structure](#-file-structure)

---

## 🎯 Project Overview

This project demonstrates a complete **end-to-end Machine Learning pipeline** — from data loading and exploration to model training, evaluation, and saving results. It is designed as a learning project to understand:

- How Linear Regression works
- How to split data into training and testing sets
- How to evaluate a model using RMSE and R² Score
- How to interpret feature coefficients
- How to improve predictions using log transformation

---

## 📊 Dataset

| Property       | Details                                      |
|----------------|----------------------------------------------|
| **Name**       | California Housing Dataset                   |
| **Source**     | Built-in via `sklearn.datasets`              |
| **Rows**       | 20,640 samples                               |
| **Features**   | 8 input features + 1 target (Price)          |
| **No Download**| Loaded directly — no CSV or URL needed       |

### Features Used

| Feature       | Description                                      |
|---------------|--------------------------------------------------|
| `MedInc`      | Median income in block group                     |
| `HouseAge`    | Median house age in block group                  |
| `AveRooms`    | Average number of rooms per household            |
| `AveBedrms`   | Average number of bedrooms per household         |
| `Population`  | Block group population                           |
| `AveOccup`    | Average number of household members              |
| `Latitude`    | Block group latitude                             |
| `Longitude`   | Block group longitude                            |
| `Price` ⭐    | **Target** — Median house value (in $100,000s)   |

---

## 🛠️ Tech Stack

| Tool / Library     | Purpose                                      |
|--------------------|----------------------------------------------|
| `Python 3.x`       | Core programming language                    |
| `NumPy`            | Numerical computations                       |
| `Pandas`           | Data loading and manipulation                |
| `Matplotlib`       | Data visualization                           |
| `scikit-learn`     | ML model, dataset, metrics, train-test split |
| `Jupyter Notebook` | Interactive development environment          |

---

## 🔄 Project Workflow

The notebook follows a clean 14-step pipeline:

```
Step 1  → Import Libraries
Step 2  → Load California Housing Dataset (from sklearn)
Step 3  → Data Understanding (shape, info, describe)
Step 4  → Check Missing Values
Step 5  → Select Features (X) and Target (y)
Step 6  → Train-Test Split (80% train / 20% test)
Step 7  → Train Linear Regression Model
Step 8  → Make Predictions on Test Data
Step 9  → Evaluate Model (RMSE + R² Score)
Step 10 → Visualization: Actual vs Predicted
Step 11 → Residual Plot (Error Analysis)
Step 12 → Feature Importance (Coefficients)
Step 13 → Model Improvement (Log Transformation)
Step 14 → Save Prediction Results as CSV
```

### Train-Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Training set: 80%  |  Testing set: 20%
```

---

## 📈 Model Evaluation

Two key metrics are used to measure model performance:

| Metric        | Interpretation                              |
|---------------|---------------------------------------------|
| **RMSE**      | Average prediction error — lower = better  |
| **R² Score**  | Closer to 1.0 = better fit                 |

```python
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)
```

---

## 📉 Visualizations

### 1. Actual vs Predicted Prices
A scatter plot comparing actual and predicted house prices. Points close to the diagonal line indicate accurate predictions.

```python
plt.scatter(y_test, y_pred)
plt.title("Actual vs Predicted Prices")
```

### 2. Residual Plot
Plots prediction errors (residuals) against predicted values. A random scatter around the zero line indicates a well-fitted model.

```python
residuals = y_test - y_pred
plt.scatter(y_pred, residuals)
plt.axhline(y=0)
```

---

## 🔍 Feature Importance

Linear Regression learns a **coefficient (weight)** for each feature. These coefficients reveal which features most strongly influence the house price.

```python
coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values(by="Coefficient", ascending=False)
```

| Coefficient Sign | Meaning                                   |
|------------------|-------------------------------------------|
| **Positive (+)** | Feature increases predicted house price   |
| **Negative (−)** | Feature decreases predicted house price   |

---

## 🚀 Model Improvement

A **Log Transformation** is applied to the target variable `y` to reduce skewness and improve model performance:

```python
y_log = np.log1p(y)   # log(1 + y) to handle zero values safely

model2 = LinearRegression()
model2.fit(X_train2, y_train2)
```

Results are compared before and after transformation using RMSE and R² Score.

---

## 💾 Output

Prediction results are exported to a CSV file for further analysis:

```python
result_df = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})
result_df.to_csv("house_price_prediction.csv", index=False)
```

**Output file:** `house_price_prediction.csv`

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/dev-rahilmirza/house-price-prediction.git
cd house-price-prediction
```

### 2. Install dependencies

```bash
pip install numpy pandas matplotlib scikit-learn jupyter
```

### 3. Launch Jupyter Notebook

```bash
jupyter notebook Project_2_house_price_prediction_.ipynb
```

### 4. Run all cells top to bottom
Use **Kernel → Restart & Run All** to execute the full pipeline.

---

## 📁 File Structure

```
house-price-prediction/
│
├── Project_2_house_price_prediction_.ipynb   # Main notebook
├── house_price_prediction.csv                # Generated predictions output
└── README.md                                 # Project documentation
```

---

## 💡 Key Concepts Covered

- **Linear Regression** — predicting continuous output from input features
- **Train-Test Split** — preventing overfitting by holding out test data
- **RMSE** — root mean squared error as a performance metric
- **R² Score** — how well the model explains variance in data
- **Residual Analysis** — diagnosing model errors through visualization
- **Feature Coefficients** — understanding which features drive predictions
- **Log Transformation** — feature engineering to improve model accuracy

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> 🎓 Built as **Project 2** in a Machine Learning learning series | Dataset: California Housing via `sklearn`
