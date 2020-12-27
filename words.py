import pyttsx3 as p

engine = p.init()
meanings = {"certification": "the action or process of providing someone or something with an official document attesting to a status or level of achievement.",
            "Programming": "the process of writing computer programs.",
            "skill": "the ability to do something well; expertise",
            "automation": "the use or introduction of automatic equipment in a manufacturing or other process or facility,",
            "robot": "a machine resembling a human and able to replicate certain human movements and functions automatically"}

translations = {"certification": "Certificacion",
                "Programming": "programacion",
                "skill": "habilidad",
                "automation": "automatizacion",
                "robot": "robot"}

def mean(name):
    if name in meanings:
        res = meanings[name]
        engine.say("the meaning of " + name + " is" + res)
        engine.runAndWait()

def translate(name):
    if name in translations:
        res = translations[name]
        engine.say("The word translates to " + res + " in Spanish")
        engine.runAndWait()