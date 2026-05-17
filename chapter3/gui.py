# 必要なライブラリをインポート
import asyncio  # 追加

import streamlit as st  # 追加
from strands import Agent
from whatsnews import get_aws_updates

agent = Agent(
    model="jp.anthropic.claude-haiku-4-5-20251001-v1:0", tools=[get_aws_updates]
)


async def process_stream(service_name, container):
    text_holder = container.empty()
    response = ""
    prompt = f"AWSの{service_name.strip()}の最新アップデートを、日付付きで要約して。"

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


st.title("AWSアップデート確認くん")
with st.form("aws_form"):
    service_name = st.text_input(
        "アップデートを知りたいAWSサービス名を入力してください："
    )

    submitted = st.form_submit_button("確認")
    if submitted and service_name:
        with st.spinner("アップデートを確認中..."):
            container = st.container()
            asyncio.run(process_stream(service_name, container))
