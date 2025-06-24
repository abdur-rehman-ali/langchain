from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large')

query = "What is the capital of Pakistan?"
response = embedding.embed_query(query)

print(str(response))
