import streamlit as st

# Create title of the page
st.title("Hello! I am Archisman")

with st.container():
    # Create two columns
    col1, col2 = st.columns([2, 1])
    # Add content to the left column
    with col1:
        # Say about yourself
        st.markdown(
            """
            <div style="text-align: justify;">
                <p>
                I am an aspiring Analyst who possesses a strong passion for strategic thinking. 
                My expertise lies in dissecting complex problems, extracting valuable insights from data, 
                and translating those insights into effective strategies. With a solid foundation in analytical 
                methodologies and a dedication to staying up-to-date with industry advancements, I am equipped 
                to drive data-informed decision-making and deliver results. My exceptional communication and 
                collaboration skills enhance the ability to convey insights and recommendations to stakeholders.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        # create a button to download resume
        resume_pdf_path = "resume.pdf"  # Replace with the actual filename and format
        # Provide the PDF file path for download
        st.download_button(
            label="Download Resume",
            data=resume_pdf_path,
            file_name="resume.pdf",
            mime="application/pdf"
        )
    # Add content to the right column
    with col2:
        # Add image of yours
        image = "image1.JPG"  # Replace with the path to your image file
        st.image(image)

with st.container():
    # Create two columns
    col1, col2 = st.columns([1, 1])
    # Add content to the left column
    with col1:
        # Add image that describes education
        image = "education.jpg"  # Replace with the path to your image file
        st.image(image)
    # Add content to the right container
    with col2:
        # Create a header
        st.header("Education")
        # Say about education
        st.markdown(
            """
            - Class X (CISCE): 86%
            - Class XII (CBSE):  85%
            - Graduation-B.Sc (CU): 7.88 (CGPA)
            - Masters-MBA :
            """) 
        st.markdown("<a href='/Education' target='_self' style='text-decoration: none;'>Know More</a>", unsafe_allow_html=True)

with st.container():
    # Create two columns
    col1, col2 = st.columns([1, 1])
    # Add content to the left column
    with col1:
        # Create a header
        st.header("Certifications")
        # Say about certifications
        st.markdown(
            """
            - Excel Certification from University of Michigan.
            - SQL Certification from Duke University.
            - Power BI Certification from Knowledge Accelerators.
            - Python Certification from Google.
            """)
        st.markdown("<a href='/Certifications' target='_self' style='text-decoration: none;'>Know More</a>", unsafe_allow_html=True)
    # Add content to the right column
    with col2:
        # Add image that describes certifications
        image = "certifications.jpg"  # Replace with the path to your image file
        st.image(image)
        

with st.container():
    # Create two columns
    col1, col2 = st.columns([1, 1])
    # Add content to the left column
    with col1:
        # Add image that describes projects
        image = "projects.jpg"  # Replace with the path to your image file
        st.image(image)
    # Add content to the right container
    with col2:
        # Create a header
        st.header("Projects")
        # Say about projects
        st.markdown(
            """
            - Excel Projects: IPL Analysis
            - SQL Projects: Pizza Sales Analysis
            - Power Bi Projects: Virat Kohli's Career Analysis, HR Attrition
            - Python Projects: Prediction Models and Data Analysis projects
            """) 
        st.markdown("<a href='/Projects' target='_self' style='text-decoration: none;'>Know More</a>", unsafe_allow_html=True) 

with st.container():
    # Create two columns
    col1, col2 = st.columns([1, 1])
    # Add content to the left column
    with col1:
        # Create a header
        st.header("Contact")
        # Say about contact
        st.markdown(
            """
            - Email: archismansom1999@gmail.com</a>
            - Phone: +91 83360 42915
            - LinkedIn: [My Profile](https://www.linkedin.com/in/archisman-som-435180205/)
            """
        )
    # Add content to the right container
    with col2:
        # Add image that describes contact
        image = "contact.jpg"  # Replace with the path to your image file
        st.image(image)
        
