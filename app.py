import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.utilities import SerpAPIWrapper

import os
os.environ["SERPAPI_API_KEY"] = st.secrets["serpapi_api_key"]

def get_image(query_text):

    serpapi = SerpAPIWrapper()

    search_result = serpapi.run(query_text, num_images=1)

    #image_url = search_result["images"][0]["url"]
    image_url = search_result

    return image_url

st.header(
    """
:blue[Andi's Streamlit-Langchain-Food-Bot]
"""
)

my_country = st.text_input("Enter country")

llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=st.secrets["openai_api_key"])

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

resulting_image = get_image(result)

print(resulting_image)

st.write(resulting_image)
