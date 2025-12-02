from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=128,
    temperature=0.3,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke([
    {"role": "user", "content": "What is the capital of India?"}
])

print(result.content)
