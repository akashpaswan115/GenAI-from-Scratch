from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from euriai.langchain_embed import EuriaiEmbeddings
from langchain.vectorstores import FAISS
from euriai.langchain_llm import EuriaiLangChainLLM
import os
loader = TextLoader("doc.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs = text_splitter.split_documents(documents)

vectorstore = FAISS.from_documents(docs,EuriaiEmbeddings())

retriever = vectorstore.as_retriever()

query = "what are the key take aways from the document?"

retrieved_docs = retriever.get_relevant_documents(query)

retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])
api_key = os.getenv("EURON_API_TOKEN")

# ✅ Use Euron-compatible LLM
model = EuriaiLangChainLLM(
    api_key=api_key,
    model="gpt-4.1-nano",
)

prompt = f"based on following text ,answer the question"
answer = model.predict(prompt)

print("Answer:",answer)