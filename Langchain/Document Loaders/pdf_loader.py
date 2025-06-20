from langchain_community.document_loaders import TextLoader,PyPDFLoader
from euriai.langchain_llm import EuriaiLangChainLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
# Load .env file
load_dotenv()

# ✅ Read API key securely
api_key = os.getenv("EURON_API_TOKEN")

# ✅ Use Euron-compatible LLM
model = EuriaiLangChainLLM(
    api_key=api_key,
    model="gpt-4.1-nano",
)

loader = PyPDFLoader('sql_notes.pdf')
docs = loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[1].metadata)