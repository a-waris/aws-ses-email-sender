import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name='AWS_REGION')

def send_email(source, to, subject, body):
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [to],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': 'CHARSET',
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': 'CHARSET',
                    'Data': subject,
                },
            },
            Source=source,
        )
    # Display an error if something goes wrong. 
    except BotoCoreError as e:
        print(e)
        return None
    except ClientError as e:
        print(e)
        return None

    print("Email sent! Message ID:"),
    print(response['MessageId'])

send_email('Your-Email', 'Recipient-Email', 'Subject', 'Body')
