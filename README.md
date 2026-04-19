🛍️ RetailSight: ML-Powered Retail Analytics Dashboard

📌 Overview

RetailSight is an interactive data analytics and machine learning dashboard built using Streamlit to analyze retail sales data and generate actionable business insights. The application enables real-time exploration of sales performance and predicts future sales trends.

🚀 Live Demo

🔗 [http://localhost:8502](https://retailsight-kw37dom9nvojs5rxahty8j.streamlit.app/)

🎯 Objectives

Analyze retail sales performance
Identify top-performing categories and regions
Understand customer purchasing behavior
Forecast future sales using Machine Learning


📊 Features

📈 Interactive Dashboard using Streamlit
🔍 Dynamic Filtering (Region, Category)
💰 KPI Metrics (Sales, Orders, Average Order Value)
📊 Sales Trend Visualization
🏆 Top Products Analysis
👥 Customer Segment Analysis
🤖 Automated Business Insights
🔮 Sales Prediction using Machine Learning
📥 Download Filtered Data (CSV)


📂 Dataset

Source: Kaggle (Superstore dataset)
Includes:
Order Date
Region
Category
Sales
Profit
Customer Segment


⚙️ Tech Stack

Python
Pandas
Matplotlib
Streamlit
Scikit-learn
NumPy


🤖 Machine Learning

Implemented Linear Regression model to predict future sales
Performed feature engineering using time-based variables
Integrated predictions into the interactive dashboard


📊 Key Insights

Technology category generates the highest sales
Certain regions consistently outperform others
Seasonal trends observed in monthly sales
Top products contribute significantly to revenue


📁 Project Structure

retailsight/
│── app/
│    └── app.py              # Streamlit Dashboard
│── src/
│    └── analysis.py         # Data Analysis Scripts
│── data/
│    └── train.csv
|── notebook/
|    └── retailsight_analysis.ipynb 
│── visuals/
│    ├── category_sales.png
│    ├── monthly_sales.png
│── requirements.txt
│── README.md

🚀 Future Enhancements
Advanced ML models (Random Forest, XGBoost)
Model performance evaluation (R², RMSE)
Interactive visualizations using Plotly
Deployment with custom domain
👩‍💻 Author

Shwetha Francis
AI & Data Science Graduate
