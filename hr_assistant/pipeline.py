
from hr_assistant import config
from hr_assistant.agent import create_hr_agent
from hr_assistant.loader import load_document
from hr_assistant.llm import get_llm
from hr_assistant.splitter import split_into_chunks
from hr_assistant.tool import create_tools
from hr_assistant.vector_store import (
    build_vector_store,
    get_retriever,
    load_vector_store,
    store_vector_store
)


def building_vector_store(file_path :str =config.DATA_FILE_PATH):
    """ craete vectors and store them"""
    document =load_document(file_path) 

    chunks = split_into_chunks(document)
    print(f"laoded the document{file_path} now splitted into {len(chunks)} chunks")
    vector_store =build_vector_store(chunks)
    store_vector_store(vector_store)
    

    print("vector store has been saved ")
    return vector_store

def building_hr_agent(file_path:str=config.DATA_FILE_PATH):
    config.check_api_keys()
    vector_store = building_vector_store(file_path)
    retriever=get_retriever(vector_store)
    search_tool = create_tools(retriever)

    llm = get_llm()
    agent = create_hr_agent(llm , search_tool)
    return agent

def ask(agent, question:str)->str:
    "ask question and get answer "
    response = agent.invoke( {
    "messages" :[{"role": "user" , 
                 "content":question}
                 ]})
    return response["messages"][-1].content