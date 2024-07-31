import json


def lambda_handler(event, context):
    for record in event['Records']:
        message = json.loads(record['body'])

        # Process the task
        # This part is omitted for brevity

    return {
        'statusCode': 200,
        'body': json.dumps('Task processed successfully')
    }
