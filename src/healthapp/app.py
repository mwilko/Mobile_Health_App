"""
Health Application to detect chronic conditions with machine learning for decision making and pose detection
"""
#-------------------------------------------------------------------------------------------------------#

# base imported modules
from os import mkdir
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

# import the Machine Learning model
import numpy as np
import pandas as pd

# import the Image Processing library
# import torchvision as tv # unsure if this lib works, not tested

#-------------------------------------------------------------------------------------------------------#

# class for start menu of the app
class HealthApp(toga.App):

    def startup(self):
        # Create the main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        
        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))

        # logo image
        # logo_image_path = ""

        # title label
        title_label = toga.Label("Health Application", style=Pack(font_size=20, padding=(0, 10)))

        # start button
        start_button = toga.Button('Start', on_press=self.start_button_handler, style=Pack(padding=10))

        # add components to the main box
        main_box.add(title_label)
        main_box.add(start_button)

        # add main_box to the main container
        main_container.add(main_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

        # Show the main window
        self.main_window.show()

    def start_button_handler(self, widget):
        # add logic for start button
        print("Start button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        ChoiceMenu(self.main_window, self)

#-------------------------------------------------------------------------------------------------------#

# ChoiceMenu class for the choice menu
class ChoiceMenu:
    def __init__(self, main_window, app):
        # store app and main_window in a variable
        self.app = app 
        self.main_window = main_window  # store main_window

        # Choice box for additional content
        choice_box = toga.Box(style=Pack(padding=20))

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # button for choices
        analyse_gait_button = toga.Button('Analyse Gait', on_press=self.gait_analysis_handler, style=Pack(padding=10))
        personal_details_button = toga.Button('Personal Details', on_press=self.personal_details_handler, style=Pack(padding=10))
        sleep_button = toga.Button('Sleep', on_press=self.sleep_handler, style=Pack(padding=10))
        lifestyle_button = toga.Button('Lifestyle', on_press=self.lifestyle_handler, style=Pack(padding=10))
        cognition_button = toga.Button('Cognition', on_press=self.cognition_handler, style=Pack(padding=10))
        heart_rate_button = toga.Button('Heart Rate', on_press=self.heart_rate_handler, style=Pack(padding=10))
        nutrition_button = toga.Button('Nutrition', on_press=self.nutrition_handler, style=Pack(padding=10))
        #return to main menu with back button
        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=10)) 

        # add buttons to the choice box
        choice_box.add(analyse_gait_button)
        choice_box.add(personal_details_button)
        choice_box.add(sleep_button)
        choice_box.add(lifestyle_button)
        choice_box.add(cognition_button)
        choice_box.add(heart_rate_button)
        choice_box.add(nutrition_button)
        choice_box.add(back_button)

        # add choice_box to the main container
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container
    
    # buttons to select the choice, takes the user to the respective page
    def gait_analysis_handler(self, widget):
        #add logic
        print("Gait Analysis button pressed!")
        AnalyseGait(self.main_window, self.app)

    def personal_details_handler(self, widget):
        print("Personal Details button pressed!")
        PersonalDetails(self.main_window, self.app) 

    def sleep_handler(self, widget):
        print("Sleep button pressed!")
        Sleep(self.main_window, self.app)

    def lifestyle_handler(self, widget):
        print("Lifestyle button pressed!")
        Lifestyle(self.main_window, self.app)

    def cognition_handler(self, widget):
        print("Cognition button pressed!")
        Cognition(self.main_window, self.app)

    def heart_rate_handler(self, widget):
        print("Heart Rate button pressed!")
        HeartRate(self.main_window, self.app)

    def nutrition_handler(self, widget):
        print("Nutrition button pressed!")
        Nutrition(self.main_window, self.app)

    def back_handler(self, widget):
        print("Back button pressed!")
        # call the startup method of the app instance
        self.app.startup()
#-------------------------------------------------------------------------------------------------------#

