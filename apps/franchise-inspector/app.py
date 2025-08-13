import streamlit as st
import pandas as pd
from io import StringIO

st.title("Franchise Inspector")

data = st.text_area("Paste CSV data", height=200)
if data:
    df = pd.read_csv(StringIO(data))
    st.write("Preview")
    st.dataframe(df.head())
    st.write("Summary")
    st.write(df.describe())
else:
    st.write("Paste CSV data to inspect.")
