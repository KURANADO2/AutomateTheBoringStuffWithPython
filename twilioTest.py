import os
from twilio.rest import Client


TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TO_NUMBER = os.getenv('TO_NUMBER')
FROM_NUMBER = os.getenv('FROM_NUMBER')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
client.api.account.messages.create(to=TO_NUMBER, from_=FROM_NUMBER, body='你好!')