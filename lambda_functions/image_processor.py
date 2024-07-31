import json
import boto3
import os

s3_client = boto3.client('s3')
sns_client = boto3.client('sns')
sns_topic_arn = os.environ['SNS_TOPIC_ARN']


def lambda_handler(event, context):
    for record in event['Records']:
        s3_bucket = record['s3']['bucket']['name']
        s3_key = record['s3']['object']['key']

        # Process the image (e.g., generate a thumbnail)
        # This part is omitted for brevity

        # Send a notification
        message = {
            'bucket': s3_bucket,
            'key': s3_key,
            'status': 'Image processed'
        }
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=json.dumps(message)
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Image processed successfully')
    }
