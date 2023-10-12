import streamlit as st
import pandas as pd



st.title("Engineering Exams")



df=pd.read_csv("after12th.csv")


df = pd.DataFrame(data)

st.dataframe(df, column_config={"Website": st.column_config.LinkColumn()})



