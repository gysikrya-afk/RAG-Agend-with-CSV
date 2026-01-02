from langchain_chroma import Chroma

def create_vectorstores(documnets,embedding,CHROMA_PATH):
    """
    Создание векторной базы на основе CHROMA_DB | Create vectorstores on ChromaDB
    
    :param documnets: Документы | Documents
    :param embedding: Математичекое представления текста | Mathemetical representation of text
    :param CHROMA_PATH: Путь к БД | Path to DB
    """

    chroma = Chroma.from_documents(
        documents=documnets,
        embedding=embedding,
        persist_directory=CHROMA_PATH
    )

    return chroma
