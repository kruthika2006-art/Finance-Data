import pandas as pd


def basic_analysis(df):

    results = {}

    results["rows"] = len(df)
    results["columns"] = len(df.columns)

    results["gender_count"] = df["gender"].value_counts()

    results["avg_age"] = round(df["age"].mean(), 2)

    return results
