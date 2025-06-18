from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from euriai.langchain_embed import EuriaiEmbeddings
from langchain.vectorstores import FAISS
from euriai.langchain_llm import EuriaiLangChainLLM
import os
from langchain.chains import retrieval_qa
loader = TextLoader("doc.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs = text_splitter.split_documents(documents)

vectorstore = FAISS.from_documents(docs,EuriaiEmbeddings())

retriever = vectorstore.as_retriever()

api_key = os.getenv("EURON_API_TOKEN")

# ✅ Use Euron-compatible LLM
llm = EuriaiLangChainLLM(
    api_key=api_key,
    model="gpt-4.1-nano",
)

qa_chain = retrieval_qa.from_chain_type(llm=llm,retriever=retriever)
query="what are the key takeaways from the document?"
answer = qa_chain.run(query)

print("Answer:",answer)  