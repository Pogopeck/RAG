# rag_app.py
from langchain_community.vectorstores import Chroma
from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
import config

# Initialize Cohere embedding and LLM
embeddings = CohereEmbeddings(
    model="embed-english-v3.0",
    cohere_api_key=config.COHERE_API_KEY
)

llm = ChatCohere(
    model="command-r",
    cohere_api_key=config.COHERE_API_KEY,
    temperature=0.3,
    max_tokens=500
)

# Load vector DB
db = Chroma(
    persist_directory=config.CHROMA_DB,
    embedding_function=embeddings
)

# Optional: Custom prompt with citations
prompt_template = """
You are an enterprise assistant. Answer the question based only on the context below. Include citations using [source:X] notation.

Context:
{context}

Question:
{question}

Answer:
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Build RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(k=3),
    chain_type_kwargs={"prompt": prompt},
    return_source_documents=True
)

def ask_question(query):
    result = qa_chain({"query": query})
    answer = result["result"]
    sources = result["source_documents"]
    return answer, sources
