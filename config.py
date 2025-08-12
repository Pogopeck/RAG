import os
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
# Or use Hugging Face for open models
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
DATA_PATH = "data/sample_docs"
CHROMA_DB = "chroma_db"
