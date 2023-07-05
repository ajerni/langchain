import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.utilities import SerpAPIWrapper
from langchain.agents import load_tools, initialize_agent, AgentType

import os
os.environ["SERPAPI_API_KEY"] = st.secrets["serpapi_api_key"]

llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=st.secrets["openai_api_key"])

st.header(
    """
:blue[Andi's Streamlit-Langchain-Food-Bot]
"""
)

my_country = st.text_input("Enter country")



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

tools = load_tools(["serpapi"], llm=llm)
get_image_agent = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
bild = get_image_agent.run(f"find one image that shows the meal described as {result} and return the URL to that single image.")

st.write(bild)
