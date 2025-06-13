from euriai import EuriaiLangChainLLM
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the Euron API key from the environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize the Euriai LLM with the key from .env
llm = EuriaiLangChainLLM(
    api_key=GOOGLE_API_KEY,
    model="gemini-2.5-flash-preview-05-20",
    #temperature=0.7,
    #max_tokens=300
)

# Invoke the model
print(llm.invoke("What is the capital of India?"))




# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# result = model.invoke('What is the capital of India')

# print(result.content)