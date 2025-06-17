from euriai.langchain_llm import EuriaiLangChainLLM
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load .env file
load_dotenv()

# ✅ Read API key securely
api_key = os.getenv("EURON_API_TOKEN")

# ✅ Use Euron-compatible LLM
model = EuriaiLangChainLLM(
    api_key=api_key,
    model="gpt-4.1-nano",
)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)