class AnalyseGait():
    def __init__(self, main_window, app):
        self.app = app 
        self.main_window = main_window

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))

        # Choice box for additional content
        choice_box = toga.Box(style=Pack(padding=20))
    
        # button for gait analysis
        analyse_gait_button = toga.Button('Analyse Gait', on_press=self.analyse_gait_handler, style=Pack(padding=10))
        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=10))

        main_box.add(analyse_gait_button)
        main_box.add(back_button)

        # add choice_box to the main container
        main_container.add(main_box)
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    async def analyse_gait_handler(self, widget):
        print("Analyse Gait button pressed!")

        # Here to make sure numpy gets added (think of it as a little test)
        n = np.array([1,2,3])
        print(n)

        # Note this doesnt return on iOS/macOS yet, fully working on android.
        if await self.app.camera.request_permission():
            photo = await self.app.camera.take_photo()
            # make dir if not exist (does not exist by default on android unconfirmed on ios)
            # mkdir(str(self.paths.data))
            file = str(self.app.paths.data) + "/paths.png"
            print("Saved picture to: " + file)
            photo.save(file)
        else:
            print("No permission for photo.")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        ChoiceMenu(self.main_window, self.app)


#-------------------------------------------------------------------------------------------------------#

class PersonalDetails():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window 
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))
        choice_box = toga.Box(style=Pack(padding=20))

        # button for physical analysis
        pd_button = toga.Button('Personal Details', on_press=self.pd_class_handler, style=Pack(padding=10))
        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=10))

        main_box.add(pd_button)
        main_box.add(back_button)

        # add main_box to the main container
        main_container.add(main_box)
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def pd_class_handler(self, widget):
        #add logic
        print("Personal Details button pressed!")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        ChoiceMenu(self.main_window, self.app)

#-------------------------------------------------------------------------------------------------------#

class Sleep():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))
        choice_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        s_button = toga.Button('Sleep', on_press=self.s_class_handler, style=Pack(padding=10))
        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=10))

        main_box.add(s_button)
        main_box.add(back_button)

        # add main_box to the main container
        main_container.add(main_box)
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def s_class_handler(self, widget):
        #add logic
        print("Sleep button pressed!")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        ChoiceMenu(self.main_window, self.app)  

#-------------------------------------------------------------------------------------------------------#

class Lifestyle():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))
        choice_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        ls_button = toga.Button('Lifestyle', on_press=self.ls_class_handler, style=Pack(padding=10))
        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=10))

        main_box.add(ls_button)
        main_box.add(back_button)

        # add main_box to the main container
        main_container.add(main_box)
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def ls_class_handler(self, widget):
        #add logic
        print("Lifestyle button pressed!")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        ChoiceMenu(self.main_window, self.app)

#-------------------------------------------------------------------------------------------------------#
        
class Cognition():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))
        choice_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        c_button = toga.Button('Cognition', on_press=self.c_class_handler, style=Pack(padding=10))
        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=10))

        main_box.add(c_button)
        main_box.add(back_button)

        # add main_box to the main container
        main_container.add(main_box)
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def c_class_handler(self, widget):
        #add logic
        print("Cognitive button pressed!")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        ChoiceMenu(self.main_window, self.app)

#-------------------------------------------------------------------------------------------------------#
        
class HeartRate():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box + choice box for the initial content
        main_box = toga.Box(style=Pack(padding=20))
        choice_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        hr_button = toga.Button('Heart Rate', on_press=self.hr_class_handler, style=Pack(padding=10))
        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=10))

        main_box.add(hr_button)
        main_box.add(back_button)

        # add main_box to the main container
        main_container.add(main_box)
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def hr_class_handler(self, widget):
        #add logic
        print("Heart Rate button pressed!")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        ChoiceMenu(self.main_window, self.app)

#-------------------------------------------------------------------------------------------------------#

class Nutrition():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))
        choice_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        n_button = toga.Button('Nutrition', on_press=self.n_class_handler, style=Pack(padding=10))
        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=10))

        main_box.add(n_button)
        main_box.add(back_button)

        # add main_box to the main container
        main_container.add(main_box)
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def n_class_handler(self, widget):
        #add logic
        print("Nutrition button pressed!")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        ChoiceMenu(self.main_window, self.app)

#-------------------------------------------------------------------------------------------------------#

def main():
    return HealthApp()
