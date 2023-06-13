import pickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import pickle

from keras.models import load_model

import numpy as np
import speech_recognition as sr	
import pyttsx3

with open("data_dict.pkl", "rb") as f:
    data_dict = pickle.load(f)

with open("final_svm_model.pkl", "rb") as f:
    final_svm_model = pickle.load(f)

with open("final_nb_model.pkl", "rb") as f:
    final_nb_model = pickle.load(f)

with open("final_rf_model.pkl", "rb") as f:
    final_rf_model = pickle.load(f)

def predictDisease(symptoms):
    symptoms = symptoms.split(",")
    
    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
        
    # reshaping the input data and converting it
    # into a suitable format for model predictions
    input_data = np.array(input_data).reshape(1, -1)
    
    # generating individual outputs
    rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]
    
    # making the final prediction by taking the mode of all predictions
    predictions_df = pd.DataFrame([rf_prediction, nb_prediction, svm_prediction])
    final_prediction = predictions_df.mode(axis=0, dropna=False).iloc[0].values[0]
    
    predictions = {
        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": svm_prediction,
        "final_prediction": final_prediction
    }
    return predictions

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
	engine.say( "  Hello "+name+ " I am chadbot, your personal Talking Healthcare Chatbot." )
	engine.runAndWait()
	
	engine.say(" To continue via voice chat press 1, To continue via texting press 2. ")
	engine.runAndWait()

	press=int(input("\nPlease Enter Your response here :"))

if(press==1):

		while True or final.lower() == 'True':
			
			engine.say(" You may select from the symptoms below." )
			print(" You may select from the symptoms below." )
			engine.runAndWait()
			with open("lamda.pkl", "rb") as f:
				retrieved_text = pickle.load(f)
				for i in retrieved_text:
					print(i)
			symptoms=input("\nYou may enter your symptoms now.\n\n")
			engine.runAndWait()
			
			try:
				
				engine.say(" You said {}".format(symptoms))
				engine.runAndWait()
				
				print("\nScanning our database for your symptom. Please wait.\n")
				engine.runAndWait()
				
				print("\nWhile we search for your disease. would you like to share your mobile number for future references...")
				mob=int(input("Please enter Mobile number here : ")) 
				print()
				
				# Calling the function by passing the voice inputted
				# symptoms converted into string
				
				predictions = predictDisease(symptoms)
				print("final prediction is",predictions['final_prediction'])
				engine.say("final prediction is",predictions['final_prediction'])
			
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
		print(" You may select from the symptoms below." )
		with open("lamda.pkl", "rb") as f:
			retrieved_text = pickle.load(f)
			for i in retrieved_text:
				print(i)
		symptoms=input("\nYou may enter your symptoms now.\n\n")
					
		try:
			print("\nScanning our database for your symptom. Please wait.")
			engine.runAndWait()
				
			print("\nWhile we search for your disease. would you like to share your mobile number for future references...\n")
			mob=int(input("Please enter Mobile number here : ")) 
			print()

				# Mobile number stored in buffer for now
				# Calling the function by passing the voice inputted
				# symptoms converted into string
				
			predictions = predictDisease(symptoms)
			print("final prediction is",predictions['final_prediction'])
			
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
