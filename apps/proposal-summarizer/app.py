import streamlit as st
import pandas as pd
from pypdf import PdfReader

st.title("Proposal Summarizer")

uploaded = st.file_uploader("Upload PDF", type="pdf")
if uploaded:
    reader = PdfReader(uploaded)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    st.subheader("Extracted Text")
    st.write(text[:1000])
    st.subheader("Word Count")
    st.write(len(text.split()))
else:
    st.write("Upload a PDF to summarize.")
