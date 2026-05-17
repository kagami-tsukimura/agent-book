from dotenv import load_dotenv
from strands import Agent

load_dotenv()

agent = Agent("jp.anthropic.claude-haiku-4-5-20251001-v1:0")
agent("Strandsってどういう意味？")
