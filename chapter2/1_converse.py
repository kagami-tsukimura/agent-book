import boto3
from dotenv import load_dotenv

load_dotenv()

client = boto3.client("bedrock-runtime")

response = client.converse(
    modelId="jp.anthropic.claude-haiku-4-5-20251001-v1:0",
    messages=[{"role": "user", "content": [{"text": "こんにちは"}]}],
)

print(response["output"]["message"]["content"][0]["text"])
