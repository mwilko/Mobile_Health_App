'''
---------------------------- MACHINE LEARNING ALGORITHM ----------------------------
This file will contain the any needed implementation ML model for the health app,
to predict the risk factor of the user on chronic conditions based on
the data collection

DATA COMMENTED OUT FOR DEVELOPMENT TESTING AS IT CRASHES PROGRAM AT LAUNCH

'''
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp

import pickle


def perform_prediction(app, input_data):
    # Load the trained model
    path = str((app.paths.app / f"resources/machine_learning/HeartDisease-1.1.3.pkl"))
    with open(path, 'rb') as file:
        model = pickle.load(file)
    
    # Perform prediction
    probability = model.predict_proba(input_data)
    
    probability_positive_class = probability[0, 1]  # Probability of positive class (class 1)
    percentage = probability_positive_class * 100  # Convert probability to percentage
    return percentage
 
