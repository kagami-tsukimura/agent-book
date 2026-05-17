from strands import Agent
from whatsnews import get_aws_updates


async def process_stream(service_name, container):
    text_holder = container.empty()
    response = ""
    prompt = f"AWSの{service_name.strip()}の最新アップデートを、日付付きで要約して。"

    agent = Agent(
        model="jp.anthropic.claude-haiku-4-5-20251001-v1:0", tools=[get_aws_updates]
    )

    async for chunk in agent.stream_async(prompt):
        if isinstance(chunk, dict):
            event = chunk.get("event", {})

            if "contentBlockStart" in event:
                tool_use = (
                    event["contentBlockStart"].get("start", {}).get("toolUse", {})
                )
                tool_name = tool_use.get("name")

                if response:
                    text_holder.markdown(response)
                    response = ""

                container.info(f"🔧 {tool_name} ツールを実行中…")
                text_holder = container.empty()

            if text := chunk.get("data"):
                response += text
                text_holder.markdown(response)
