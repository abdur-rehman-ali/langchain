from langchain_community.document_loaders import CSVLoader
import os


def load_csv_basic(csv_path):
    """
    Basic CSV loading example
    """
    print("=== Basic CSV Loading ===")

    loader = CSVLoader(
        file_path=csv_path,
        encoding="utf-8"
    )

    documents = loader.load()

    print(f"Number of documents loaded: {len(documents)}")
    print(f"First document content: {documents[0].page_content}")
    print(f"First document metadata: {documents[0].metadata}")
    print()


if __name__ == "__main__":
    csv_path = "6_Document_Loaders/documents/sample.csv"
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found!")
        print("Please make sure the CSV file exists in the documents directory.")
    else:
        load_csv_basic(csv_path)
        print("CSV loading completed successfully!")
