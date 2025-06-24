from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model='gpt-4')
dynamic_prompt = "Explain {topic} like I am {age} year child?"

prompt_template = PromptTemplate(
    input_variables=["topic", "age"],
    template=dynamic_prompt
)

prompt = prompt_template.format(topic="Gen AI", age=5)
response = chat_model.invoke(prompt)

print(response.content)