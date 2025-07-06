
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='6_Document_Loaders/documents',
    glob='*.pdf',
    loader_cls=PyPDFLoader,
    show_progress=True,
)

# docs = loader.load()
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
    print(document.page_content)
    print("--------------------------------")
