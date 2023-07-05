import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

st.header("""
:blue[Andi's Streamlit-Langchain-Food-Bot]
""")

my_country = st.text_input("Enter country")

llm = OpenAI(model_name='gpt-3.5-turbo', openai_api_key=st.secrets["openai_api_key"])

template = """
let me know a typical meal from {country}.
Respond in one short sentence.
"""

prompt = PromptTemplate(
    input_variables=["country"],
    template=template,
)

final_prompt = prompt.format(country=my_country)

result = llm(final_prompt)

st.write(":blue[Here comes a typical meal of the country you entered:]")

st.write(result)