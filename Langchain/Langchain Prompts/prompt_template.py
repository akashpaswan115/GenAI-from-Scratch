from langchain_core.prompts import PromptTemplate
from euriai.langchain_llm import EuriaiLangChainLLM
from dotenv import load_dotenv
import os

load_dotenv()

# ✅ Read API key securely
api_key = os.getenv("EURON_API_TOKEN")

# ✅ Use Euron-compatible LLM
model = EuriaiLangChainLLM(
    api_key=api_key,
    model="gpt-4.1-nano",
    temperature=1.5,
    max_tokens=500
)

# detailed way
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':'akash'})

result = model.invoke(prompt)

print(result)
