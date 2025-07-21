import streamlit as st
import google.generativeai as genai

# Configure Gemini with Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="AI Workflow Assistant", page_icon="🤖", layout="centered")
st.title("🤖 AI Skill & Job Workflow Assistant")

goal = st.text_input("Enter your career goal (e.g., Get a software engineer job):")
skills = st.text_area("Enter skills you want to learn (comma separated):")
experience = st.selectbox("Experience Level:", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Workflow"):
    with st.spinner("Creating your workflow..."):
        prompt = f"""
        You are an AI Workflow Assistant. 
        The user's career goal: {goal}
        Skills to learn: {skills}
        Experience Level: {experience}

        Create a 4-week learning & job-application workflow. 
        Break it into weekly tasks and give job/courses recommendations.
        Format it in a neat table.
        """
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        st.subheader("📌 Your Personalized Workflow")
        st.markdown(response.text)
