from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model='gpt-4')
prompt = "Explain Gen AI in simple way?"

response = chat_model.invoke(prompt)

print(response.content)