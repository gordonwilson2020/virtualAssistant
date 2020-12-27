import speech_recognition as sr
import pyttsx3 as p
from web_automation import *

r = sr.Recognizer()
engine = p.init()
engine.say("Hello, how are you doing?")
engine.runAndWait()

with sr.Microphone() as source:
    text = r.listen(source)
    try:
        recognised_text = r.recognize_google(text)
        print(recognised_text)
        if recognised_text == "play music":
            music()
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")
    engine.say("What do you want me to do?")
    engine.runAndWait()
    text1 = r.listen(source)
    try:
        recognised_text = r.recognize_google(text1)
        print(recognised_text)
        if recognised_text == "play music":
            music()
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")