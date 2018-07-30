import os
from gtts import gTTS

text = "Dave was here"
lang = 'en'

ttsObj = gTTS(text=text, lang=lang, slow=False)

# ttsObj.save("welcome.mp3")
