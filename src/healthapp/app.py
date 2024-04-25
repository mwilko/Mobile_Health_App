"""
Health Application to detect chronic conditions with machine learning for decision making and pose detection
"""
# -------------------------------------------------------------------------------------------------------#

# base imported modules
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

from healthapp.user import User

# -------------------------------------------------------------------------------------------------------#

# class for start menu of the app


class HealthApp(toga.App):

    def startup(self):
        # Create the apps data folder
        #  self.paths.data is the directory where we can read/write to and have it persist after reboot/update etc etc.
        self.paths.data.mkdir(parents=True, exist_ok=True)

        # Create the main window
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Login/Register
        from healthapp.windows.login import showAuthPage
        showAuthPage(self)

    def login_handler(self, user: User):
        self.user = user  # Holds all user info. (see User class for details)
        print("User logged in: " + str(user))
        self.show_menu()

    def show_menu(self):
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.windows.choice_menu import ChoiceMenu
        ChoiceMenu(self)

    def show_cognitive(self):
        # pass self as the app instance to the Cognition class
        from healthapp.windows.cognitive import Cognition
        Cognition(self)

    def show_cognitive_memory(self):
        # pass self as the app instance to the Cognition class
        from healthapp.windows.cognitive_memory import CognitiveMemory
        CognitiveMemory(self)

    def show_cognitive_math(self):
        # pass self as the app instance to the Cognition class
        from healthapp.windows.cognitive_math import CognitiveMath
        CognitiveMath(self)

    def show_cognitive_spell(self):
        # pass self as the app instance to the Cognition class
        from healthapp.windows.cognitive_spell import CognitiveSpell
        CognitiveSpell(self)

    def show_mla_smoker(self):
        # pass self as the app instance to the Lifestyle class
        from healthapp.windows.mla_smoker import Smoker
        Smoker(self)

    def show_lifestyle(self):
        # pass self as the app instance to the Lifestyle class
        from healthapp.windows.lifestyle import Lifestyle
        Lifestyle(self)

    def show_mla_exercise(self):
        # pass self as the app instance to the Lifestyle class
        from healthapp.windows.mla_exercise import Exercise
        Exercise(self)

    def show_mla_highbp(self):
        # pass self as the app instance to the Lifestyle class
        from healthapp.windows.mla_highbp import HighBP
        HighBP(self)

    def show_mla_highcol(self):
        # pass self as the app instance to the Lifestyle class
        from healthapp.windows.mla_highcol import HighCol
        HighCol(self)

    def show_mla_stroke(self):
        # pass self as the app instance to the Lifestyle class
        from healthapp.windows.mla_stroke import Stroke
        Stroke(self)

    def show_mla_diabetes(self):
        # pass self as the app instance to the Lifestyle class
        from healthapp.windows.mla_diabetes import Diabetes
        Diabetes(self)

    def show_mla_alcohol(self):
        # pass self as the app instance to the Lifestyle class
        from healthapp.windows.mla_alcohol import Alcohol
        Alcohol(self)

    def show_mla_walking(self):
        # pass self as the app instance to the Lifestyle class
        from healthapp.windows.mla_walking import Walking
        Walking(self)

    def update_content(self, content) -> None:
        self.main_window.content = content
        self.main_window.show()

# -------------------------------------------------------------------------------------------------------#
