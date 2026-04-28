# 🛍️ RetailSight: Revenue Drop Analysis & Sales Intelligence Dashboard

<p align="center">
  <a href="https://retailsight-kw37dom9nvojs5rxahty8j.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Demo-Streamlit-green?style=for-the-badge&logo=streamlit" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/ML-Scikit--learn-orange?style=for-the-badge&logo=scikit-learn" />
</p>

<p align="center">
  <b>Diagnosing a 18% revenue drop across retail segments — and predicting where sales are headed next</b>
</p>

---

## 🧩 Business Problem

A mid-size retail company noticed a **significant revenue drop** across multiple product categories and regions. Leadership needed answers fast:

- *Which categories and regions are underperforming — and why?*
- *Is this a seasonal dip or a structural decline?*
- *What will sales look like next quarter if nothing changes?*

**RetailSight** was built to answer these questions through interactive analytics and ML-powered forecasting — giving business stakeholders a self-service tool to explore the data themselves.

---

## 💡 Key Business Recommendations

| Finding | Recommendation | Estimated Impact |
|--------|----------------|-----------------|
| Technology category drives the highest revenue but shows seasonal dips in Q1 | Pre-load inventory and run promotions in January–February | Recover ~10–15% of Q1 revenue gap |
| Certain regions consistently outperform others | Replicate top-region sales strategy (pricing, promotions) in underperforming regions | Lift underperforming region revenue by ~8% |
| Top 10 products account for disproportionate share of sales | Protect stock availability and prioritize marketing for top SKUs | Reduce revenue leakage from stockouts |
| Consumer segment shows highest order volume but lower avg order value | Introduce bundle offers to increase basket size | Increase avg order value by ~12% |

---

## 📊 Key Insights

- **Technology** generates the highest revenue among all categories
- **Regional performance gap** identified — West region leads, South lags by ~22%
- **Seasonal trends** detected — Q4 consistently outperforms Q1 by 35%+
- **Top 10 products** contribute to over 40% of total sales revenue
- **Consumer segment** places most orders but Corporate segment yields higher profit margins

---

## 🔮 ML Sales Forecasting

| Detail | Value |
|--------|-------|
| Model | Linear Regression |
| Features | Month, Quarter, Category encoding, Region encoding |
| Use case | Predict next period's sales by category and region |
| Evaluation | R² Score, RMSE (see notebook for results) |

> **Next improvement planned:** Upgrade to Random Forest or XGBoost with cross-validation and proper RMSE/MAPE reporting for production-grade forecasting.

---

## ✨ Dashboard Features

| Feature | What It Does |
|---------|-------------|
| Dynamic filtering | Filter by Region, Category, Customer Segment in real time |
| KPI metrics | Sales, Orders, Average Order Value — updated with filters |
| Sales trend chart | Monthly/quarterly trend with trendline overlay |
| Top products analysis | Bar chart of top 10 revenue-generating products |
| Customer segmentation | Purchase behavior by Consumer, Corporate, Home Office |
| Sales prediction | Enter inputs → get predicted sales value instantly |
| CSV download | Export filtered data for offline reporting |

---

## 📐 Project Workflow

```
Raw CSV → Data Cleaning → EDA → Feature Engineering → ML Model → Streamlit Dashboard → Business Insights
```

1. **Data Cleaning** — parsed date formats, handled nulls, standardized category labels
2. **EDA** — trend analysis, regional comparison, category performance, seasonality detection
3. **Feature Engineering** — extracted month, quarter, year from Order Date; encoded categorical variables
4. **ML Forecasting** — Linear Regression trained on time-based features for sales prediction
5. **Streamlit App** — fully interactive dashboard deployed on Streamlit Cloud

---

## 📁 Dataset

- **Source:** [Superstore Sales Dataset — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Size:** 9,994 orders × 21 features
- **Key fields:** Order Date, Region, Category, Sales, Profit, Customer Segment, Product Name

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.10 |
| Data Analysis | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn (Linear Regression) |
| Dashboard Framework | Streamlit |
| Deployment | Streamlit Cloud |

---

## 🗂️ Project Structure

```
RetailSight/
├── app/
│   └── app.py                  # Main Streamlit application
├── data/
│   └── superstore.csv          # Source dataset
├── notebooks/
│   └── retail_analysis.ipynb   # EDA + ML development notebook
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Shwetha-Francis/Retail-Industry-Sales-Data-Revenue-Drop-Analysis-.git
cd Retail-Industry-Sales-Data-Revenue-Drop-Analysis-

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app/app.py
```

Or simply visit the **[Live Demo →](https://retailsight-kw37dom9nvojs5rxahty8j.streamlit.app/)**

---

## 🔭 Planned Improvements

- [ ] Upgrade ML model to Random Forest / XGBoost
- [ ] Add proper model evaluation (R², RMSE, MAPE)
- [ ] Add RFM customer segmentation module
- [ ] Migrate charts to Plotly for richer interactivity
- [ ] Add SQL-based data querying layer

---

## 👩‍💻 About

**Shwetha Francis** | BTech in AI & Data Science  
Aspiring Data Analyst with hands-on experience in Python, Power BI, Streamlit, and machine learning.  
Passionate about turning messy data into clear, actionable business decisions.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/your-profile)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black)](https://github.com/Shwetha-Francis)
[![Live App](https://img.shields.io/badge/Live%20App-RetailSight-green)](https://retailsight-kw37dom9nvojs5rxahty8j.streamlit.app/)
