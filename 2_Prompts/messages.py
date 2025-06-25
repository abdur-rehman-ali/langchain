from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

chat_model = ChatOpenAI()

messages = [
  SystemMessage(content="You are a helpful assistant that provides information and answers questions."),
  HumanMessage(content="What is the capital of France?"),
]

response = chat_model.invoke(messages)
messages.append(AIMessage(content=response.content))
print("AI: ", response.content)

print("Chat History:")
for message in messages:
  print(f"{message}")
