from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

chat_model = ChatOpenAI()

chat_template = ChatPromptTemplate([
  ('system', 'You are a helpful {domain} expert that provides information and answers questions.'),
  ('human', 'Explain this {topic} like I am {age} year child?'),
])

prompt = chat_template.invoke({
  'domain': 'Gen AI',
  'topic': 'Generative AI',
  'age': 5 
})


response = chat_model.invoke(prompt)
chat_template.append(AIMessage(content=response.content))
print("AI: ", response.content)

print(chat_template)

