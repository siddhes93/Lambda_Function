# Lambda_Function

you can use this Lambda function for any AWS resource for which notification should be publish in case of any event. In this Example i have used EC2 as example.  

Requirment: 

1. EC2 instance should be created
2. SNS Topic Define and add subscribers to it. 
3. Create an IAM Role and lambda should have access to SNS Topic to send alerts for any event. (create a custom policy Attach SNS , Cloudwatch services and add the custome Policy to the IAM Role) 
4. If Lamda create a log it should forward to Clouwatch Logs. 
5. Create a Lambda function , which has details of your ARN and message and import Boto3 which is sdk for python. Python version you can select any version you want. In my example I have used python 3.9

Lambda Function:

1. I have imported boto3 which is sdk for python
2. used client.publish methodology to publish the event to the subscriber.

SNS : Simple Notification service

  Step 1: Create a SNS Topic
  Step 2: Add subscriber to it. Subscribers means alert steps either it can be Email, SMS, HTTP . Select any option you wish.

Create Cloudwatch Event: 

1. Create a cloudwatch event for your lambda function and cloudwatch logs. To integreate both  of it. 
2. Add the trigger event details select EC2 instance , state on which event should trigger and select Instance ID. 





