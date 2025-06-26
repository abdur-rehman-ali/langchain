from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

class ResumeType(TypedDict):
  name: str
  email: str
  skills: list[str]
  qualifications: list[str]
  experience: list[str]
  languages: list[str]


prompt = """John Doe is a Certified Data Scientist with 5 years of experience in machine learning and AI development. He holds a Master's degree in Computer Science from Stanford University and is proficient in Python, TensorFlow, PyTorch, and SQL. His professional experience includes developing predictive models at TechCorp (2020-2023) and implementing NLP solutions at DataWorks (2018-2020). Additional skills include data visualization, cloud computing (AWS, GCP), and team leadership. John has published 3 research papers in AI conferences and is fluent in English and Spanish."""

model = ChatOpenAI()
with_structured_output = model.with_structured_output(ResumeType)
response = with_structured_output.invoke(prompt)

print(response)
