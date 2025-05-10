import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from eda_utils import generate_report

st.title("Data Doctor AI Assistant 🚑📊")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Data uploaded successfully!")
    st.write("**Data Preview:**")
    st.dataframe(df.head())

    st.write("**Summary Report:**")
    generate_report(df)

    st.write("**Visualizations:**")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Show Missing Values"):
            st.write(df.isnull().sum())

    with col2:
        if st.button("Show Column Stats"):
            st.write(df.describe())

    st.write("---")
    st.subheader("Custom Graphs 📈")

    if st.checkbox("Show Histogram"):
        column = st.selectbox("Select Column for Histogram", df.columns)
        fig, ax = plt.subplots()
        df[column].hist(ax=ax)
        st.pyplot(fig)

    if st.checkbox("Show Scatter Plot"):
        x_col = st.selectbox("X-axis Column", df.columns)
        y_col = st.selectbox("Y-axis Column", df.columns)
        fig, ax = plt.subplots()
        ax.scatter(df[x_col], df[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)



