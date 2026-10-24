import streamlit as st
import pymupdf
from database import get_resources, fs

st.title("Company Resources")

if "selected_company" not in st.session_state:
    st.warning("Please select a company from the Company List.")
    st.stop()

company = st.session_state["selected_company"]

st.header(f"{company} - Placement Resources")

st.write(f"Access placement preparation resources for {company}.")

st.divider()

resources = [
    "Interview Preparation",
    "Coding Questions",
    "Interview Experiences",
    "Study Materials",
    "Job Description",
    "Eligibility"
]

selected_resource = st.selectbox("Select a Resource", resources)

st.divider()
st.subheader(selected_resource)

if selected_resource == "Interview Preparation":
    st.write(
        f"Interview preparation resources for {company} "
        "will be displayed here."
    )

elif selected_resource == "Coding Questions":
    st.write(
        f"Coding questions for {company} "
        "will be displayed here."
    )

elif selected_resource == "Interview Experiences":
    st.write(
        f"Interview experiences shared by students "
        f"for {company} will be displayed here."
    )

elif selected_resource == "Study Materials":
    company_resources = get_resources(company)

    if not company_resources:
        st.info(f"No study materials available for {company}.")

    else:
        for resource in company_resources:
            st.write(f"### {resource['title']}")

            file = fs.get(resource["file_id"])
            pdf_bytes = file.read()

            col1, col2 = st.columns(2)

            with col1:
                st.download_button(
                    label="Download PDF",
                    data=pdf_bytes,
                    file_name=file.filename,
                    mime="application/pdf",
                    key=f"download_{resource['file_id']}"
                )

            with col2:
                preview_clicked = st.button(
                    "Preview PDF",
                    key=f"preview_{resource['file_id']}"
                )

            if preview_clicked:
                pdf_document = pymupdf.open(
                    stream=pdf_bytes,
                    filetype="pdf"
                )

                for page_number in range(len(pdf_document)):
                    page = pdf_document.load_page(page_number)
                    pix = page.get_pixmap(
                        matrix=pymupdf.Matrix(1.5, 1.5)
                    )

                    image_bytes = pix.tobytes("png")

                    st.image(
                        image_bytes,
                        caption=f"Page {page_number + 1}",
                        use_container_width=True
                    )

                pdf_document.close()

elif selected_resource == "Job Description":
    st.write(
        f"Job description for {company} "
        "will be displayed here."
    )

elif selected_resource == "Eligibility":
    st.write(
        f"Eligibility criteria for {company} "
        "will be displayed here."
    )

Coding_Questions = {
    "Google": [
        "Arrays and Strings",
        "Linked Lists",
        "Trees and Graphs",
        "Dynamic Programming"
    ],
    "Microsoft": [
        "Linked Lists",
        "Trees and Graphs",
        "Dynamic Programming",
        "Arrays and Strings",
        "Hash Tables and Heaps"
    ],
    "Amazon": [
        "Arrays and Hashing",
        "Linked Lists",
        "Trees and Graphs",
        "Dynamic Programming",
        "Sliding Window and Two Pointers"
    ]
}
