from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt_template = PromptTemplate(
  template="Write a summary about the following document {document}",
  input_variables=["document"],
)

parser = StrOutputParser()

loader = TextLoader("6_Document_Loaders/documents/sample.txt")

documents = loader.load()
print("Loaded Documents")
print(documents[0].page_content)
print("######################")

chain = prompt_template | model | parser

response = chain.invoke({"document": documents[0].page_content})

print("######################")
print("Summary:", response)
