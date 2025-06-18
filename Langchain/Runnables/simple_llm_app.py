from euriai.langchain_llm import EuriaiLangChainLLM
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate,load_prompt

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
    input_variable=["topic"],
    template="Suggest a catchy blog title about {topic}."
)

topic = input('Enter a topic')

formatted_prompt = prompt.format(topic=topic)

blog_title = model.predict(formatted_prompt)

print("Generated Blog Title: ", blog_title)