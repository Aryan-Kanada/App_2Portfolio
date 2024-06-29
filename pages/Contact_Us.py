import streamlit as st

st.header("Contact US")

with st.form(key="contact_forms"):
    user_email = st.text_input("Your Email Address")
    user_message = st.text_area("Your Message")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    print("Pressed!!")