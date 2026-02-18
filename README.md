# Project 1: Exploratory Data Analysis (EDA) — Titanic Dataset

A beginner-friendly data analysis project using the Titanic dataset to explore survival patterns through Python, Pandas, and Matplotlib.

---

## 📌 Overview

This project walks through the core steps of Exploratory Data Analysis (EDA) — from loading and cleaning data to visualizing key insights. It also covers Python fundamentals and Matplotlib/NumPy concepts practiced alongside the analysis.

---

## 🗂️ Dataset

- **Source:** [Titanic Dataset](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)
- **Records:** 891 passengers
- **Features:** PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning & analysis |
| Matplotlib | Data visualization |
| NumPy | Numerical operations |

---

## 📋 Project Steps

### Step 1 — Import Libraries
Imported `pandas` for data handling and `matplotlib` for visualization.

### Step 2 — Load Dataset
Loaded the Titanic CSV directly from an online URL using `pd.read_csv()`.

### Step 3 — Understand the Data
- Checked shape (rows × columns) using `df.shape`
- Explored column names and data types using `df.info()`
- Generated statistical summary using `df.describe()`

### Step 4 — Handle Missing Values
- Filled missing **Age** values with the column mean
- Filled missing **Embarked** values with the most frequent value (mode)

### Step 5 — Simple Analysis
- Counted survival vs. non-survival using `value_counts()`

### Step 6 — Data Visualization
- **Survival Count Bar Chart** — overall survived vs. not survived
- **Gender vs. Survival Rate** — compared survival rates by sex
- **Age Distribution Histogram** — spread of passenger ages

---

## 📊 Key Findings

- More passengers **died** than survived
- **Females** had a significantly higher survival rate than males
- Most passengers were between **20–40 years old**
- Both **age and gender** strongly influenced survival outcomes

---

## 🧠 Python Concepts Covered

Along with EDA, the notebook also covers Python fundamentals:

- **Variables, Data Types & Operators** — area of a triangle, f-strings
- **Lists & Indexing** — accessing elements by index
- **Conditional Statements** — if-else, if-elif-else, nested conditions
- **Loops** — `for` and `while` loops
- **Modules** — `math`, `datetime`
- **Matplotlib & NumPy** — line plots, scatter plots, bar charts, histograms, pie charts

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:
   ```bash
   pip install pandas matplotlib numpy
   ```

3. Open the notebook:
   ```bash
   jupyter notebook "Project_1__EDA_.ipynb"
   ```

---

## 📁 File Structure

```
📦 Project 1 - EDA
 ┣ 📓 Project_1__EDA_.ipynb   # Main Jupyter Notebook
 ┗ 📄 README.md               # Project documentation
```

---

## 🙋‍♂️ Author 

Made with ❤️ as part of a data science learning journey.
