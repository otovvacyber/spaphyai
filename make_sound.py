import os
import speech_recognition as sr
from gtts import gTTS

def process_assistant_speaks(audioStirngAssistant):
    print("AI:", audioStirngAssistant)
    togTTs = gTTS(text = audioStirngAssistant, lang = 'en-us', slow = False)
    togTTs.save("audioStirngAssistant.mp3")
    os.system("mpg321 audioStirngAssistant.mp3 -q")

#def process_assistant_speaks_exit(audioStirngAssistantExitRandom):
#    print("AI:", audioStirngAssistantExitRandom)
#    togTTs = gTTS(text = audioStirngAssistantExitRandom, lang = 'en-us', slow = False)
#    togTTs.save("audioStirngAssistantExitRandom.mp3")
#    os.system("mpg321 audioStirngAssistantExitRandom.mp3 -q")

voice = process_assistant_speaks("Okay bye see you later")



