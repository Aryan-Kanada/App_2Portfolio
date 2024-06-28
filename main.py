import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\Photo.png",)

with col2:
    st.title("Aryan Kanada")
    content1 = """
    Hi Myself Aryan Kanada
    """
    st.info(content1)

content2 = """
Below you can find some of app I have built in Python. Fell free to content me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:11].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[11:].iterrows():
        st.header(row["title"])



