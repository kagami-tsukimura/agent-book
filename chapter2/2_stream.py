import boto3

client = boto3.client("bedrock-runtime")

response = client.converse_stream(
    modelId="jp.anthropic.claude-haiku-4-5-20251001-v1:0",
    messages=[{"role": "user", "content": [{"text": "いろは歌を詠んで"}]}],
)


for event in response.get("stream", []):
    if "contentBlockDelta" in event:
        chunk = event["contentBlockDelta"]["delta"]["text"]
        print(chunk, end="")
