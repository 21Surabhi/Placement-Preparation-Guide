import streamlit as st
from database import add_company

st.title("Add New Company")

st.write("Enter the details of the company visiting campus.")

with st.form("add_company_form"):
    company_name = st.text_input("Company Name")
    arrival_date = st.date_input("Arrival Date")
    vacancies = st.number_input("Number of Vacancies", min_value=1, step=1)
    job_role = st.text_input("Job Role")
    ctc = st.text_input("CTC")

    submitted = st.form_submit_button("Save Company")

    if submitted:
        if company_name.strip() and job_role.strip() and ctc.strip():
            saved = add_company(
                company_name.strip(),
                arrival_date.strftime("%d %b %Y"),
                int(vacancies),
                job_role.strip(),
                ctc.strip()
            )

            if saved:
                st.success(f"{company_name} has been saved successfully!")
            else:
                st.error("A company with this name already exists.")
        else:
            st.error("Please fill in the company name, job role and CTC.")

if st.button("Back to List of Companies"):
    st.switch_page("pages/Company List.py")
