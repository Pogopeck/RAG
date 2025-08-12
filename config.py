import os
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
DATA_PATH = os.getenv("DATA_PATH", "data/sample_docs")
CHROMA_DB = os.getenv("CHROMA_DB", "chroma_db")
