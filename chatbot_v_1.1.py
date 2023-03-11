import random                          # Importing all the required libraries
import json
import pickle

import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

import numpy as np
import speech_recognition as sr
import pyttsx3
import time

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())     # loading the required dataset

words = pickle.load(open('words.pkl', 'rb'))          # This is the vocab for the model
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')                # loading the pre-trained model


def clean_up_sentence(sentence):
	sentence_words = nltk.word_tokenize(sentence)
	sentence_words = [lemmatizer.lemmatize(word)
					for word in sentence_words]

	return sentence_words


def bag_of_words(sentence):
	sentence_words = clean_up_sentence(sentence)
	bag = [0] * len(words)

	for w in sentence_words:
		for i, word in enumerate(words):
			if word == w:
				bag[i] = 1
	return np.array(bag)


def predict_class(sentence):
	bow = bag_of_words(sentence)
	res = model.predict(np.array([bow]))[0]

	ERROR_THRESHOLD = 0.25

	results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

	results.sort(key=lambda x: x[1], reverse=True)

	return_list = []

	for r in results:
		return_list.append({'intent': classes[r[0]],
							'probability': str(r[1])})
	return return_list


def get_response(intents_list, intents_json):            # This function gives a random response from the available responses.
	tag = intents_list[0]['intent']
	list_of_intents = intents_json['intents']

	result = ''

	for i in list_of_intents:
		if i['tag'] == tag:
			result = random.choice(i['responses'])
			break
	return result


def calling_the_bot(txt,press):                           # This function finds the Disease accoring to the symptoms given.
	
	global res
	predict = predict_class(txt)
	res = get_response(predict, intents)

	if(press==1):
		engine.say(" Found it. From our Database we found that" + res)
		print("\nFound it. From our Database we found that" + res)
	else:
		print("\nFound it. From our Database we found that" + res)
	
	# engine.say(res)
	
	engine.runAndWait()
	print("\nYour Symptom was : ", txt)
	print("\nResult found in our Database : ", res)


if __name__ == '__main__':
	
	print("\nBot is Running ...")
	name=input("\nPlease Enter you First Name and Last Name : ") 	#name stored in buffer for now
	

	engine = pyttsx3.init()
	rate = engine.getProperty('rate')

	# Increase the rate of the bot according to need,
	# Faster the rate, faster it will speak, vice versa for slower.

	engine.setProperty('rate', 150)

	# Increase or decrease the bot's volume
	
	volume = engine.getProperty('volume')
	engine.setProperty('volume', 1.0)

	voices = engine.getProperty('voices')
	engine.say( "  Hello "+name+ " I am sheela, your personal Talking Healthcare Chatbot." )
	engine.runAndWait()
	
	engine.say(" To continue via voice chat press 1, To continue via texting press 2. ")
	engine.runAndWait()

	press=int(input("\nPlease Enter Your response here :"))
	
	if(press==1):

		while True or final.lower() == 'True':
			
			engine.say(" You may tell me your symptoms now." )
			engine.runAndWait()
			
			symptom=input("\nYou may tell me your symptoms now.\n\n")
			engine.runAndWait()
			
			try:
				
				engine.say(" You said {}".format(symptom))
				engine.runAndWait()
				
				print("\nScanning our database for your symptom. Please wait.\n")
				engine.runAndWait()
				
				print("\nWhile we search for your disease. would you like to share your mobile number for future references...")
				mob=int(input("Please enter Mobile number here : ")) 
				print()
				
				# Calling the function by passing the voice inputted
				# symptoms converted into string
				
				calling_the_bot(symptom,press)
			
			except sr.UnknownValueError:
				
				engine.say("Sorry, Either your symptom is unclear to me or it is not present in our database. Please Try Again.")
				engine.runAndWait()
				print("Sorry, Either your symptom is unclear to me or it is not present in our database. Please Try Again.")
			
			finally:
				
				print("\nIf you want to continue please say True otherwise type False.\n")
				engine.runAndWait()

			final=input("\nEnter Your response here :")
			
			if final.lower() == 'no' or final.lower() == 'please exit' or final.lower() == 'false' or final.lower() == 'exit' or final.lower() == 'stop':
				
				engine.say(" Thank You. wish you a speedy recovery, Shutting Down now.\n")
				engine.runAndWait()
				
				print("\n\nBot has been stopped by the user\n")
				exit(0) # Program stopped 
	
	
	elif(press==2):
		
		while True or final.lower() == 'True':
			
			symptom=input("\nYou may tell me your symptoms now.\n\n")
			engine.runAndWait()
			
			try:
				print("\nScanning our database for your symptom. Please wait.")
				engine.runAndWait()
				
				print("\nWhile we search for your disease. would you like to share your mobile number for future references...\n")
				mob=int(input("Please enter Mobile number here : ")) 
				print()

				# Mobile number stored in buffer for now
				# Calling the function by passing the voice inputted
				# symptoms converted into string
				
				calling_the_bot(symptom,press)
			
			except sr.UnknownValueError:
				
				print("Sorry, Either your symptom is unclear to me or it is not present in our database. Please Try Again.")
				engine.runAndWait()
				print("Sorry, Either your symptom is unclear to me or it is not present in our database. Please Try Again.")
			
			finally:
				
				print("\nIf you want to continue please say True otherwise type False.")
				engine.runAndWait()

			final=input("\nEnter Your response here :")
			
			if final.lower() == 'no' or final.lower() == 'please exit' or final.lower() == 'false' or final.lower() == 'exit' or final.lower() == 'stop':
				
				engine.say("\n Thank You. wish you a speedy recovery, Shutting Down now.")
				engine.runAndWait()
				
				print("\n\nBot has been stopped by the user")
				exit(0) # Program stopped
