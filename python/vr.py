from os import *
from time import *
import playsound
from speech_recognition import *
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text,lang="en")
    fn  = "voice.mp3"
    tts.save(fn)
    playsound(fn)

speak("hey bro")