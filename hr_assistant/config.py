"""All settings for the app live here, in one place."""


import os 
from dotenv import load_dotenv

load_dotenv()

## ENV VAR / SECRET - LLMS 

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
gemini_API_KEY= os.getenv("gemini_API_KEY")


GUARD_MODEL_NAME = "openai/gpt-oss-safeguard-20b"





## DEFINE PATH - DATA / VECTOR STORE 

DATA_FILE_PATH = os.path.join("data", "attendance_wfh_policy.txt")

## VECTORE STORES 


VECTOR_STORE_PATH =os.path.join("data" , "faiss_index")
# IN MEMORY 
# persistent memory - vectors # 100gb - ingestion 
# cloud memory
## MODELS 
# LLM and EMBEDING MODEL 

LLM_MODEL_NAME = "openai/gpt-oss-20b"
embedding_model_name="gemini-embedding-001"

## CHUNK / TEXT SPLITTING CONFIG 

CHUNK_SIZE = 400
CHUNK_OVERLAP = 40

# RETRIVAL RESULTS 
TOP_K_RESULTS = 3


## SYSTEM INSTRUCTIONS 

SYSTEM_PROMPT = (
    """You are a friendly HR assistant."
    " Always use the search_hr_policy tool to look up "
    "facts before answering. If the answer isn't in the search results, say you don't know "
    "instead of guessing."
    """
)


def check_api_keys() -> None:
    """Stop early with a clear message if a required API key is missing."""
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY. Please add it to your .env file.")
