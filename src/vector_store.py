# vector_store.py
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_cohere import CohereEmbeddings
import config

def load_and_split_docs():
    loader = DirectoryLoader(config.DATA_PATH, glob="**/*.pdf")
    docs = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(docs)

# Use Cohere embeddings
embeddings = CohereEmbeddings(
    model="embed-english-v3.0",
    cohere_api_key=config.COHERE_API_KEY
)

# Load documents and split
documents = load_and_split_docs()

# Create vector store
db = Chroma.from_documents(
    documents,
    embeddings,
    persist_directory=config.CHROMA_DB
)
db.persist()
print("Vector store created and persisted!")
