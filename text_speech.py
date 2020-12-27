import pyttsx3 as p

"""VOICE"""
engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

engine.say("Hello, how are you doing?")
engine.say("What would you like me to do?")
engine.runAndWait()