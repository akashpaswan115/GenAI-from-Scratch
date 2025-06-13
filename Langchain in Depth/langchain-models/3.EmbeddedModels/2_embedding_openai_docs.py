from euriai.langchain_embed import EuriaiEmbeddings
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Fetch API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize embedding model
embedding_model = EuriaiEmbeddings(api_key=OPENAI_API_KEY)
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
# Call embed_query
print(embedding_model.embed_documents(documents))  


# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# documents = [
#     "Delhi is the capital of India",
#     "Kolkata is the capital of West Bengal",
#     "Paris is the capital of France"
# ]

# result = embedding.embed_documents(documents)

# print(str(result))