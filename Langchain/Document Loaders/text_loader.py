from langchain_community.document_loaders import TextLoader
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

prompt = PromptTemplate(
    template = "Write a summary for the following poem \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt',encoding='utf-8')

docs = loader.load()

print(type(docs)) # list
print(len(docs))  # 1
print(docs[0].page_content)
print(docs[0].metadata)
chain = prompt | model | parser
print(chain.invoke({'poem':docs[0]}))