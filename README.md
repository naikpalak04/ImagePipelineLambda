# ImagePipelineLambda
ImagePipelineLambda is a serverless application that demonstrates the use of AWS Lambda, SNS, SQS, and S3 to create an efficient, scalable image processing pipeline. This project showcases how to seamlessly integrate various AWS services to handle image uploads, send notifications, and manage processing tasks.


# Serverless Image Processing with AWS Lambda, SNS, SQS, and S3

This project demonstrates a serverless application using AWS Lambda, SNS, SQS, and S3. It processes image uploads, sends notifications, and manages tasks using AWS services.

## Architecture

1. **Image Upload to S3**: Users upload images to an S3 bucket.
2. **Lambda Trigger**: An S3 event triggers a Lambda function to process the image.
3. **SNS Notification**: The Lambda function sends a notification to an SNS topic.
4. **SQS Queue**: The SNS notification triggers another Lambda function, which sends the message to an SQS queue.
5. **Task Management**: A final Lambda function processes the messages from the SQS queue.

## Prerequisites

- AWS CLI configured
- Python 3.8
- AWS account with necessary IAM roles

## Deployment

1. Clone the repository.
2. Deploy the CloudFormation stack:

   ```bash
   aws cloudformation deploy --template-file template.yaml --stack-name serverless-image-processing

## Upload images to the S3 bucket:
   aws s3 cp path/to/your/image.jpg s3://my-image-upload-bucket/

