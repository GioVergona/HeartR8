import json
# import the AWS SDK (for Python the package name is boto3)
import boto3

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('user1_sesion1')


def lambda_handler(event, context):

    # write result and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'time': event['time'],
            'sensor': event['sensor']
        })

    return {
        'statusCode': 200,
        'body': json.dumps('Insert new item in DB ' + str(event['sensor']))
    }
