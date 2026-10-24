import streamlit as st

st.set_page_config(
    page_title="Placement Preparation Portal",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

[data-testid="stSidebar"] {
    background-color: #20232d;
    border-right: 1px solid #343946;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 0.8rem;
}

[data-testid="stSidebarNav"] {
    padding: 0.5rem 0.65rem 1rem 0.65rem;
}

[data-testid="stSidebarNav"] a {
    border-radius: 8px;
    margin: 3px 0;
    padding: 0.55rem 0.75rem;
    transition: background-color 0.2s ease;
}

[data-testid="stSidebarNav"] a:hover {
    background-color: #303747;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: #354057;
    border-left: 3px solid #91aefc;
    border-radius: 8px;
}

[data-testid="stSidebarNav"] span {
    font-size: 0.92rem;
}

.stButton > button {
    border: 1px solid #454c5c;
    border-radius: 9px;
    min-height: 42px;
    font-weight: 500;
    transition: border-color 0.2s ease;
}

.stButton > button:hover {
    border-color: #91aefc;
}

.hero {
    padding: 45px 30px;
    text-align: center;
    border-radius: 18px;
    background: linear-gradient(135deg, #1b2334, #151922);
    border: 1px solid #303b50;
    margin: 12px 0 35px 0;
}

.hero-title {
    font-size: clamp(28px, 4vw, 42px);
    font-weight: 700;
    color: #f5f7ff;
    margin-bottom: 12px;
}

.hero-text {
    font-size: 17px;
    color: #b8c3d6;
    line-height: 1.8;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #f5f7ff;
    margin-bottom: 5px;
}

.section-text {
    color: #b8c3d6;
    font-size: 16px;
    margin-bottom: 20px;
}

.company-card {
    padding: 28px;
    border-radius: 16px;
    border: 1px solid #343946;
    background-color: #20232d;
    margin-top: 15px;
    margin-bottom: 15px;
}

.company-icon {
    font-size: 35px;
}

.company-heading {
    font-size: 22px;
    font-weight: 650;
    color: #f5f7ff;
    margin-top: 8px;
}

.company-description {
    color: #b8c3d6;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 5px;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)


home = st.Page(
    "pages/Home.py",
    title="Home",
    default=True
)

companies = st.Page(
    "pages/Company List.py",
    title="Companies"
)

resume = st.Page(
    "pages/Resume Builder.py",
    title="Resume Builder"
)

login = st.Page(
    "pages/Login.py",
    title="Login"
)

company_resources = st.Page(
    "pages/Company Resources.py",
    title="Company Resources"
)

add_company = st.Page(
    "pages/Add Company.py",
    title="Add Company"
)

pg = st.navigation(
    [
        home,
        companies,
        resume,
        login,
        company_resources,
        add_company
    ],
    position="sidebar",
    expanded=True
)

pg.run()

