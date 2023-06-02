import streamlit as st

st.header("Contactez-moi !")

with st.form(key="email_forms"):
    user_email = st.text_input("Votre Adresse Email")
    message = st.text_area("Votre message")
    submit_btn = st.form_submit_button("Envoyer")

    if submit_btn:
        print("send")