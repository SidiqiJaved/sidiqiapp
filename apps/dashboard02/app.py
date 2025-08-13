import streamlit as st
import pandas as pd

st.title("Dashboard 02")

uploaded = st.file_uploader("Upload CSV", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df)
    numeric_cols = df.select_dtypes("number")
    if not numeric_cols.empty:
        st.line_chart(numeric_cols)
else:
    st.write("Upload a CSV file to visualize.")
