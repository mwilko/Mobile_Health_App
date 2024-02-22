import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

import healthapp.app as HealthApp

# ChoiceMenu class for the choice menu
class ChoiceMenu:
    print("ChoiceMenu class running...")

    def __init__(self, main_window: toga.MainWindow, app: HealthApp):
        # store app and main_window in a variable
        self.app = app 
        self.main_window = main_window  # store main_window

        # Create the ml box as per prototype
        # ml results would be displayed inside of the box
        machine_learning_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        # Choice box for additional content
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Label for the choice menu
        name_label = toga.Label(f"Welcome, {self.app.user.first} {self.app.user.last}", style=Pack(font_size=12, padding=(5, 10)))
        ml_label = toga.Label("Machine Learning Algorithm has no data", style=Pack(font_size=15, padding=(0, 10)))

        machine_learning_box.add(name_label)
        machine_learning_box.add(ml_label)

        # button for choices

        analyse_gait_button = toga.Button('Analyse Gait', on_press=self.gait_analysis_handler, style=Pack(padding=2), enabled=(toga.platform.current_platform.lower() != "ios"))
        personal_details_button = toga.Button('Personal Details', on_press=self.personal_details_handler, style=Pack(padding=2))
        sleep_button = toga.Button('Sleep', on_press=self.sleep_handler, style=Pack(padding=2))
        lifestyle_button = toga.Button('Lifestyle', on_press=self.lifestyle_handler, style=Pack(padding=2))
        cognition_button = toga.Button('Cognition', on_press=self.cognition_handler, style=Pack(padding=2))
        heart_rate_button = toga.Button('Heart Rate', on_press=self.heart_rate_handler, style=Pack(padding=2))
        nutrition_button = toga.Button('Nutrition', on_press=self.nutrition_handler, style=Pack(padding=2))
        
        for button in [analyse_gait_button, personal_details_button, sleep_button,
                        lifestyle_button, cognition_button, heart_rate_button, 
                        nutrition_button]:
            main_box.add(button)

        # add boxes to the main container
        main_container.add(machine_learning_box)
        main_container.add(main_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container
    
    # buttons to select the choice, takes the user to the respective page
    def gait_analysis_handler(self, widget):
        #add logic
        print("Gait Analysis button pressed!")
        HealthApp.AnalyseGait(self.main_window, self.app)

    def personal_details_handler(self, widget):
        print("Personal Details button pressed!")
        HealthApp.PersonalDetails(self.main_window, self.app) 

    def sleep_handler(self, widget):
        print("Sleep button pressed!")
        HealthApp.Sleep(self.main_window, self.app)

    def lifestyle_handler(self, widget):
        print("Lifestyle button pressed!")
        HealthApp.Lifestyle(self.main_window, self.app)

    def cognition_handler(self, widget):
        print("Cognition button pressed!")
        HealthApp.Cognition(self.main_window, self.app)

    def heart_rate_handler(self, widget):
        print("Heart Rate button pressed!")
        HealthApp.HeartRate(self.main_window, self.app)

    def nutrition_handler(self, widget):
        print("Nutrition button pressed!")
        HealthApp.Nutrition(self.main_window, self.app)