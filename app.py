import streamlit as st
from langchain import HuggingFaceHub
from apikey import apikey
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = apikey

repo_id = "gpt2"

llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0.9, "max_length":256})

st.title('Gen AI App')

prompt = st.text_input('Enter your prompt')

if prompt:
    st.write(llm(prompt))
