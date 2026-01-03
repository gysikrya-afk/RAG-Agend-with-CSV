from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.schema import Document as LangchainDocument

from typing import Iterable

def document_splitter(document:Iterable[LangchainDocument]):
    """
    Разбитие документа на чанки | Splitting a document into chunks
    
    :param document: Документ | Document

    Returns:
        splitted_document:Документ разбитый на чанки | Splitting a document
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    splitted_document = text_splitter.split_documents(document)

    return splitted_document
