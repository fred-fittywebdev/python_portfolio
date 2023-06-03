import streamlit as st
from send_email import send_email

st.header("Contactez-moi !")

with st.form(key="email_forms"):
    user_email = st.text_input("Votre Adresse Email")
    raw_message = st.text_area("Votre message")
    message = f"""\
Sujet: Nouvel email de {user_email}

From: {user_email}
{raw_message}
"""
    submit_btn = st.form_submit_button("Envoyer")

    if submit_btn:
        send_email(message)
        st.success("Votre email a bien été envoyé. Merci.")