from langchain_community.document_loaders import CSVLoader

def csv_loader(file_csv):
    """
    Загрузка csv файла | Download CSV file
    
    :param file_csv: CSV файл | CSV file

    Returns:
        document:Загруженный документ | Download file
    """

    loader = CSVLoader(file_path=file_csv)

    document = loader.load()

    return document
