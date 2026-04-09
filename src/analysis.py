"""
RetailSight Project
Author: Shwetha Francis

Description:
This project analyzes retail sales data to extract business insights 
such as sales trends, category performance, and customer segmentation.
"""

import pandas as pd
import matplotlib.pyplot as plt


# Load dataset and Preprocess
df = pd.read_csv("data/train.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)#convert from sting to datetime format
df['Month'] = df['Order Date'].dt.to_period('M')

print("Dataset loaded Successfully\n")
print(df.head())

# KPI ANALYSIS

def calculate_kpis(df):
    total_sales = df['Sales'].sum()
    total_orders = df.shape[0]
    avg_order_value = df['Sales'].mean()

    print("\n KEY PERFORMANCE INDICATORS")
    print("-" * 40)
    print(f"Total Sales        : {total_sales:,.2f}")
    print(f"Total Orders       : {total_orders}")
    print(f"Avg Order Value    : {avg_order_value:,.2f}")

    return pd.DataFrame([{
        "Total Sales": total_sales,
        "Total Orders": total_orders,
        "Avg Order Value": avg_order_value
    }])


kpi_df = calculate_kpis(df)
print("\nKPI Table:\n", kpi_df)


# CATEGORY ANALYSIS

def category_analysis(df):
    category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

    print("\n Sales by Category:\n", category_sales)

    category_sales.plot(kind='bar', title="Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("visuals/category_sales.png")
    plt.close()


category_analysis(df)


# REGION ANALYSIS

def region_analysis(df):
    region_sales = df.groupby('Region')['Sales'].sum()
    print("\nSales by Region:\n", region_sales)


region_analysis(df)


# TIME SERIES ANALYSIS

def time_series_analysis(df):
    monthly_sales = df.groupby('Month')['Sales'].sum().sort_index()

    print("\n Monthly Sales Trend:\n", monthly_sales.head())

    monthly_sales.plot(kind='bar', title="Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visuals/monthly_sales.png")
    plt.close()


time_series_analysis(df)

# TOP PRODUCTS

def top_products_analysis(df):
    top_products = df.groupby('Product Name')['Sales'].sum() \
        .sort_values(ascending=False).head(10)

    print("\nTop 10 Products:\n", top_products)


top_products_analysis(df)


# CUSTOMER SEGMENT

def segment_analysis(df):
    segment_sales = df.groupby('Segment')['Sales'].sum()

    print("\n Sales by Customer Segment:\n", segment_sales)


segment_analysis(df)