import pandas as pd
import streamlit as st

# Load data
df = pd.read_csv("data.csv")

# Categorize function
def categorize(desc):
    desc = desc.lower()
    if "swiggy" in desc or "food" in desc:
        return "Food"
    elif "uber" in desc:
        return "Transport"
    elif "amazon" in desc:
        return "Shopping"
    elif "salary" in desc:
        return "Income"
    else:
        return "Other"

df["category"] = df["description"].apply(categorize)

# Streamlit UI
st.title("💸 Expense Tracker")

st.write("### Data Preview")
st.dataframe(df)

# Summary
summary = df.groupby("category")["amount"].sum()

st.write("### Category Summary")
st.bar_chart(summary)
