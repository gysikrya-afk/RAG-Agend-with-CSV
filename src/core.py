from langchain_openai import ChatOpenAI
from langchain_classic.prompts import PromptTemplate
from langchain_classic.chains.llm import LLMChain

def create_llm(model,api_key,temperature):
    """
    Создание LLM для RAG | Create LLM for RAG
    
    :param model: Модель OpenAI | Model OpenAI
    :param api_key: API-ключ от OpenAI | API-Key OpenAI
    :param temperature: Точность ИИ | AI Accuracy

    Returns:
        chain:Готовая модель для роботы | Ready model for work
    """

    llm = ChatOpenAI(
        model=model,
        temperature=temperature,
        openai_api_key=api_key
    )

    prompt = PromptTemplate(
        input_variables=['documents'],
        template="""
        Ты RAG-Ассистент.Твоя задача отвечать на вопросы по загруженим докуметам.
        Если не найдёшь ответа в документах смело и понятно говопи про это.Ничего не выдумывай!

        Документы:{documents}


        """
    )

    chain = LLMChain(llm=llm,prompt=prompt)

    return chain
