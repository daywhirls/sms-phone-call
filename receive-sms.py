import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from outboundCall import makeCall

# init Flask app
app = Flask(__name__)

# create /sms route for TWIML to understand
@app.route("/sms", methods=['GET','POST'])

# msg: [numberToCall] [messageToSay]
def sms():
    msg = request.form['Body']
    input = msg.split()
    message = ' '.join(input[1:]) # everything after phone number is the message
    makeCall(str(input[0]), str(message)) # from outbound-call.py

if __name__ == "__main__":
    app.run(debug=True)
