import speech_recognition as sr
import pyttsx3 as p
from web_auto import *
from web_auto1 import *
from web_automation import *
from recommendations import *
from words import *

r1 = sr.Recognizer()
engine = p.init()
engine.say("Hello sir, how are you today?")
engine.runAndWait()
with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    print("how are you today?")
    audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")

engine.say("What would you like me to do?")
engine.runAndWait()
print("What do you want?")

r2 = sr.Recognizer()
with sr.Microphone() as source:
    r2.adjust_for_ambient_noise(source)
    audio = r2.listen(source)
    try:
        instruction = r2.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")

r3 = sr.Recognizer()
if "information" in instruction:
    engine.say("information about what?")
    engine.runAndWait()
    with sr.Microphone() as source1:
        audio2 = r3.listen(source1)
        try:
            information = r3.recognize_google(audio2)
            bot = info()
            bot.get_info(information)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

r4 = sr.Recognizer()
if "review" in instruction:
    engine.say("What is the name of the movie?")
    engine.runAndWait()
    with sr.Microphone() as source2:
        audio3 = r4.listen(source2)
        try:
            rating = r4.recognize_google(audio3)
            bot = Movie()
            bot.get_movie(rating)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

r5 = sr.Recognizer()
if "music" in instruction:
    engine.say("Which artist should I play?")
    engine.runAndWait()
    with sr.Microphone() as source3:
        audio4 = r5.listen(source3)
        try:
            video = r5.recognize_google(audio4)
            bot = music()
            bot.play(video)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

if "recommendation" in instruction:
    engine.say("Here is a list of movies you can choose to watch from")
    engine.runAndWait()
    bot = recom()
    bot.recom_info()

r6 = sr.Recognizer()
if "meaning" in instruction:
    engine.say("Which word sir?")
    engine.runAndWait()
    with sr.Microphone() as source4:
        audio5 = r6.listen(source4)
        try:
            word = r6.recognize_google(audio5)
            mean(word)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

r7 = sr.Recognizer()
if "translate" in instruction:
    engine.say("Which word sir?")
    engine.runAndWait()
    with sr.Microphone() as source5:
        audio6 = r7.listen(source5)
        try:
            word1 = r7.recognize_google(audio6)
            translate(word1)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")