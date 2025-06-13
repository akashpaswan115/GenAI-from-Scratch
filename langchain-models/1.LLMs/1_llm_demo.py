from euriai import EuriaiLangChainLLM
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the Euron API key from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the Euriai LLM with the key from .env
llm = EuriaiLangChainLLM(
    api_key=OPENAI_API_KEY,
    model="gpt-4.1-nano",
    temperature=0.7,
    max_tokens=300
)

# Invoke the model
print(llm.invoke("What is the capital of India?"))


# from langchain_openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = OpenAI(model='gpt-3.5-turbo-instruct')

# result = llm.invoke("What is the capital of India")

# print(result)