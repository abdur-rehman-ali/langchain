from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt_template = PromptTemplate(
  template="Tell me a joke about {topic}.",
  input_variables=["topic"],
)

parser = StrOutputParser()

chain = prompt_template | model | parser
response = chain.invoke({"topic": "programming"})
print("Response:", response)

print("#################")
print("Graph of the chain:")
chain.get_graph().print_ascii()
