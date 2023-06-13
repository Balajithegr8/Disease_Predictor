import pickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

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

# Call the predictDisease function with the symptoms parameter
symptoms = "Acidity,Indigestion,Stiff Neck"
predictions = predictDisease(symptoms)
print("final prediction is",predictions['final_prediction'])
