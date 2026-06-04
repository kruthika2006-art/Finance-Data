import streamlit as st
import pandas as pd
import plotly.express as px

from analysis import basic_analysis

st.set_page_config(
    page_title="Investment Analysis Dashboard",
    layout="wide"
)

st.title("Investment Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.header("Dataset Preview")
    st.dataframe(df)

    results = basic_analysis(df)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Rows",
        results["rows"]
    )

    col2.metric(
        "Columns",
        results["columns"]
    )

    col3.metric(
        "Average Age",
        results["avg_age"]
    )

    st.header("Gender Distribution")

    fig = px.pie(
        values=results["gender_count"].values,
        names=results["gender_count"].index,
        title="Gender Distribution"
    )

    st.plotly_chart(fig)

    st.header("Investment Preferences")

    investment_cols = [
        "Mutual_Funds",
        "Equity_Market",
        "Debentures",
        "Government_Bonds",
        "Fixed_Deposits",
        "PPF",
        "Gold"
    ]

    avg_scores = df[investment_cols].mean()

    fig2 = px.bar(
        x=avg_scores.index,
        y=avg_scores.values,
        labels={
            "x": "Investment Type",
            "y": "Average Score"
        },
        title="Average Investment Preference"
    )

    st.plotly_chart(fig2)

    st.header("Age Distribution")

    fig3 = px.histogram(
        df,
        x="age",
        nbins=10,
        title="Age Distribution"
    )

    st.plotly_chart(fig3)

else:
    st.info("Upload your CSV file.")
