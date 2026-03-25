import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"]    = "Autonomous_Research_Agent"

# Model settings
LLM_MODEL        = "meta-llama/llama-4-scout-17b-16e-instruct"

# Retrieval settings
TOP_K            = 4
MAX_PUBMED_DOCS  = 5
MAX_RETRIES      = 2

# Chunking settings
CHUNK_SIZE       = 500
CHUNK_OVERLAP    = 50