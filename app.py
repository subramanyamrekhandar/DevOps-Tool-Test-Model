import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Verify API key availability
if not openai.api_key:
    st.error("OpenAI API key is missing. Please configure it in the environment variables.")
else:
    # Sidebar
    st.sidebar.title("DevOps Chatbot")
    option = st.sidebar.selectbox(
        "Choose Assistance",
        ("Terraform Generator", "YAML Generator", "Error Debugger")
    )

    # Chat Interface
    st.title("DevOps Assistant Chatbot")
    user_input = st.text_input("Ask me anything about Terraform or YAML:")

    if st.button("Generate"):
        if user_input:
            try:
                # Use openai.ChatCompletion for generating responses
                response = openai.ChatCompletion.create(
                    model="gpt-4",  # Use the appropriate model
                    messages=[
                        {"role": "system", "content": f"You are a helpful assistant specializing in {option}."},
                        {"role": "user", "content": f"Generate {option} code: {user_input}"}
                    ],
                    max_tokens=150
                )
                language = 'yaml' if 'YAML' in option else 'json'
                st.code(response['choices'][0]['message']['content'], language=language)
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
