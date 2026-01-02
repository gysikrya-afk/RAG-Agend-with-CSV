from langchain_text_splitters import RecursiveCharacterTextSplitter

def document_splitter(document):
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
