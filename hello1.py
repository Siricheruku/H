import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]

with open('bucket_names.txt', 'w') as f:
    for bucket in buckets:
        f.write(bucket + '\n')



