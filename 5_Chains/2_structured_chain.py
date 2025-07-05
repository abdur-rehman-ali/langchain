from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(temperature=0)  # Lower temperature for more consistent results

prompt_template_1 = PromptTemplate(
  template="Generate a detailed report about {topic}.",
  input_variables=["topic"],
)

prompt_template_2 = PromptTemplate(
  template="Write summary of {topic}.",
  input_variables=["topic"],
)

parser = StrOutputParser()

chain = prompt_template_1 | model | parser | prompt_template_2 | model | parser
response = chain.invoke({"topic": "programming"})
print("Response:", response)

print("#################")
print("Graph of the chain:")
chain.get_graph().print_ascii()
