
import streamlit as st
from src.analyzer import run_analysis

st.title("Security SIEM Dashboard")

file = "data/sample_logs.csv"
df = run_analysis(file)

st.subheader("High Risk Alerts")
alerts = df[df['risk_score'] >= 6]
st.write(alerts)

st.subheader("Risk Score Distribution")
st.bar_chart(df['risk_score'].value_counts())

st.subheader("Raw Data")
st.write(df.head())
