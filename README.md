# 🛍️ Fashion Recommendation System

## 📌 Overview

This project is an end-to-end **Fashion Product Recommendation System** built using the **H&M Personalized Fashion Recommendations Dataset**. The system recommends similar fashion products based on customer purchasing behavior using **Item-Based Collaborative Filtering** and **Cosine Similarity**.

The project follows a complete Data Science workflow including data preprocessing, exploratory data analysis (EDA), model building, evaluation, and deployment using Streamlit.

---

## 🚀 Features

* Exploratory Data Analysis (EDA)
* Customer Purchase Behavior Analysis
* Product Popularity Analysis
* Recommendation Engine using Collaborative Filtering
* Model Evaluation using Precision@K, Recall@K, and Hit Rate
* Interactive Streamlit Web Application
* Product Explorer and Recommendation Dashboard

---

## 📊 Dataset

**Dataset:** H&M Personalized Fashion Recommendations
**Link:** https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations

Dataset contains:

* 31M+ customer transactions
* 1.3M+ customers
* 100K+ fashion products

Files used:

* `articles.csv`
* `customers.csv`
* `transactions_train.csv`

---

## 🛠️ Tech Stack

### Languages

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Pickle

### Deployment

* Streamlit

---

## 📂 Project Structure

```text
Fashion-Recommendation-System/
│
├── Data/
│   ├── articles.csv
│   ├── customers.csv
│   └── transactions_train.csv
│
├── notebooks/
│   ├── 01_Data_Loading.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Model_Evaluation.ipynb
│
├── models/
│   ├── similarity.pkl
│   └── articles.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔍 Exploratory Data Analysis

The following analyses were performed:

### Customer Analysis

* Active customers
* Purchase frequency
* Customer buying patterns

### Product Analysis

* Top-selling products
* Popular categories
* Color preferences
* Department-wise sales

### Sales Trend Analysis

* Monthly purchase trends
* Transaction distribution

### RFM Analysis

* Recency
* Frequency
* Monetary Value

---

## 🤖 Recommendation Model

### Approach

The recommendation system uses:

**Item-Based Collaborative Filtering**

Steps:

1. Create Customer-Product Interaction Matrix
2. Compute Cosine Similarity between products
3. Identify similar products
4. Generate Top-N recommendations

### Similarity Metric

```python
Cosine Similarity
```

---

## 📈 Model Evaluation

Evaluation metrics used:

* Precision@K
* Recall@K
* Hit Rate

### Results

| Metric       | Score           |
| ------------ | --------------- |
| Precision@10 | 0.0071          |
| Recall@10    | 0.07            |
| Hit Rate     | 0.072           |

---

## 🖥️ Streamlit Application

The web application includes:

### Home Dashboard

* Project overview
* Dataset summary

### Product Explorer

* Browse fashion products
* View product details

### Recommendation Engine

* Select a product
* Generate similar product recommendations

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/ShivamKumarSrivastava/Fashion-Recommendation-System.git

cd Fashion-Recommendation-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Key Learnings

* Large-scale retail data analysis
* Recommendation system development
* Collaborative filtering techniques
* Model evaluation for recommender systems
* End-to-end ML project deployment
* Streamlit application development

---

## 📸 Screenshots

Add screenshots of:

* EDA Dashboard
* Product Explorer
* Recommendation Engine

---

## 🔮 Future Improvements

* Matrix Factorization (SVD)
* Deep Learning-based Recommendations
* Personalized User Recommendations
* Product Image Integration
* Hybrid Recommendation System
* Real-time Recommendation Pipeline

---

## 👨‍💻 Author

**Shivam Kumar**

B.Tech Information Technology

Interested in:

* Data Science
* Machine Learning
* Artificial Intelligence
* Analytics

LinkedIn: https://www.linkedin.com/in/shivam-srivastava-314153256/

