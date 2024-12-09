import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama


load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')
print(google_api_key)

llm = ChatGoogleGenerativeAI(model="gemini-vision-pro", api_key=google_api_key)

while True:
    print('#'*60)
    query = input("Enter the Query: ")
    result = llm.invoke(query)
    print(result.content)
    print('#'*60)
