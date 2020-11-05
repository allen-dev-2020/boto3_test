#############################
#Sample for S3 bucket access#
#############################
mykey = "AKIAQH7JYYNITD5K2FFA"
mysecretkey = "+aFPzML3TXA7TF7tzpqQZ0wqPeRwv92vqk4JuQlm"

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='mykey',
    aws_secret_access_key='mysecretkey'
)
