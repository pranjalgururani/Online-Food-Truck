import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.

class dynam(object):

    def __init__(self):
        self = self


    def create(self):
        table = dynamodb.create_table(
            TableName='users',
            KeySchema=[
               {
                   'AttributeName': 'username',
                   'KeyType': 'HASH'
               },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
                }
            )
        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName='users')
        # Print out some data about the table.
        print(table.item_count)


    def putItems(self):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        table.put_item(
            Item={
                'username': 'janedoe',
                'first_name': 'Jane',
                'last_name': 'Doe',
                'age': 25,
                'account_type': 'standard_user',
    }
)