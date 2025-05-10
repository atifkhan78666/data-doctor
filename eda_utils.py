import streamlit as st

def generate_report(df):
    st.write("*Rows, Columns:*", df.shape)
    st.write("**Column Types:**")
    st.write(df.dtypes)
    st.write("**Missing Data (%):**")
    missing_percent = (df.isnull().sum() / len(df)) * 100
    st.write(missing_percent)


