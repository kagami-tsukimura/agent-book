import os

from dotenv import load_dotenv

load_dotenv()

print("ENV ACCESS:", repr(os.getenv("AWS_ACCESS_KEY_ID")))
print("ENV SECRET:", repr(os.getenv("AWS_SECRET_ACCESS_KEY")))
