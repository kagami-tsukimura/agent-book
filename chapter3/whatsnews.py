import feedparser
from dotenv import load_dotenv
from strands import Agent, tool

load_dotenv()


@tool
def get_aws_updates(service_name: str) -> list:
    feed = feedparser.parse("https://aws.amazon.com/about-aws/whats-new/recent/feed/")
    result = []

    for entry in feed.entries:
        if service_name.lower() in entry.title.lower():
            result.append(
                {
                    "published": entry.get("published", "N/A"),
                    "summary": entry.get("summary", ""),
                }
            )

            if len(result) >= 3:
                break

    return result


def main():
    agent = Agent(
        model="jp.anthropic.claude-haiku-4-5-20251001-v1:0", tools=[get_aws_updates]
    )

    service_name = input(
        "アップデートを知りたいAWSサービス名を入力してください："
    ).strip()

    prompt = f"AWSの{service_name}の最新アップデートを日付付きで要約して。"
    agent(prompt)


if __name__ == "__main__":
    main()
