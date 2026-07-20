import streamlit as st


st.set_page_config(
    page_title="AI Resume Intelligence Platform",
    page_icon="📄",
    layout="wide",
)


st.title("📄 AI Resume Intelligence Platform")

st.markdown(
    """
    Upload your resume and paste a job description.

    The application will eventually analyze:

    - Resume skills
    - Matching skills
    - Missing skills
    - Job compatibility score
    - Resume improvement suggestions
    """
)

st.divider()

resume_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"],
)

job_description = st.text_area(
    "Paste the job description",
    height=250,
    placeholder="Paste the complete job description here...",
)

analyze_button = st.button(
    "🚀 Analyze Resume",
    type="primary",
    use_container_width=True,
)

if analyze_button:
    if resume_file is None:
        st.error("Please upload a resume.")

    elif not job_description.strip():
        st.error("Please paste a job description.")

    else:
        st.success("Resume and job description received successfully.")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="Uploaded File",
                value=resume_file.name,
            )

        with col2:
            st.metric(
                label="Job Description Characters",
                value=len(job_description),
            )

        st.info(
            "The document analysis engine will be added in the next milestone."
        )