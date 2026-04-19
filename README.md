🛍️ RetailSight: ML-Powered Retail Analytics Dashboard

🚀 Live Demo
🔗 https://retailsight-kw37dom9nvojs5rxahty8j.streamlit.app/

👉 An interactive data analytics + machine learning dashboard to explore retail sales performance, uncover insights, and predict future trends.

📌 Overview

RetailSight is a Streamlit-based analytics application built to transform raw retail data into actionable business insights.
It allows users to analyze sales trends, monitor KPIs, and forecast future sales through an intuitive and interactive interface.

🎯 Objectives
Analyze retail sales performance across regions and categories
Identify top-performing products and revenue drivers
Understand customer purchasing behavior and segmentation
Detect trends and seasonality in sales data
Forecast future sales using machine learning models
✨ Features
📊 Interactive dashboard for real-time analysis
🔍 Dynamic filters (Region, Category, Segment)
💰 KPI metrics (Total Sales, Orders, Average Order Value)
📈 Sales trend visualization
🏆 Top-performing products and categories
👥 Customer segment analysis
🤖 Automated business insights
🔮 Sales prediction using machine learning
📥 Export filtered data as CSV
📊 Dataset
Source: Kaggle – Superstore Dataset
Key Features:
Order Date
Region
Category
Sales
Profit
Customer Segment
⚙️ Tech Stack
Programming: Python
Data Analysis: Pandas, NumPy
Visualization: Matplotlib, Seaborn
Machine Learning: Scikit-learn
Framework: Streamlit
Deployment: Streamlit Cloud
🤖 Machine Learning
Built a Linear Regression model to predict future sales
Performed feature engineering using time-based variables
Integrated predictions directly into the dashboard for real-time insights
📊 Key Insights
📌 Technology category generates the highest revenue
🌍 Certain regions consistently outperform others
📅 Seasonal patterns observed in monthly sales trends
🏆 A small number of products contribute significantly to overall revenue
📁 Project Structure

retailsight/
│── app/
│ └── app.py # Streamlit dashboard
│── src/
│ └── analysis.py # Data analysis scripts
│── data/
│ └── train.csv
│── notebook/
│ └── retailsight_analysis.ipynb
│── visuals/
│ ├── category_sales.png
│ ├── monthly_sales.png
│── requirements.txt
│── README.md

🚀 Run Locally
git clone https://github.com/Shwetha-Francis/retailsight.git
cd retailsight
pip install -r requirements.txt
streamlit run app/app.py

Open in browser:
http://localhost:8501

🚀 Future Enhancements
Implement advanced models (Random Forest, XGBoost)
Add model evaluation metrics (R², RMSE)
Enhance UI with interactive visualizations (Plotly)
Deploy with custom domain and authentication
👩‍💻 Author

Shwetha Francis
AI & Data Science Graduate

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
