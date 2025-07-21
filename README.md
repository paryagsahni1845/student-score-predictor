# Student Score Predictor: End-to-End Machine Learning Pipeline

## 📌 Project Overview

This project aims to predict students' math scores based on various demographic and academic features. It demonstrates the development of an end-to-end machine learning system, starting from data ingestion and preprocessing to model training, evaluation, and deployment through a Flask-based web interface.

This project is built to simulate a real-world ML application pipeline, complete with modular Python scripts, serialized artifacts, and a web interface for user interaction.

---

## 🎯 Objectives

- Understand the relationship between student performance and socio-academic factors
- Build a clean and modular ML pipeline
- Perform data preprocessing and transformation
- Train multiple models and evaluate them using R² score
- Save the best-performing model and preprocessing pipeline
- Develop a Flask UI for real-time predictions
- Deploy the project using AWS EC2 and Docker (via Amazon ECR)

---

## 📊 Dataset

- **Source**: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Size**: 1000 rows and 8 columns
- **Features**:
  - `gender`
  - `race/ethnicity`
  - `parental level of education`
  - `lunch`
  - `test preparation course`
  - `reading score`
  - `writing score`
- **Target**: `math score`

---

## 🧠 Methodology

### 1. Problem Statement

Build a regression model that can predict a student's math score based on input attributes.

### 2. Data Ingestion

- Read raw data from CSV
- Perform train-test split
- Save raw, train, and test datasets into an `artifacts/` folder

### 3. Data Transformation

- Handle missing values using `SimpleImputer`
- Encode categorical variables using `OneHotEncoder`
- Standardize features with `StandardScaler`
- Save preprocessing pipeline as `preprocessor.pkl`

### 4. Model Training

- Evaluate multiple regressors: Linear Regression, Decision Tree, Random Forest, XGBoost, CatBoost, AdaBoost, and Gradient Boosting
- Perform hyperparameter tuning using `GridSearchCV`
- Select the best model based on R² score
- Save the best model as `model.pkl`

### 5. Prediction Pipeline

- Load model and preprocessor objects
- Transform new data and return prediction

### 6. Flask Web App

- Created a UI form with dropdowns and inputs for all features
- Accepts user input and returns predicted math score
- Uses the prediction pipeline to process form data and generate output

### 7. Deployment (Planned)

- Flask app runs on port 5000 locally
- Dockerized the entire application
- Deployment planned on **AWS EC2 instance** using **ECR (Elastic Container Registry)** to host Docker image

---

## 🧰 Technology Stack

- **Language**: Python 3.10+
- **Framework**: Flask (for web app)
- **Libraries**:
  - `pandas`, `numpy` (data handling)
  - `scikit-learn` (preprocessing, modeling, evaluation)
  - `xgboost`, `catboost` (advanced regressors)
  - `dill` (serialization)
  - `logging`, `sys`, `os` (system handling)
- **Deployment Tools**:
  - Docker (for containerization)
  - AWS EC2 + ECR (for deployment)

---

## 🧪 Models Evaluated

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

### Evaluation Metric:

- **R² Score** (on the test set)
- Grid search used for hyperparameter tuning
- Model with highest R² score selected and saved

---

## 🔍 Key Insights

- Students who completed test preparation tended to score significantly higher
- Parental education level had moderate influence on scores
- Ensemble methods (like Random Forest and Gradient Boosting) generally outperformed linear models

---

## 📷 UI Demo

A simple and clean HTML form built with Flask allows users to input values and get predicted scores.

**Input Fields**:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

**Output**:

- Predicted Math Score displayed on form submission


<img width="1088" height="645" alt="image" src="https://github.com/user-attachments/assets/f48acbd5-1ccc-4a6c-be2e-6c4371424778" />

<!-- ![Student Score Predictor UI](images/ui_screenshot.png) -->

---

## 📝 Conclusion

This project represents a complete machine learning pipeline from raw data to user-facing predictions. It showcases real-world skills such as modular code structure, model evaluation, Flask integration, and preparation for production deployment. It was a highly instructive learning experience covering all major aspects of building and deploying ML systems.

---

## 📎 Acknowledgments

- Kaggle for the dataset
- Scikit-learn, XGBoost, CatBoost teams for the libraries
- Flask for web framework

---
