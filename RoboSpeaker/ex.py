# Import the required module for text
# to speech conversion
import pyttsx3
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
while True:
    print("Welcome to RoboSpeaker 1.1. Created by Sachin")
    x = input("Enter What you want me to speak: ")
    if x == "Quit":
        s = engine.getProperty("voices")
        engine.setProperty("voice", s[0].id)
        engine.setProperty("rate", 100)
        engine.say("Quit")
        engine.say("Bye Bye Friends.")
        engine.runAndWait()
        break
    s = engine.getProperty("voices")
    engine.setProperty("voice", s[0].id)
    engine.setProperty("rate", 100)
    # say method on the engine that passing input text to be spoken
    engine.say(x)
    # run and wait method, it processes the voice commands.
    engine.runAndWait()


