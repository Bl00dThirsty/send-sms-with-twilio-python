from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Test',
         from_ =  +19013502979, #Your Twilio phone number
         to = +*123456789
     )
print(message.sid)