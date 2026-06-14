# Cardiovascular Disease Prediction Using Machine Learning

## Project Overview

Cardiovascular diseases are among the leading causes of death worldwide. Early prediction of cardiovascular disease can help healthcare professionals make informed decisions and improve patient outcomes.

This project applies machine learning techniques to predict the presence of cardiovascular disease using patient medical information. The project covers the complete machine learning pipeline, including data preprocessing, exploratory data analysis, feature engineering, model training, hyperparameter tuning, model evaluation, and deployment.

---

## Project Objectives

* Predict cardiovascular disease using patient medical data.
* Compare multiple machine learning algorithms.
* Identify the best-performing model.
* Deploy the final model as an interactive web application using Streamlit.

---

## Dataset Information

### Dataset Source

The dataset used in this project was obtained from Kaggle and contains patient medical information related to cardiovascular disease risk factors.

Dataset: Cardiovascular Disease Dataset (Kaggle)

The dataset was selected because it represents a real-world healthcare problem and provides sufficient data for machine learning model development, evaluation, and deployment.

### Dataset Characteristics

* Approximately 68,985 records
* 13 features
* Binary classification problem

### Target Variable

* 0 = No Cardiovascular Disease
* 1 = Cardiovascular Disease

### Features Include

* Age
* Gender
* Height
* Weight
* Blood Pressure
* Cholesterol Level
* Glucose Level
* Smoking Status
* Alcohol Consumption
* Physical Activity

---

## Data Preprocessing

The following preprocessing steps were performed:

* Missing value inspection
* Duplicate removal
* Outlier handling
* Data cleaning
* Feature scaling

### Feature Engineering

A new feature called BMI (Body Mass Index) was created using height and weight:

BMI = Weight / Height²

This feature was included because BMI is strongly associated with cardiovascular disease risk and can improve predictive performance.

---

## Exploratory Data Analysis (EDA)

Several visualizations were created to explore the dataset and identify relationships between variables and cardiovascular disease.

The analysis included:

* Histograms
* Boxplots
* Scatterplots
* Correlation Heatmaps
* Feature Distribution Analysis

These visualizations helped identify trends, correlations, and potential predictors of cardiovascular disease.

---

## Machine Learning Models

Three machine learning algorithms were trained and compared:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

### Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 72.9%    |
| Decision Tree       | 63.0%    |
| Random Forest       | 71.8%    |

Logistic Regression achieved the highest baseline performance, while Random Forest was further optimized through hyperparameter tuning.

---

## Hyperparameter Tuning

GridSearchCV was used to optimize the Random Forest model.

### Best Parameters

* n_estimators = 200
* max_depth = 10
* min_samples_split = 5

### Best Cross-Validation Score

* 73.3%

Hyperparameter tuning improved the model's performance and reliability.

---

## Model Evaluation

The final tuned Random Forest model was evaluated using multiple performance metrics.

### Evaluation Results

* Accuracy: 73.5%
* Precision: 76.4%
* Recall: 67.7%
* F1 Score: 71.8%

A confusion matrix was also used to assess classification performance across both classes.

---

## Deployment

The final machine learning model was deployed using Streamlit.

The web application allows users to:

* Enter patient medical information
* Generate cardiovascular disease predictions
* Receive results in real time

The deployment demonstrates how machine learning models can be transformed into practical healthcare prediction tools.

---

## Repository Contents

* Cardiovascular_Disease_Prediction.ipynb
* app.py
* cardio_train.csv
* cardio_model.pkl
* scaler.pkl
* requirements.txt
* README.md


## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* GitHub

---

## Author

Mohammed Magdy Salem

Machine Learning and Data Mining Course
