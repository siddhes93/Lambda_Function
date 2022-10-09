import boto3 ##Boto 3 is SDK for python

client = boto3.client('sns')

def lambda_handler(event, context):
    topic_arn='arn:aws:sns:us-east-1:*******:Prodalert'  ## in Place of *** use your ARN accoutn ID##
    message='prod server stopped alerts please look into it' ## you can add your own custom message. these are varables which is used down.
    client.publish(TopicArn=topic_arn,Message=message) 
