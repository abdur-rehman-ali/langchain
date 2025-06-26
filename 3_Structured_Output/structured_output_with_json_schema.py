from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List, Optional
from dotenv import load_dotenv
import json

load_dotenv()

# JSON Schema equivalent of your ResumeModel
resume_schema = {
    "title": "Resume",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Name of the person in uppercase"
        },
        "email": {
            "type": ["string", "null"],
            "description": "Email address if available"
        },
        "age": {
            "type": ["integer", "null"],
            "description": "Age of the person if available"
        },
        "skills": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List of technical and professional skills"
        },
        "qualifications": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List of degrees and certifications"
        },
        "experience": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List of professional experiences with durations"
        },
        "languages": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List of languages spoken"
        }
    },
    "required": ["name", "skills", "qualifications", "experience", "languages"]
}

prompt = """Jimmy king is a Certified Data Scientist with 5 years of experience in machine learning and AI development. I am 45 year old. He holds a Master's degree in Computer Science from Stanford University and is proficient in Python, TensorFlow, PyTorch, and SQL. His professional experience includes developing predictive models at TechCorp (2020-2023) and implementing NLP solutions at DataWorks (2018-2020). Additional skills include data visualization, cloud computing (AWS, GCP), and team leadership. John has published 3 research papers in AI conferences and is fluent in English and Spanish."""

model = ChatOpenAI(model='gpt-4o-2024-08-06')
structured_model = model.with_structured_output(resume_schema)
response = structured_model.invoke(prompt)

# Convert response to pretty-printed JSON
print(json.dumps(response, indent=2))
