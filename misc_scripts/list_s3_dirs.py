import boto3
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

def list_directories(bucket_name):
    # Create an S3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    # Initialize a paginator to handle large lists of objects
    '''
    Paginator: In AWS, a paginator is a feature that abstracts the process of iterating over the results of an API operation that is truncated. Paginators are used when some AWS operations return incomplete results and require additional requests to get the entire result set. This process of sending subsequent requests is called pagination.
    
    list_objects_v2: Creates an iterator that will paginate through responses from S3.Client.list_objects_v2().
    '''
    paginator = s3_client.get_paginator('list_objects_v2')
    result = paginator.paginate(Bucket=bucket_name, Delimiter='/')
    directories = []
    for page in result:
        if 'CommonPrefixes' in page:
            for prefix in page['CommonPrefixes']:
                directories.append(prefix['Prefix'])
    return directories

if __name__ == "__main__":
    bucket_name = 'sanjay-app-s3-bucket'  # Replace with your S3 bucket name
    directories = list_directories(bucket_name)
    if directories:
        print("Directories found in the S3 bucket:")
        for directory in directories:
            print(directory)
    else:
        print("No directories found in the S3 bucket.")