import boto3

session = boto3.Session()

cred = session.get_credentials()

print("access key:", cred.access_key)
print("token exists:", cred.token is not None)
print("region:", session.region_name)
