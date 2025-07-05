from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import json

load_dotenv()

response_schemas = [
  ResponseSchema(name="name", type="str", description="Name of the person in uppercase"),
  ResponseSchema(name="email", type="str", description="Email address if available", optional=True),
  ResponseSchema(name="age", type="int", description="Age of the person if available", optional=True),
  ResponseSchema(name="skills", type="List[str]", description="List of technical and professional skills"),
  ResponseSchema(name="qualifications", type="List[str]", description="List of degrees and certifications"),
  ResponseSchema(name="experience", type="List[str]", description="List of professional experiences with durations"),
  ResponseSchema(name="languages", type="List[str]", description="List of languages spoken")
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = parser.get_format_instructions()

prompt_template = """
Extract the following information from the resume text below. 
Return a JSON object with exactly these fields:
- name (uppercase)
- email (if available)
- age (if available)
- skills (list)
- qualifications (list)
- experience (list)
- languages (list)

Resume Text:
{resume_text}

{format_instructions}
"""

resume_text = """
Jimmy King is a Certified Data Scientist with 5 years of experience in machine learning and AI development. 
He is 45 years old. He holds a Master's degree in Computer Science from Stanford University and is proficient 
in Python, TensorFlow, PyTorch, and SQL. His professional experience includes developing predictive models at 
TechCorp (2020-2023) and implementing NLP solutions at DataWorks (2018-2020). Additional skills include data 
visualization, cloud computing (AWS, GCP), and team leadership. Jimmy has published 3 research papers in AI 
conferences and is fluent in English and Spanish.
"""

template = PromptTemplate(
  template=prompt_template,
  input_variables=["resume_text"],
  partial_variables={"format_instructions": format_instructions}
)

model = ChatOpenAI(temperature=0)  # Lower temperature for more consistent results
chain = template | model | parser

try:
  response = chain.invoke({"resume_text": resume_text})
  print(json.dumps(response, indent=2))
except Exception as e:
  print(f"Error: {e}")

# Drawback
# 1. We can't do data validations
