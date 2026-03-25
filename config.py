import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"]    = "Autonomous_Research_Agent"

# Model settings
LLM_MODEL        = "meta-llama/llama-4-scout-17b-16e-instruct"

# Chunking settings
CHUNK_SIZE       = 500
CHUNK_OVERLAP    = 50
