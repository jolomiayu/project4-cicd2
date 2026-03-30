import boto3, os

def handler(event, context):
    return {"statusCode": 200, "body": "Hello from Lambda"}
