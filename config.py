from pathlib import Path

# ==========================================================
# PROJECT PATHS
# ==========================================================

# Project Root Folder
BASE_DIR = Path(__file__).resolve().parent

# Data Folder
DATA_DIR = BASE_DIR / "data"

# Upload Folder
UPLOAD_DIR = DATA_DIR / "uploads"

# FAISS Storage Folder
FAISS_DIR = DATA_DIR / "faiss_index"





# ==========================================================
# CREATE REQUIRED DIRECTORIES
# ==========================================================

# Automatically create folders if they don't exist
DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)

FAISS_DIR.mkdir(
    parents=True,
    exist_ok=True
)



# ==========================================================
# SUPPORTED FILE TYPES
# ==========================================================

SUPPORTED_FILE_TYPES = [
    ".pdf",
    ".txt",
    ".png",
    ".jpg",
    ".jpeg",
]

# ==========================================================
# TEXT CHUNKING
# ==========================================================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

# ==========================================================
# EMBEDDING MODEL
# ==========================================================

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# ==========================================================
# FAISS FILES
# ==========================================================

FAISS_INDEX_FILE = FAISS_DIR / "index.faiss"

FAISS_CHUNKS_FILE = FAISS_DIR / "chunks.pkl"

# ==========================================================
# OLLAMA SETTINGS
# ==========================================================

OLLAMA_BASE_URL = "http://localhost:11434"

OLLAMA_MODEL = "gemma3:1b"

# ==========================================================
# RETRIEVAL SETTINGS
# ==========================================================

TOP_K = 5

# ==========================================================
# OCR SETTINGS
# ==========================================================

TESSERACT_LANGUAGE = "eng"

# ==========================================================
# STREAMLIT SETTINGS
# ==========================================================

APP_TITLE = "Learning RAG with Ollama"

APP_ICON = "📚"