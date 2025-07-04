from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI()

prompt_template_1 = PromptTemplate(
  input_variables=["topic"],
  template="Write a detailed report on {topic} in 100 words."
)

prompt_template_2 = PromptTemplate(
  input_variables=["report"],
  template="Write a summary of this report in 50 words: {report}"
)

parser = StrOutputParser()

chain = prompt_template_1 | chat_model | parser | prompt_template_2 | chat_model | parser

response = chain.invoke({
  "topic": "Cricker"
})

print("Summary: ", response)
