from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
  sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser_2 = PydanticOutputParser(pydantic_object=Feedback)

prompt_1 = PromptTemplate(
  template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
  input_variables=['feedback'],
  partial_variables={'format_instruction':parser_2.get_format_instructions()}
)

classifier_chain = prompt_1 | model | parser_2

prompt_2 = PromptTemplate(
  template='Write an appropriate response to this positive feedback \n {feedback}',
  input_variables=['feedback']
)

prompt_3 = PromptTemplate(
  template='Write an appropriate response to this negative feedback \n {feedback}',
  input_variables=['feedback']
)

branch_chain = RunnableBranch(
  (lambda x: x.sentiment == 'positive', prompt_2 | model | parser),
  (lambda x: x.sentiment == 'negative', prompt_3 | model | parser),
  RunnableLambda(lambda x: "Could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a worst phone'}))
print("\n#################\n")
print(chain.invoke({'feedback': 'This is a best phone'}))

print("\n#################\n")
print("Graph of the chain:")
chain.get_graph().print_ascii()
