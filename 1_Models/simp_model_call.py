from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(temperature=0.9)
text = "What is the capital of Pakistan?"

response = llm.invoke(text)
print(response)