from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
chat_model = ChatOpenAI(model='gpt-4')

text = "What is 2 + 2?"
response = chat_model.invoke(text)

print(response.content)