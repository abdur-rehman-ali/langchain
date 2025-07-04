from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv
import json

load_dotenv()

model = ChatOpenAI()

prompt_template_1 = PromptTemplate(
  template='Generate short and simple notes from the following text \n {text}',
  input_variables=['text']
)

prompt_template_2 = PromptTemplate(
  template='Generate 5 short question answers from the following text \n {text}',
  input_variables=['text']
)

prompt_template_3 = PromptTemplate(
  template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
  input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
  {
    "notes": prompt_template_1 | model | parser,
    "quiz": prompt_template_2 | model | parser
  }
)


text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""


merge_chain = prompt_template_3 | model | parser

chain = parallel_chain | merge_chain

response = chain.invoke({"text": text})

print("Response:", response)

print("\n#################\n")
print("Graph of the chain:")
chain.get_graph().print_ascii()
