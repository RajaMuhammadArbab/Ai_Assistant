import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def data_analysis_ui():
    st.header("📊 Upload and Analyze CSV Data")
    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.write("📋 Preview", df.head())
        st.write("📈 Summary", df.describe())

        col = st.selectbox("Select a column to visualize", df.columns)
        if df[col].dtype in ["int64", "float64"]:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            st.pyplot(fig)
