import os
from openai import OpenAI

# Create a client using your KodeKey credentials
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

# Send a message to the LLM
response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {"role": "user", "content": "What is an LLM?"}
    ]
)

# Print the response
print(response.choices[0].message.content)