from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network.csv')

docs = loader.load()

print(len(docs))
print(docs[1])