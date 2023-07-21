# aws-ses-email-sender

This is a Python script that uses Amazon Simple Email Service (SES) via Boto3, the Amazon Web Services (AWS) SDK for Python. Note that this script assumes you've set up Amazon SES correctly, you've verified your email addresses, and you've stored your AWS credentials in the appropriate location.

Auto rotating sending IP is not typically managed at the application level, but rather it's a feature that must be set at the SES service level or using a proxy solution.

Please remember to replace 'Your-Email', 'Recipient-Email', 'Subject', and 'Body' with actual values. Also, be sure to replace 'AWS_REGION' with your SES region and 'CHARSET' with your desired email charset, like 'UTF-8'.

In order to track email events like the 'email opened' event, you have to use Amazon SES configuration sets. These allow you to publish email sending events to Amazon CloudWatch or Amazon Kinesis. You can track deliveries, bounces, complaints, sends, rejects, opens, clicks, rendering failures, and delivery delays.

Regarding scheduling emails, you could use cron jobs if you're on a Unix-like operating system, or Task Scheduler on Windows. However, scheduling and rotating IPs is beyond Python's scope. You might consider services like AWS Lambda for scheduling or using AWS SES dedicated IP pools for IP rotation.
