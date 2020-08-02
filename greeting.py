def process_greeting_words(self):
	audioStirngAssistant = ["Spaphy is here to help you how can i help you sir","Hello sir Spaphy here what can i do for you","Hi sir     Spaphy here what can i do for you","What can do for you sir Spaphy would like to help you", "Hello there what can i do for you i am here to help y    ou", "Hey there i am here to help you What can do for you"]
	return random.choice(audioStirngAssistant)

def process_exit_greeting_words(self):
	audioStirngAssistantExitRandom = ["Okey fine nice to talk to you","Okay bye see you later", "See you next time bye"]
	return random.choice(audioStirngAssistantExitRandom)
