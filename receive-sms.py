import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from outboundCall import makeCall

# init Flask app
app = Flask(__name__)

# create /sms route for TWIML to understand
@app.route("/sms", methods=['GET','POST'])

# msg: [numberToCall] [messageToSay...]
# example: "+1xxxxxxxxxx what is up my dude."
# Rip off number, make a new string for message,
# and replace spaces with %20 so TwiML URL can understand it.
def sms():
    msg = request.form['Body']
    input = msg.split()
    message = '%20'.join(input[1:]) # everything after msg[0] is the message
    makeCall(str(input[0]), str(message)) # pass phoneNumber, msg to outboundCall

if __name__ == "__main__":
    app.run()
