# 🌾 Dry Bean Classification with Machine Learning

## 📌 Problem Statement  
Manual classification of dry beans by visual inspection is labor-intensive, inconsistent, and prone to human error. In agricultural research and commercial operations, the need for **accurate and automated classification systems** has become essential for improving productivity, standardization, and decision-making. This project addresses this challenge using **machine learning techniques**.

---

## 💡 Solution  
Using a dataset containing **13,611 samples** and **16 morphological features**, this project builds and compares various classification models to automatically identify the **seven species of dry beans**. The final model was deployed using Streamlit, allowing users to input bean characteristics and receive instant predictions.

---

## 🔍 Project Highlights  
- ✅ **Exploratory Data Analysis (EDA):** Distribution plots, boxplots, pairplots, and correlation analysis to understand data patterns and outliers.
- ✅ **Model Training & Comparison:**
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - XGBoost
- ✅ **Feature Selection:** Used **Recursive Feature Elimination (RFE)** to identify the most important features contributing to classification.
- ✅ **Dimensionality Reduction:** Applied **PCA** to reduce features and visualize bean class separation in 2D.
- ✅ **Cross-Validation & Evaluation:** Assessed models using cross-validation, confusion matrix, and class-wise accuracy.
- ✅ **Hyperparameter Tuning:** Performed GridSearchCV and RandomizedSearchCV on Gradient Boosting and XGBoost to improve model performance.

---

## 🚀 Deployment  
Try the deployed model here:  
🔗 **[Dry Bean Classifier Web App](https://drybeanclassification.streamlit.app/)**

---

## 🛠️ Tools & Technologies  
- **Python** (Pandas, NumPy, Scikit-learn)
- **XGBoost**, **Random Forest**, **Gradient Boosting**
- **Matplotlib**, **Seaborn** for Data Visualization
- **Streamlit** for Deployment
- **Jupyter Notebook** for development and experimentation

---

## 💭 Key Takeaways  

- **Domain-Specific ML Enhances Real-World Impact:**  
  Applying machine learning in agriculture demonstrates how domain-specific data can be transformed into actionable insights that streamline traditional processes.

- **Fewer Features, Same Power:**  
  With Recursive Feature Elimination (RFE), the model achieved high accuracy with a **reduced feature set**, showing that simpler models can still be powerful if built on the right features.

- **Explainability Matters:**  
  PCA visualizations and feature importance helped explain how the model makes decisions—critical for stakeholder trust and adoption in the field.

- **Data Quality is as Important as Model Choice:**  
  Insights from EDA, such as outliers and feature distributions, played a big role in shaping model performance—clean data led to more stable predictions.

- **From Model to Meaningful Application:**  
  Deploying the trained model through a web interface bridged the gap between research and usability, proving that machine learning solutions can be made **accessible and practical** even for non-technical users.

---
