from euriai.langchain_embed import EuriaiEmbeddings
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Fetch API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize embedding model
embedding_model = EuriaiEmbeddings(api_key=OPENAI_API_KEY)

# Call embed_query
print(embedding_model.embed_query("What's AI?")[:5])  # Print first 5 dimensions





# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# result = embedding.embed_query("Delhi is the capital of India")

# print(str(result))