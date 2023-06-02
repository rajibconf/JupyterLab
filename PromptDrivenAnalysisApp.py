"""
!pip install streamlit pandasai python-dotenv pdfplumber
"""
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import pdfplumber

load_dotenv()

API_KEY = os.environ["OPENAI_API_KEY"]
llm = OpenAI(api_token=API_KEY)
pandas_ai = PandasAI(llm)


def read_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text


# Function to check if the entered username and password are valid
def authenticate(username, password):
    # Add your authentication logic here
    # For example, you can check against a database of users or use hardcoded values for demonstration purposes
    if username == "admin" and password == "password":
        return True
    else:
        return False


st.title("Prompt-driven analysis")

# Check if the user is logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    # Check if the login button is clicked
    if login_button:
        # Authenticate the user
        if authenticate(username, password):
            st.success("Login successful!")
            session_state = st.session_state
            session_state.logged_in = True
            st.experimental_rerun()  # Rerun the app to update the layout after successful login
        else:
            st.error("Invalid username or password!")
else:
    uploaded_file = st.file_uploader("Upload a file for analysis", type=['csv', 'pdf'])

    # Rest of the app's functionality
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
            st.write(df.head(3))
            prompt = st.text_area("Enter your prompt:")
            if st.button("Generate"):
                if prompt:
                    with st.spinner("Generation response..."):
                        result = pandas_ai.run(df, prompt=prompt)
                        st.write(result)
                else:
                    st.warning("Please enter a prompt.")
        elif file_extension == "pdf":
            text = read_pdf(uploaded_file)
            st.write(text[:500])
            prompt = st.text_area("Enter your prompt:")
            if st.button("Generate"):
                if prompt:
                    with st.spinner("Generation response..."):
                        result = pandas_ai.run(pd.DataFrame({'Text': [text]}), prompt=prompt)
                        st.write(result)
                else:
                    st.warning("Please enter a prompt.")
        else:
            st.error("Invalid file format. Only CSV and PDF files are supported.")
    else:
        st.warning("Please upload a file.")

# Create a sidebar
st.sidebar.markdown("---")

# Add copyright text in the sidebar
st.sidebar.markdown("© 2023 Tiger Park Limited. All rights reserved.")

