from langchain_community.vectorstores import FAISS
import os 

from hr_assistant import config
from hr_assistant.embedding import get_embeddings_model
def build_vector_store(chunks):
    """
    convert into number """
    embeddings_model = get_embeddings_model()
    return FAISS.from_documents(chunks , embeddings_model)



#  storing our vector index 

def store_vector_store(vector_store , path :str= config.VECTOR_STORE_PATH):
    """
    save the faiss index to disk so we don't have to re uild everytime  """
    vector_store.save_local(path)

def load_vector_store(path :str= config.VECTOR_STORE_PATH):
    embeddings_model=get_embeddings_model()
    return FAISS.load_local(path, embeddings_model,allow_dangerous_deserialization=True)


def get_retriever(vector_store , k=config.TOP_K_RESULTS):
    """ return top matching vector store , something in which our agenct can interectwith """
    return vector_store.as_retriever(search_kwargs= {"k": k})
