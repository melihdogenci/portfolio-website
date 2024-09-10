import streamlit as st
from send_email import send_email

st.title("Contact Me")

with st.form(key='my_form'):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New email from {user_email}
Content-Type: text/plain; charset=utf-8

From: {user_email}
{raw_message}

"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email sent!")