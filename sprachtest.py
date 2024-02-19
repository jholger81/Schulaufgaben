import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from gtts import gTTS
from pygame import mixer
import time

def text_to_speech(text):
    speech = gTTS(text, lang = "de")
    speech_file = 'speech.mp3'
    speech.save(speech_file)
    mixer.init()
    mixer.music.load(speech_file)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.music.stop()
    mixer.quit()
    
