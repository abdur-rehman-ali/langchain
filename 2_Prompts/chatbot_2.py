from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []

while True:
  user_input = input('You: ')
  if user_input == 'exit':
    break
  chat_history.append(user_input)
  result = model.invoke(chat_history)
  chat_history.append(result.content)
  print("AI: ",result.content)
  print("################################")


print("Chat History:" + str(chat_history))