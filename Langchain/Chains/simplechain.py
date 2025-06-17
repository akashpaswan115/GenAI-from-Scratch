from euriai.langchain_llm import EuriaiLangChainLLM
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import StrOutputParser
# Load .env file
load_dotenv()

# ✅ Read API key securely
api_key = os.getenv("EURON_API_TOKEN")

prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

# ✅ Use Euron-compatible LLM
model = EuriaiLangChainLLM(
    api_key=api_key,
    model="gpt-4.1-nano",
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'life'})

print(result)

chain.get_graph().print_ascii()