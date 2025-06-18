import os
import secret_key
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

llm = ChatGroq(
    groq_api_key=secret_key.GROQ_API_KEY,
    model_name="llama3-8b-8192", 
    temperature=0.6
)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want a restaurant name for {cuisine} food, suggest me bestest fancy name")
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables =['restaurant_name'],
        template="""Suggest some menu items for {restaurant_name}.""")
    
    food_items_chain =LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")

    chain = SequentialChain(
        chains = [name_chain,food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name','menu_items'])

    response = chain({'cuisine':cuisine})
    
    return response


if __name__=="__main__":
    print(generate_restaurant_name_and_items("Indian"))

