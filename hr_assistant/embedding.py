from langchain_google_genai import GoogleGenerativeAIEmbeddings
from hr_assistant import config

def get_embeddings_model():
    """
    read model 
    """
    return GoogleGenerativeAIEmbeddings(model =config.embedding_model_name , google_api=config.gemini_API_KEY)
