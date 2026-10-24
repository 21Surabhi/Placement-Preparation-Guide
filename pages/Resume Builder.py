import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from io import BytesIO
from xml.sax.saxutils import escape

st.set_page_config(page_title="Resume Builder", layout="wide")

st.title("Resume Builder")
st.write("Create a professional resume for your placement applications.")

with st.form("resume_form"):
    st.subheader("Personal Information")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")
    location = st.text_input("Location")
    objective = st.text_area("Career Objective", height=100)

    st.subheader("Education")

    college = st.text_input("College / University")
    degree = st.text_input("Degree and Branch")
    graduation_year = st.text_input("Graduation Year")
    cgpa = st.text_input("CGPA / Percentage")

    st.subheader("Skills")

    skills = st.text_area(
        "Technical Skills",
        placeholder="Python, Java, SQL, HTML, CSS"
    )

    st.subheader("Projects")

    project1 = st.text_input("Project 1 Name")
    project1_desc = st.text_area("Project 1 Description", height=80)

    project2 = st.text_input("Project 2 Name")
    project2_desc = st.text_area("Project 2 Description", height=80)

    st.subheader("Internships and Experience")

    experience = st.text_area(
        "Internship / Work Experience",
        placeholder="Role, company, duration and responsibilities",
        height=120
    )

    st.subheader("Certifications and Achievements")

    certifications = st.text_area(
        "Certifications",
        placeholder="Certification name and issuing organization",
        height=80
    )

    achievements = st.text_area(
        "Achievements / Extracurricular Activities",
        height=80
    )

    submitted = st.form_submit_button(
        "Generate Resume",
        type="primary",
        use_container_width=True
    )

if submitted:
    if not name.strip() or not email.strip():
        st.error("Please enter at least your name and email address.")
    else:
        st.session_state["resume_data"] = {
            "name": name.strip(),
            "email": email.strip(),
            "phone": phone.strip(),
            "linkedin": linkedin.strip(),
            "github": github.strip(),
            "location": location.strip(),
            "objective": objective.strip(),
            "college": college.strip(),
            "degree": degree.strip(),
            "graduation_year": graduation_year.strip(),
            "cgpa": cgpa.strip(),
            "skills": skills.strip(),
            "project1": project1.strip(),
            "project1_desc": project1_desc.strip(),
            "project2": project2.strip(),
            "project2_desc": project2_desc.strip(),
            "experience": experience.strip(),
            "certifications": certifications.strip(),
            "achievements": achievements.strip()
        }

if "resume_data" in st.session_state:
    data = st.session_state["resume_data"]

    st.divider()
    st.subheader("Resume Preview")

    st.markdown(f"# {data['name']}")

    contact = [
        data["email"],
        data["phone"],
        data["location"],
        data["linkedin"],
        data["github"]
    ]
    st.write(" | ".join(item for item in contact if item))

    if data["objective"]:
        st.markdown("### Career Objective")
        st.write(data["objective"])

    if any(data[key] for key in ["college", "degree", "graduation_year", "cgpa"]):
        st.markdown("### Education")
        if data["degree"]:
            st.write(f"**Degree:** {data['degree']}")
        if data["college"]:
            st.write(f"**Institution:** {data['college']}")
        if data["graduation_year"]:
            st.write(f"**Graduation Year:** {data['graduation_year']}")
        if data["cgpa"]:
            st.write(f"**CGPA / Percentage:** {data['cgpa']}")

    if data["skills"]:
        st.markdown("### Technical Skills")
        st.write(data["skills"])

    if data["project1"] or data["project1_desc"]:
        st.markdown("### Projects")
        if data["project1"]:
            st.markdown(f"**{data['project1']}**")
        if data["project1_desc"]:
            st.write(data["project1_desc"])

    if data["project2"] or data["project2_desc"]:
        if data["project2"]:
            st.markdown(f"**{data['project2']}**")
        if data["project2_desc"]:
            st.write(data["project2_desc"])

    if data["experience"]:
        st.markdown("### Internships and Experience")
        st.write(data["experience"])

    if data["certifications"]:
        st.markdown("### Certifications")
        st.write(data["certifications"])

    if data["achievements"]:
        st.markdown("### Achievements and Activities")
        st.write(data["achievements"])

    def create_pdf(data):
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=45,
            leftMargin=45,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(
            name="ResumeName",
            parent=styles["Title"],
            alignment=TA_CENTER,
            textColor=colors.HexColor("#163A5F"),
            fontSize=20,
            leading=24,
            spaceAfter=8
        ))
        styles.add(ParagraphStyle(
            name="ResumeSection",
            parent=styles["Heading2"],
            textColor=colors.HexColor("#163A5F"),
            fontSize=12,
            leading=15,
            spaceBefore=10,
            spaceAfter=5
        ))
        styles.add(ParagraphStyle(
            name="ResumeBody",
            parent=styles["BodyText"],
            fontSize=9,
            leading=13,
            spaceAfter=4
        ))

        story = []

        def add_text(value, style="ResumeBody"):
            if value:
                safe_value = escape(value).replace("\n", "<br/>")
                story.append(Paragraph(safe_value, styles[style]))
                story.append(Spacer(1, 3))

        def add_section(title, values):
            values = [value for value in values if value]
            if values:
                story.append(Paragraph(title, styles["ResumeSection"]))
                for value in values:
                    add_text(value)

        story.append(Paragraph(escape(data["name"]), styles["ResumeName"]))

        contact = [
            data["email"],
            data["phone"],
            data["location"],
            data["linkedin"],
            data["github"]
        ]
        add_text(" | ".join(item for item in contact if item))

        add_section("CAREER OBJECTIVE", [data["objective"]])

        education = []
        if data["degree"]:
            education.append(data["degree"])
        if data["college"]:
            education.append(data["college"])
        if data["graduation_year"]:
            education.append("Graduation Year: " + data["graduation_year"])
        if data["cgpa"]:
            education.append("CGPA / Percentage: " + data["cgpa"])
        add_section("EDUCATION", education)

        add_section("TECHNICAL SKILLS", [data["skills"]])

        projects = []
        if data["project1"]:
            projects.append(data["project1"])
        if data["project1_desc"]:
            projects.append(data["project1_desc"])
        if data["project2"]:
            projects.append(data["project2"])
        if data["project2_desc"]:
            projects.append(data["project2_desc"])
        add_section("PROJECTS", projects)

        add_section("INTERNSHIPS AND EXPERIENCE", [data["experience"]])
        add_section("CERTIFICATIONS", [data["certifications"]])
        add_section("ACHIEVEMENTS AND ACTIVITIES", [data["achievements"]])

        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()

    pdf_bytes = create_pdf(data)

    st.download_button(
        label="Download Resume as PDF",
        data=pdf_bytes,
        file_name="my_resume.pdf",
        mime="application/pdf",
        type="primary",
        use_container_width=True
    )
