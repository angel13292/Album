import boto3

bucket_name ='166665-angel'
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
bucket.put_object(Key='another.txt', Body=open('test.txt', 'rb'))
