from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("6_Document_Loaders/documents/sample-langchain.pdf")
documents = loader.load()
print(len(documents))

print(documents)
