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
        physical_button = toga.Button('Physical', on_press=self.physical_handler, style=Pack(padding=10))
        behavioural_button = toga.Button('Behavioural', on_press=self.behavioural_handler, style=Pack(padding=10))

        # add buttons to the choice box
        choice_box.add(analyse_gait_button)
        choice_box.add(physical_button)
        choice_box.add(behavioural_button)

        # add choice_box to the main container
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container
    
    # buttons to select the choice, takes the user to the respective page
    def gait_analysis_handler(self, widget):
        #add logic
        print("Gait Analysis button pressed!")
        AnalyseGait(self.main_window, self.app)

    def physical_handler(self, widget):
        print("Physical button pressed!")
        Physical(self.main_window, self.app) 

    def behavioural_handler(self, widget):
        print("Behavioural button pressed!")
        Behavioural(self.main_window, self.app)


#-------------------------------------------------------------------------------------------------------#

class AnalyseGait():
    print("AnalyseGait class created")
    def __init__(self, main_window, app):
        # store app in a variable
        self.app = app 

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))

        # Choice box for additional content
        choice_box = toga.Box(style=Pack(padding=20))
    
        # button for gait analysis
        analyse_gait_button = toga.Button('Analyse Gait', on_press=self.analyse_gait_handler, style=Pack(padding=10))

        choice_box.add(analyse_gait_button)


    async def analyse_gait_handler(self, widget):
        # Here to make sure numpy gets added (think of it as a little test)
        n = np.array([1,2,3])
        print(n)

        print("Analyse Gait button pressed!")

        # Note this doesnt return on iOS/macOS yet, fully working on android.
        if await self.app.camera.request_permission():
            photo = await self.app.camera.take_photo()
            # make dir if not exist (does not exist by default on android unconfirmed on ios)
            mkdir(str(self.paths.data))
            file = str(self.app.paths.data) + "/paths.png"
            print("Saved picture to: " + file)
            photo.save(file)
        else:
            print("No permission for photo.")


#-------------------------------------------------------------------------------------------------------#

class Physical():
    print("Physical class created")
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window 
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))

        # button for physical analysis
        physical_button = toga.Button('Physical', on_press=self.physical_handler, style=Pack(padding=10))


    def physical_handler(self, widget):
        #add logic
        print("Physical button pressed!")


#-------------------------------------------------------------------------------------------------------#

class Behavioural():
    print("Behavioural class created")
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        behavioural_button = toga.Button('Behavioural', on_press=self.behavioural_handler, style=Pack(padding=10))

    def behavioural_handler(self, widget):
        #add logic
        print("Behavioural button pressed!")
    

#-------------------------------------------------------------------------------------------------------#

def main():
    return HealthApp()
