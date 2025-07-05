from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# Quickest way to get JSON output
parser = JsonOutputParser()

template = PromptTemplate(
  template="Give me name, age and country of a person. {format_instructions}",
  input_variables=[],
  partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Example of using the template and parser
prompt = template.format()
response = model.invoke(prompt)
parsed_response = parser.parse(response.content)
print("Response: ", parsed_response)

# Example of using the template, model, and parser in a chain
chain = template | model | parser
response = chain.invoke({})
print("Response using chains: ", response)

# Drawback
# 1. We can't enforce a schema for the JSON output.