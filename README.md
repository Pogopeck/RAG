enterprise-knowledge-rag/
│
├── .devcontainer/                     # Codespaces configuration
│   └── devcontainer.json
│
├── src/                               # Core application code
│   ├── rag_app.py                     # Main RAG logic & QA chain
│   ├── vector_store.py                # Load, chunk, and store docs
│   ├── retriever.py                   # Custom retriever with reranking
│   ├── utils/                         # Helper modules
│   │   ├── pii_redactor.py
│   │   ├── audit_logger.py
│   │   └── file_loader.py
│   └── api/                           # Optional: FastAPI/Flask endpoints
│       └── main.py
│
├── data/                              # Sample internal documents (for dev)
│   └── sample_docs/
│       ├── policy.pdf
│       ├── employee_handbook.pdf
│       └── it_guidelines.pdf
│
├── config/                            # Configuration files
│   ├── __init__.py
│   ├── settings.py                    # App settings
│   └── logging_config.py
│
├── tests/                             # Unit & integration tests
│   ├── test_rag.py
│   ├── test_utils.py
│   └── conftest.py
│
├── notebooks/                         # Jupyter notebooks for exploration
│   └── rag_experiments.ipynb
│
├── scripts/                           # CLI tools & automation
│   └── ingest_data.py                 # Script to add new documents
│
├── .env                               # Environment variables (git-ignored)
├── .gitignore
├── requirements.txt                   # Python dependencies
├── pyproject.toml                     # Optional: modern Python packaging
├── README.md                          # Project overview & setup guide
└── LICENSE
