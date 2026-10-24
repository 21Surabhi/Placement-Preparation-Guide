import streamlit as st
from database import add_resource

st.title("Add Resource")

st.divider()

company = st.selectbox(
    "Select Company",
    ["Google", "Microsoft", "TCS", "Adobe", "Amazon", "Oracle"]
)

title = st.text_input("Resource Title")

pdf = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if st.button("Save Resource"):

    if not title.strip():
        st.warning("Please enter a resource title.")

    elif pdf is None:
        st.warning("Please upload a PDF.")

    else:
        add_resource(company, title, pdf)
        st.success("Resource added successfully!")