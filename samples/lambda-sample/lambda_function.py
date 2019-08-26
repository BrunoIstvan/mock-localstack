# import boto3

# ENDPOINT_URL = 'http://localhost:4574'
# LAMBDA_FUNCTION
# REGION = 'us-west-1'
# ACCESS_KEY = 'AKIAIOSFODNN7EXAMPLE'
# SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'


# aws --endpoint-url=http://localhost:4574 lambda create-function --function-name lambda-demo --runtime python3.7
# --role whatever --handler lambda_function.lambda_handler --zip-file fileb://lambda.zip

def lambda_handler(event, context):

    return {'message': 'Lambda called'}
