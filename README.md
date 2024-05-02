![Static Badge](https://img.shields.io/badge/build-android-green) ![Static Badge](https://img.shields.io/badge/build-ios-red) 

![GitHub last commit](https://img.shields.io/github/last-commit/mwilko/Mobile_Health_App) ![Static Badge](https://img.shields.io/badge/status-development-yellow)


# Mobile Health App to Detect Chronic Conditions

Team Software Engineering project. This project is a mobile application built in BeeWare, which utilies machine learning algorithms and a pose detection module to detect chronic conditions in users.

## How to install:

Install Python 3.9. This version of language is needed for the modules to execute properly.
```
$ python3 --version
```
If your Python version is stated as 3.9, we can continue, if not create a virual enviroment with that Python version and be sure to select the Python 3.9 interperator:
```
$ python3 -m venv env
$ source env/bin/activate
```

Next, install Briefcase and Toga which are BeeWare libaries:
```
$ python -m pip install briefcase
$ python -m pip install toga
```
You may need to include the project dependencies:
```
$ pip install numpy, pandas, opencv-python,scikit-learn, matplotlib,
  tflite-runtime
```

## How to Run:

For the first time when running the app, you may need to install the Android SDK:
```
$ briefcase create android
```
After this you should be able to run the application with the following:
```
$ briefcase run android -r -u
```
This would compile the application where the terminal will take you through the proccess of hosting the app via a virutal device which you select.

Thanks for taking the time to visit our application.

Regards,
Development Team
(26551623@students.lincoln.ac.uk, 27203747@students.lincoln.ac.uk, 26457815@students.lincoln.ac.uk, 26379294@students.lincoln.ac.uk)
