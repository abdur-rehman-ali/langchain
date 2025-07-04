from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI()

prompt_content_1 = "Write a detailed report on {topic} in 100 words."

prompt_template_1 = PromptTemplate(
  input_variables=["topic"],
  template=prompt_content_1
)

prompt_1 = prompt_template_1.invoke({
  "topic": "Cricket"
})

reponse_1 = chat_model.invoke(prompt_1)

prompt_content_2 =  "Write a summary of this report in 50 words: {report}"

prompt_template_2 = PromptTemplate(
  input_variables=["report"],
  template=prompt_content_2
)

prompt_2 = prompt_template_2.invoke({
  "report": reponse_1.content
})

reponse_2 = chat_model.invoke(prompt_2)

print("Report: ", reponse_1.content)
print("################################")
print("Summary: ", reponse_2.content)
