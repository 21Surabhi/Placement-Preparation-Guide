import streamlit as st
from database import get_companies

col1, col2 = st.columns([8, 1])

with col1:
    st.title("List of Companies")

with col2:
    if st.button("Add"):
        st.switch_page("pages/Add Company.py")

st.write("Explore companies and access placement resources")

st.divider()

saved_companies = get_companies()

companies = [
    {
        "name": company["name"],
        "arrival_date": company["arrival_date"],
        "vacancies": company["vacancies"],
        "role": company["role"],
        "ctc": company["ctc"]
    }
    for company in saved_companies
]

default_companies = [
    {
        "name": "Google",
        "arrival_date": "15 Aug 2026",
        "vacancies": 10,
        "role": "Software Engineer",
        "ctc": "20 LPA"
    },
    {
        "name": "Microsoft",
        "arrival_date": "20 Sep 2026",
        "vacancies": 15,
        "role": "Software Engineer",
        "ctc": "25 LPA"
    },
    {
        "name": "TCS",
        "arrival_date": "",
        "vacancies": "",
        "role": "",
        "ctc": ""
    },
    {
        "name": "Adobe",
        "arrival_date": "",
        "vacancies": "",
        "role": "",
        "ctc": ""
    },
    {
        "name": "Amazon",
        "arrival_date": "5 Sep 2026",
        "vacancies": 30,
        "role": "Software Development Engineer",
        "ctc": "18 LPA"
    },
    {
        "name": "Oracle",
        "arrival_date": "",
        "vacancies": "",
        "role": "",
        "ctc": ""
    }
]

companies = default_companies + [
    company for company in companies
    if company["name"].casefold() not in {
        item["name"].casefold() for item in default_companies
    }
]

col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 1, 1])

with col1:
    st.write("**Company**")

with col2:
    st.write("**Arrival Date**")

with col3:
    st.write("**Vacancies**")

with col4:
    st.write("**Job Role**")

with col5:
    st.write("**CTC**")

with col6:
    st.write("**View**")


for company in companies:

    col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 1, 2, 1, 1])

    with col1:
        st.write(company["name"])

    with col2:
        st.write(company["arrival_date"])

    with col3:
        st.write(str(company["vacancies"]))

    with col4:
        st.write(company["role"])

    with col5:
        st.write(company["ctc"])

    with col6:
        if st.button("View", key=f"view_{company['name']}"):
            st.session_state["selected_company"] = company["name"]
            st.switch_page("pages/Company Resources.py")