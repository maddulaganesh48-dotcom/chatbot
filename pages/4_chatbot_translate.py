import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')
#print(google_api_key)
genai.configure(api_key=google_api_key)

#llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=google_api_key)

llm = genai.GenerativeModel('gemini-1.5-pro-latest')

st.set_page_config(page_title="Chatbot Text Demo", page_icon="📈")

st.title("Chatbot Text Demo")
st.sidebar.header("Chatbot Text Demo")

st.divider()

with st.container():

    col1, col2, col3 = st.columns(3)

    query = ""

    with col1 and col2 and col3:
        query = st.text_area('Text', placeholder="Enter your text here")
        btn = st.button('Translate')
        if btn:
            response = llm.generate_content(query) 
            st.text_area(response.text)
