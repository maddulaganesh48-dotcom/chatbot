import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
import tempfile


load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=google_api_key)

llm = genai.GenerativeModel('gemini-1.5-pro-latest')

def process_audio(audio_file_path, user_prompt):
    audio_file = genai.upload_file(audio_file_path)
    response = llm.generate_content([user_prompt, audio_file])
    return response.text

def save_uploaded_file(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        st.error(f"Error handling uploaded file: {e}")
        return None
    
st.set_page_config('Chatbot Application', layout='centered')

st.title('Chatbot Application')

st.divider()

audio_uploader = st.file_uploader('Upload Audio')

if audio_uploader:
    audio_path = save_uploaded_file(audio_uploader)
    print(audio_path)
    st.audio(audio_path)

query = st.text_input('Enter Your Query here..', placeholder='Can you explain about the audio?')

if st.button('Submit'):
    response = process_audio(audio_file_path=audio_path, user_prompt=query)
    st.write(response)