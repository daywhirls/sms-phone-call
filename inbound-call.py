import os
from twilio.twiml.voice_response import Play, VoiceResponse
from flask import Flask

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])

def voice():
    response = VoiceResponse()
    response.say("Hello. You have reached David's secret phone line. Initiating phase two.")
    return str(response)

if __name__ == '__main__':
    app.run()
