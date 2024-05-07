'''
---------------------------- MACHINE LEARNING ALGORITHM ----------------------------
This file will contain the any needed implementation ML model for the health app,
to predict the risk factor of the user on chronic conditions based on
the data collection
'''

from healthapp.config import ML_MODEL_FILES
import pickle


def perform_prediction(app, input_data):
    # Load the trained model
    path = str((app.paths.app / ML_MODEL_FILES["heart_disease"]))
    with open(path, 'rb') as file:
        model = pickle.load(file)
    
    # Perform prediction
    probability = model.predict_proba(input_data)
    
    probability_positive_class = probability[0, 1]  # Probability of positive class (class 1)
    percentage = probability_positive_class * 100  # Convert probability to percentage
    return percentage
 
