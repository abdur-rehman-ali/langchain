from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')
text = "Explain Gen AI in simple way?"

response = llm.invoke(text)
print(response)

