import os
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

load_dotenv()
# GitHub API setup
endpoint = os.getenv("AZURE_AI_ENDPOINT")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
model = "openai/gpt-4.1"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(GITHUB_TOKEN)
)

response = client.complete(
    messages = [
        SystemMessage(content="You are an assistant, helping with day-to-day repetitive office jobs"),
        UserMessage("What is the capital of Canada?"),
    ],
    temperature=1,
    top_p = 1,
    model=model
)

print(response.choices[0].message.content)
