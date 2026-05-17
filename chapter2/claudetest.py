import boto3
from dotenv import load_dotenv

load_dotenv()

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="ap-northeast-1",
)

response = client.invoke_model(
    modelId="anthropic.claude-3-haiku-20240307-v1:0",
    body='{"anthropic_version":"bedrock-2023-05-31","max_tokens":100,"messages":[{"role":"user","content":"こんにちは"}]}',
    contentType="application/json",
    accept="application/json",
)

print(response["body"].read())
