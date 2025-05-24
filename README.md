#  HR Analytics: Predicting Job Change of Data Scientists

## Overview

This project focuses on understanding and predicting the likelihood of job changes among data science professionals. By leveraging a combination of demographic and experiential factors, we performed exploratory data analysis, feature engineering, and classification modeling. An interactive dashboard was also created to visualize patterns.

---

## Table of Contents

- [Dataset Description](#dataset-description)
- [Objective](#objective)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Feature Engineering](#feature-engineering)
- [Modeling & Evaluation](#modeling--evaluation)
- [Feature Importance](#feature-importance)
- [Interactive Dashboard](#interactive-dashboard)
- [How to Run the Dashboard](#how-to-run-the-dashboard)
- [Conclusion](#conclusion)

---

## Dataset Description

The dataset includes demographic, educational, and employment-related information of data science professionals:

- `train.csv`: Training data (19,158 rows × 14 columns)
- `test.csv`: Test data (2,129 rows × 13 columns)
- `test_target.csv`: Target values for test data

---

## Objective

To predict whether a candidate is likely to look for a new job based on various features using classification techniques.

---

## Exploratory Data Analysis (EDA)

### 🔍 Missing Values
Visualizing percentage of missing data per column:

![Missing Values](images/missing-values-plot.png)

### Target Class Distribution
Majority of the candidates are **not** looking for a new job:

![Target Distribution](images/target-distribution.png)

### Experience Distribution
Shows the distribution of years of experience:

![Experience Distribution](images/experience-distribution.png)

---

Feature Engineering

- Cleaned `experience` and `last_new_job` columns by converting ranges and symbols to numeric.
- Encoded categorical columns using `LabelEncoder`.
- Combined train/test for consistent transformation.

---

Modeling & Evaluation

A Random Forest Classifier was used:

**Classification Report:**
Precision: 0.83 (class 0), 0.57 (class 1)
Recall: 0.88 (class 0), 0.47 (class 1)
Accuracy: 78%


**Confusion Matrix:**
[[2543 334]
[ 506 449]]


---

Feature Importance

Top contributing features (according to Random Forest):

1. `training_hours`
2. `city_development_index`
3. `experience`
4. `company_size`
5. `city`

![Feature Importance](images/feature-importance.png)

---

📊 Interactive Dashboard

A dashboard was created using **Plotly Dash** for visualizing key metrics and distributions interactively.

![Dashboard Preview](images/dashboard-preview.png)

---

How to Run the Dashboard

1. Clone this repository:
   ```bash
   git clone https://github.com/arnavrajpurohit/hr-analytics-job-change.git
   cd hr-analytics-job-change
2. pip install -r requirements.txt
3. Run the dashboard: python dashboard.py
4. Visit:
http://127.0.0.1:8050/
 


Conclusion

This project demonstrates how HR analytics can be used to understand and predict job change behavior in data scientists. By applying data preprocessing, EDA, modeling, and visualization, we derived actionable insights and built an interactive tool for exploration.



Author

Arnav — Aspiring Data Scientist passionate about solving real-world problems using data.


