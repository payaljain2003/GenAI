from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

import streamlit as st

def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.getenv("OPEN_API_KEY"), model_name = "text-davinci-003",temperature =0.6 )
    response = llm(question)
    return response

st.set_page_config(page_title = "Q&A Demo")
st.header("Langchain Application")

input = st.text_input("Input : ", key="input")
response = get_openai_response(input)
submit = st.button("Ask the question")

if submit:
    st.subheader("The response is : ")
    st.write(response)