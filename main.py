import streamlit as st

st.set_page_config(layout="wide")

col_1, col_2 = st.columns(2)

with col_1:
    st.image("images/photo.png")  # width=500

with col_2:
    st.title("Frédéric Guerra")
    content = """
    Développeur intégrateur web junior. Créatif et innovant, avoir travailler
    pendant 1 an au sein d'un groupe international comme Boardriders me
    permet de créer des sites web et des applications pour des clients de premier
    plan aux demandes et visions complexes. Doté d'excellentes compétences en
    matière d'organisation, de planification et de travail en équipe. Ouvert à de
    nouveaux challenges je souhaite vous apporter mon expertise en
    développement web.
    """
    st.info(content)

content_2 = """
Below you can find some of the apps i have built in Python. Feel free to contact me!
"""

st.write(content_2)
