import boto3
import json

ENDPOINT_URL = 'http://localhost:4576'
QUEUE_URL = f'{ENDPOINT_URL}/queue/teste'
REGION = 'us-west-1'
ACCESS_KEY = 'AKIAIOSFODNN7EXAMPLE'
SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'


def create_sqs_client():
    try:
        return boto3.client('sqs',
                              endpoint_url=ENDPOINT_URL,
                              region_name=REGION,
                              aws_access_key_id=ACCESS_KEY,
                              aws_secret_access_key=SECRET_KEY)
    except Exception as ex:
        print(ex)
        raise ex


def send_sqs_message(sqs_client, message):

    sqs_client.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=message
    )


def read_sqs(sqs_client):

    response = sqs_client.receive_message(
        QueueUrl=QUEUE_URL
    )

    print(response['Messages'][0]['Body'])


client = create_sqs_client()
send_sqs_message(client, 'Ohhhh vamos ganhar porcooooo !!!')
read_sqs(client)
