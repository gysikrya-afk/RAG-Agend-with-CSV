from langchain_community.document_loaders import CSVLoader
from langchain_classic.schema import Document as LangchainDocument

from typing import List

def csv_loader(file_csv:str) -> List[LangchainDocument]:
    """
    Загрузка CSV файла как список документов | Download CSV files how list documents

    :param file_csv: Путь к CSV файлу | Path to CSV file

    Returns:
        documents: Список документов | List documents
    """

    loader = CSVLoader(file_path=file_csv)
    documents = loader.load()
    return documents
