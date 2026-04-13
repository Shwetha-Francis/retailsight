import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


# PAGE CONFIG (IMPORTANT)

st.set_page_config(
    page_title="RetailSight",
    page_icon="📊",
    layout="wide"
)


# HEADER

st.markdown(
    """
    <h1 style='text-align: center;'>📊 RetailSight Dashboard</h1>
    <p style='text-align: center;'>AI + Analytics for Retail Business Insights</p>
    """,
    unsafe_allow_html=True
)


# LOAD DATA

@st.cache_data
def load_data():
    df = pd.read_csv("data/train.csv")
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
    df['Month'] = df['Order Date'].dt.to_period('M')
    df['Days'] = (df['Order Date'] - df['Order Date'].min()).dt.days
    return df

df = load_data()


# SIDEBAR

st.sidebar.header("🔍 Filters")

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]


# KPI SECTION

st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
col2.metric("📦 Total Orders", filtered_df.shape[0])
col3.metric("🧾 Avg Order Value", f"${filtered_df['Sales'].mean():,.2f}")

# CHARTS (SIDE BY SIDE)

col4, col5 = st.columns(2)

with col4:
    st.subheader("📊 Sales by Category")
    cat_sales = filtered_df.groupby("Category")["Sales"].sum()

    fig1, ax1 = plt.subplots()
    cat_sales.plot(kind='bar', ax=ax1)
    st.pyplot(fig1)

with col5:
    st.subheader("🌍 Sales by Region")
    region_sales = filtered_df.groupby("Region")["Sales"].sum()
    st.bar_chart(region_sales)


# TIME SERIES

st.subheader("📈 Monthly Sales Trend")

monthly_sales = filtered_df.groupby("Month")["Sales"].sum().sort_index()
st.line_chart(monthly_sales)


# TOP PRODUCTS

st.subheader("🏆 Top 10 Products")

top_products = filtered_df.groupby("Product Name")["Sales"].sum() \
    .sort_values(ascending=False).head(10)

st.dataframe(top_products)


#  INSIGHTS

st.subheader("🤖 Smart Insights")

if not filtered_df.empty:
    top_category = filtered_df.groupby("Category")["Sales"].sum().idxmax()
    top_region = filtered_df.groupby("Region")["Sales"].sum().idxmax()

    st.info(f"🏆 {top_category} is driving the highest sales.")
    st.info(f"🌍 {top_region} region shows strongest performance.")
else:
    st.warning("No data available")


#  ML MODEL

model = LinearRegression()
model.fit(df[['Days']], df['Sales'])


#  PREDICTION

st.subheader("🔮 Sales Forecast")

future_days = st.slider("Days into Future", 1, 30, 7)
future_value = [[df['Days'].max() + future_days]]

prediction = model.predict(future_value)

st.success(f"📈 Predicted Sales: ${prediction[0]:,.2f}")


#  DOWNLOAD BUTTON

st.subheader("📥 Download Data")

csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="retailsight_data.csv",
    mime="text/csv"
)