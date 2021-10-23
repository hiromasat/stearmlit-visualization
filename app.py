import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Streamlit Demo")
st.subheader("by H. T.")

df = px.data.iris()
st.write(df)
st.write(px.scatter(df, x="sepal_length", y="sepal_width", color="species"))