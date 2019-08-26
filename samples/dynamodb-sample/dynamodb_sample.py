import boto3

TABLE_NAME = 'Paises'
ENDPOINT_URL = 'http://localhost:4569'
DYNAMODB = f'{ENDPOINT_URL}/queue/teste'
REGION = 'us-west-1'
ACCESS_KEY = 'AKIAIOSFODNN7EXAMPLE'
SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'


def create_dynamodb_client():

    try:
        return boto3.client('dynamodb',
                            endpoint_url=ENDPOINT_URL
                            # ,
                            # region_name=REGION,
                            # aws_access_key_id=ACCESS_KEY,
                            # aws_secret_access_key=SECRET_KEY
                            )
    except Exception as ex:
        print(ex)
        raise ex


def create_dynamodb_resource():

    try:
        return boto3.resource('dynamodb',
                              endpoint_url=ENDPOINT_URL,
                              region_name=REGION,
                              aws_access_key_id=ACCESS_KEY,
                              aws_secret_access_key=SECRET_KEY)

    except Exception as ex:
        print(ex)
        raise ex


def create_table(db_client):

    db_client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'sigla',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'nome',
                'AttributeType': 'S'
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'sigla',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'nome',
                'KeyType': 'RANGE'  # Partition key
            }
        ],
        ProvisionedThroughput={ # // required provisioned throughput for the table
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        },
        TableName=TABLE_NAME
    )


def save_data(db_client, pais):

    table = db_client.Table(TABLE_NAME)
    table.put_item(Item=pais)


def read_data(db_client, key):

    try:
        table = db_client.Table(TABLE_NAME)
        response = table.get_item(Key=key)
        pais = response['Item']
        print(pais)
    except KeyError as ex:
        print('Registro não encontrado: ', key)


def update_data(db_client, key, continente):

    table = db_client.Table(TABLE_NAME)
    table.update_item(Key=key,
        UpdateExpression='SET continente=:value1',
        ExpressionAttributeValues={
            ':value1': continente
        }
    )


def delete_data(db_client, key):

    table = db_client.Table(TABLE_NAME)
    table.delete_item(Key=key)


brasil = {'sigla': 'BR', 'nome': 'Brasil', 'continente': 'América do Norte'}
brasil_key = {'sigla': 'BR', 'nome': 'Brasil'}

uruguai = {'sigla': 'UY', 'nome': 'Uruguai', 'continente': 'América do Sul'}
uruguai_key = {'sigla': 'UY', 'nome': 'Uruguai'}

argentina = {'sigla': 'AR', 'nome': 'Argentina', 'continente': 'América do Sul'}
argentina_key = {'sigla': 'AR', 'nome': 'Argentina'}


client = create_dynamodb_client()
resource = create_dynamodb_resource()
create_table(db_client=resource)
save_data(db_client=resource, pais=brasil)
read_data(db_client=resource, key=brasil_key)
update_data(db_client=resource, key=brasil_key, continente='América do Sul')
print('After update')
read_data(db_client=resource, key=brasil_key)

save_data(db_client=resource, pais=uruguai)
read_data(db_client=resource, key=uruguai_key)

save_data(db_client=resource, pais=argentina)
read_data(db_client=resource, key=argentina_key)
delete_data(db_client=resource, key=argentina_key)
print('After delete')
read_data(db_client=resource, key=argentina_key)
