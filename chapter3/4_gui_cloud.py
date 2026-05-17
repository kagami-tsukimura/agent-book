import asyncio
import os

import streamlit as st
from gui import process_stream
from strands import Agent
from whatsnews import get_aws_updates

os.environ["AWS_ACCESS_KEY_ID"] = st.secrets["AWS_ACCESS_KEY_ID"]
os.environ["AWS_SECRET_ACCESS_KEY"] = st.secrets["AWS_SECRET_ACCESS_KEY"]
os.environ["AWS_DEFAULT_REGION"] = st.secrets["AWS_DEFAULT_REGION"]

agent = Agent(
    model="jp.anthropic.claude-haiku-4-5-20251001-v1:0", tools=[get_aws_updates]
)


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
