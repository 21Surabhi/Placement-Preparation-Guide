import streamlit as st

left, right = st.columns([8, 1])

with right:
    if st.button(
        "Login",
        key="home_login",
        use_container_width=True
    ):
        st.switch_page("pages/Login.py")

st.write("")


st.markdown("""
<div class="hero">
<div class="hero-title">
Placement Preparation Portal
</div>
<div class="hero-text">
Your one-stop platform for campus placement preparation.<br>
Explore companies, opportunities and resources to prepare
for your placement journey.
</div>
</div>
""", unsafe_allow_html=True)

st.header("Companies")

st.write(
    "Explore companies visiting campus and access "
    "company-specific placement information and resources."
)


with st.container(border=True):
    st.subheader("List of Companies")

    st.write(
        "View arrival dates, vacancies, job roles, CTC "
        "information and company-specific preparation resources."
    )

    if st.button(
        "View List of Companies →",
        key="home_companies",
        use_container_width=True
    ):
        st.switch_page("pages/Company List.py")
