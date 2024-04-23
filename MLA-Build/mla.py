"""

This is the main file for the Machine Learning Algorithm (MLA) module. This module is responsible for training and testing the machine learning model.

IMPORTANT: To run this file, you need to have the following libraries installed:
- pandas
- scikit-learn (MUST BE 1.3.2)
(See requirements.txt for more details)

This MLA file simply trains and builds the heartdisease pkl file which is used in the Health Application to predict the risk factor of the user on chronic conditions based on the data collection.

"""


import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

heart_data =  pd.read_csv("heart_disease.csv")
heart_data['ONE'] = 1

#print(heart_data)

features = ['HighBP', 'HighChol', 'BMI', 'Smoker', 'Stroke',
            'Diabetes', 'PhysActivity', 'HvyAlcoholConsump',
            'PhysHlth', 'DiffWalk', 'Sex', 'Age']

target_variable = 'HeartDisease'

# Prepare inputs and outputs
inputs = heart_data[features].values
outputs = heart_data[target_variable].astype(int)

# Split the data
in_tr, in_te, out_tr, out_te = train_test_split(inputs, outputs, test_size=.5, random_state=42)

# Initialize the Decision Tree Classifier
tree_d = DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=5,
                                min_samples_leaf=10, min_samples_split=3, splitter='best', random_state=42)

# Fit the model
tree_d.fit(in_tr, out_tr)

# Make predictions
prediction = tree_d.predict(in_te)

# Evaluate the model
accuracy = accuracy_score(out_te, prediction)
print(f"Accuracy: {accuracy:.2f}")



# Dump the trained decision tree classifier with Pickle
decision_tree_pkl_filename = 'HeartDisease-1.1.3.pkl'
# Open the file to save as pkl file
decision_tree_model_pkl = open(decision_tree_pkl_filename, 'wb')
pickle.dump(tree_d, decision_tree_model_pkl)
# Close the pickle instances
decision_tree_model_pkl.close()

print("Model saved as:", decision_tree_pkl_filename)
