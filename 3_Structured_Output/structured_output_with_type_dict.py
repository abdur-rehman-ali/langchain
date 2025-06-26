from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional
from dotenv import load_dotenv

load_dotenv()

class ResumeType(TypedDict):
  name: Annotated[str, "Please provide the name of the person in upercase."]
  email: str
  age: Annotated[Optional[int], "Please provide the age of the person, if present in resume and keep it empty if not available."]
  skills: list[str]
  qualifications: list[str]
  experience: list[str]
  languages: list[str]


prompt = """Jimmy king is a Certified Data Scientist with 5 years of experience in machine learning and AI development. I am 45 year old. He holds a Master's degree in Computer Science from Stanford University and is proficient in Python, TensorFlow, PyTorch, and SQL. His professional experience includes developing predictive models at TechCorp (2020-2023) and implementing NLP solutions at DataWorks (2018-2020). Additional skills include data visualization, cloud computing (AWS, GCP), and team leadership. John has published 3 research papers in AI conferences and is fluent in English and Spanish."""

model = ChatOpenAI()
with_structured_output = model.with_structured_output(ResumeType)
response = with_structured_output.invoke(prompt)

print(response)
