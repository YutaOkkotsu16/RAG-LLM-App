# Retrieval Augmented Generation (RAG)

import os
from dotenv import load_dotenv

# Calling the API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")
os.environ['OPENAI_API_KEY'] = api_key

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Loading the data
try:
    documents = SimpleDirectoryReader(os.path.join(os.path.dirname(__file__), "data")).load_data()
except Exception as e:
    raise RuntimeError(f"Failed to load data: {e}")

# Creating the index to the vectors
index = VectorStoreIndex.from_documents(documents, show_progress=True)

# Create a query engine for retrieving the data
query_engine = index.as_query_engine()

# Get response
response = query_engine.query("How to choose a search space representation?")

print(response)