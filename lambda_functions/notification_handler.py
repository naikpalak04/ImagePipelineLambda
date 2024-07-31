import json
import boto3
import os

sqs_client = boto3.client('sqs')
sqs_queue_url = os.environ['SQS_QUEUE_URL']


def lambda_handler(event, context):
    for record in event['Records']:
        message = json.loads(record['Sns']['Message'])

        # Send message to SQS queue
        sqs_client.send_message(
            QueueUrl=sqs_queue_url,
            MessageBody=json.dumps(message)
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent to SQS')
    }
