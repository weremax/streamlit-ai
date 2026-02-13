import streamlit as st
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="Quick Chat")
st.title("Quick Chat")

model = OllamaLLM(model="qwen2.5-coder:1.5b")

def generate_response(input_text):
  st.info(model.invoke(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'Provide react code for a component that would render data from an axios call.')
  submitted = st.form_submit_button('Submit')
  if submitted:generate_response(text)

