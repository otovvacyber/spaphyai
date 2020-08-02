import speech_recognition as sr
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import random
import sys
#import urllib
#import json
#import calendar
import warnings
#import wikipedia
#import re
import time
#import webbrowser
import random
#import smtplib
#import requests
#import bs4
#import tkinter
from gtts import gTTS
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys#
#from pygame import mixer
#from pyowm import OWM

#Ignore any warning messages
warnings.filterwarnings('ignore')

class Spaphy_ai():
	def __init__(self):
		pass
		
	def process_assistant_speaks(self, audioStirngAssistant):
		print("AI:", audioStirngAssistant)
		togTTs = gTTS(text = audioStirngAssistant, lang = 'en-us', slow = False)
		togTTs.save("audioStirngAssistant.mp3")
		os.system("mpg321 audioStirngAssistant.mp3 -q")
		os.remove("audioStirngAssistant.mp3")

	def process_assistant_speaks_exit(self, audioStirngAssistantExitRandom):
		print("AI:", audioStirngAssistantExitRandom)
		togTTs = gTTS(text = audioStirngAssistantExitRandom, lang = 'en-us', slow = False)
		togTTs.save("audioStirngAssistantExitRandom.mp3")
		os.system("mpg321 audioStirngAssistantExitRandom.mp3 -q")
		os.remove("audioStirngAssistantExitRandom.mp3")

	def process_get_audio_in(self):
		speechRecognitionMic = sr.Recognizer()
		with sr.Microphone() as source:
			print ("Listening...")
			audioStirngPerson = speechRecognitionMic.listen(source, phrase_time_limit = 5)
			audioStirngPersonToText = ""
		try:
			audioStirngPersonToText = speechRecognitionMic.recognize_google(audioStirngPerson)
			print("Me:", audioStirngPersonToText)
			return audioStirngPersonToText
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
			return 0
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
			return 0
		finally:
			pass

	def process_system_application_digital_assistant(self, speechRecognitionMic):
		pass

	def process_greeting_words(self):
		audioStirngAssistant = ["Spaphy is here to help you how can i help you sir","Hello sir Spaphy here what can i do for you","Hi sir Spaphy here what can i do for you","What can do for you sir Spaphy would like to help you", "Hello there what can i do for you i am here to help you", "Hey there i am here to help you What can do for you"]
		return random.choice(audioStirngAssistant)
	def process_exit_greeting_words(self):
		audioStirngAssistantExitRandom = ["Okey fine nice to talk to you","Okay bye see you later", "See you next time bye"]
		return random.choice(audioStirngAssistantExitRandom)


audioStirngAssistant = ""
audioStirngAssistantExitRandom = ""

run_spaphy_ai = Spaphy_ai()

audioStirngAssistantExitRandom = run_spaphy_ai.process_exit_greeting_words()

def main():
	while True:
		audioStirngAssistant = run_spaphy_ai.process_greeting_words()
		run_spaphy_ai.process_assistant_speaks(audioStirngAssistant)
		speechRecognitionMic = run_spaphy_ai.process_get_audio_in()
		if "exit" in str(speechRecognitionMic) or "ok bye bye" in str(speechRecognitionMic) or "sleep" in str(speechRecognitionMic) or "go away" in str(speechRecognitionMic) or "shutdown" in str(speechRecognitionMic) or "get out" in str(speechRecognitionMic) or "see you bye" in str(speechRecognitionMic) or "good bye" in str(speechRecognitionMic) or "we can see later" in str(speechRecognitionMic) or "bye bye" in str(speechRecognitionMic) or "bye" in str(speechRecognitionMic) or "close" in str(speechRecognitionMic) or "see you later" in str(speechRecognitionMic): 
			audioStirngAssistantExitRandom = run_spaphy_ai.process_exit_greeting_words()
			run_spaphy_ai.process_assistant_speaks_exit(audioStirngAssistantExitRandom)
			break 
		else:
			run_spaphy_ai.process_system_application_digital_assistant(speechRecognitionMic)
if __name__ == "__main__":
	main()
