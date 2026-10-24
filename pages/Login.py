import streamlit as st

st.title("Login")
st.write("Enter your credentials")

with st.form("login_form"):
    role = st.selectbox("Login as", ["Student", "Admin"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

if submitted:
    if not email.strip() or not password:
        st.error("Please enter both email and password.")

    elif role == "Admin":
        if email == "admin@placement.com" and password == "admin123":
            st.session_state["logged_in"] = True
            st.session_state["role"] = "Admin"
            st.session_state["email"] = email
            st.switch_page("pages/Company List.py")
        else:
            st.error("Invalid admin email or password.")

    elif role == "Student":
        if email == "student@placement.com" and password == "student123":
            st.session_state["logged_in"] = True
            st.session_state["role"] = "Student"
            st.session_state["email"] = email
            st.switch_page("pages/Home.py")
        else:
            st.error("Invalid student email or password.")

if st.session_state.get("logged_in"):
    st.write(f"Logged in as: {st.session_state['role']}")
