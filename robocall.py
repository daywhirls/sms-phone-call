import os
from twilio.rest import Client
from gtts import gTTS

# Twilio credentials
TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH = os.environ["TWILIO_AUTH"]

# My personal phone number & twilio number
my_number = os.environ["MY_NUMBER"]
twilio_number = os.environ["TWILIO_NUMBER"]

client = Client(TWILIO_SID, TWILIO_AUTH)
