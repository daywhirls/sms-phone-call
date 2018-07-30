import os
from twilio.rest import Client

# takes number and msg from received SMS and converts it to text-to-speech and makes the phone call.
def makeCall(number, msg):

    # Twilio credentials
    TWILIO_SID = os.environ["TWILIO_SID"]
    TWILIO_AUTH = os.environ["TWILIO_AUTH"]

    # My personal phone number & twilio number
    my_number = os.environ["MY_NUMBER"]
    twilio_number = os.environ["TWILIO_NUMBER"]

    client = Client(TWILIO_SID, TWILIO_AUTH)
    twimlTemplate = 'https://handler.twilio.com/twiml/EH5b088cce6596c4685d86e231ea7b46ba'

    url = twimlTemplate + '?Msg=' + msg

    call = client.calls.create(
        url=url,
        to=number,
        from_=twilio_number
        )

    print(call.sid)
