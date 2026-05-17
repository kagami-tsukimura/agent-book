import os
import boto3
from dotenv import load_dotenv

load_dotenv()

print("Using Access Key:", os.getenv("AWS_ACCESS_KEY_ID"))
sts = boto3.client("sts")
print(sts.get_caller_identity())
