import boto3

client = boto3.client('sns')

def lambda_handler(event, context):
    topic_arn='arn:aws:sns:us-east-1:*******:Prodalert'
    message='prod server stopped alerts please look into it'
    client.publish(TopicArn=topic_arn,Message=message)
