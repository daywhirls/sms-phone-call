import os
from twilio.twiml.voice_response import Play, VoiceResponse
from flask import Flask

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])

def voice():
    response = VoiceResponse()
    response.say("Hello. You have reached David's secret phone line. Please hang up and await further instructions.")
    return str(response)

if __name__ == '__main__':
    app.run()
