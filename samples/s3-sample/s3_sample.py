import boto3

ENDPOINT_URL = 'http://localhost:4572'
BUCKET_NAME = 'bucket-demo'
PAISES_FILE = 'Paises.txt'
REGION = 'us-west-1'
ACCESS_KEY = 'AKIAIOSFODNN7EXAMPLE'
SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'


def get_s3_client():

    return boto3.client('s3',
                        endpoint_url=ENDPOINT_URL)


def check_bucket(s3_client):

    try:
        s3_client.head_bucket(Bucket=BUCKET_NAME)
        return True
    except Exception as ex:
        print(ex)
        return False


def create_bucket(s3_client):

    try:
        s3_client.create_bucket(Bucket=BUCKET_NAME,
                                ACL='private',
                                )
    except Exception as ex:
        print('Erro ao criar Bucket: ', ex)
        raise ex


def upload_file(s3_client):

    s3_client.upload_file(Filename=PAISES_FILE, Bucket=BUCKET_NAME, Key=PAISES_FILE)


def read_file(s3_client):

    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=PAISES_FILE)
    if response is not None:
        if response['Body'] is not None:
            content = response['Body']
            data = content.read()
            print(data)


client = get_s3_client()
exists = check_bucket(client)
if not exists:
    create_bucket(client)
upload_file(client)
read_file(client)
