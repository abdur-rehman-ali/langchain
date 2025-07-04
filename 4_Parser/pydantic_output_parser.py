from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

class ResumeModel(BaseModel):
  name: str = Field(description="Name of the person in uppercase")
  email: Optional[str] = Field(None, description="Email address if available")
  age: Optional[int] = Field(None, description="Age of the person if available")
  skills: List[str] = Field(description="List of technical and professional skills")
  qualifications: List[str] = Field(description="List of degrees and certifications")
  experience: List[str] = Field(description="List of professional experiences with durations")
  languages: List[str] = Field(description="List of languages spoken")

prompt = "Jimmy king is a Certified Data Scientist with 5 years of experience in machine learning and AI development. I am 45 year old. He holds a Master's degree in Computer Science from Stanford University and is proficient in Python, TensorFlow, PyTorch, and SQL. His professional experience includes developing predictive models at TechCorp (2020-2023) and implementing NLP solutions at DataWorks (2018-2020). Additional skills include data visualization, cloud computing (AWS, GCP), and team leadership. John has published 3 research papers in AI conferences and is fluent in English. {format_instructions}"

parser = PydanticOutputParser(pydantic_object=ResumeModel)

template = PromptTemplate(
  template=prompt,
  input_variables=[],
  partial_variables={"format_instructions": parser.get_format_instructions()}
)

model = ChatOpenAI()

chain = template | model | parser

response = chain.invoke({})

print(response)
