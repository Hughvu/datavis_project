import streamlit as st
import pandas as pd
import plotly.express as px

st.title("ICT Business Analyst Portfolio Dashboard")

df = pd.read_csv("sales_data.csv")

st.subheader("Monthly Sales Trend")
monthly_sales = df.groupby("Month")["Revenue"].sum().reset_index()

fig = px.line(
    monthly_sales,
    x="Month",
    y="Revenue",
    title="Monthly Revenue Trend",
    markers=True
)

st.plotly_chart(fig)

st.subheader("Sales by Category")
category_sales = df.groupby("Category")["Revenue"].sum().reset_index()

fig2 = px.bar(
    category_sales,
    x="Category",
    y="Revenue",
    title="Revenue by Product Category"
)

st.plotly_chart(fig2)