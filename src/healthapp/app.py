"""
Health Application to detect chronic conditions with machine learning for decision making and pose detection
"""
#-------------------------------------------------------------------------------------------------------#

# base imported modules
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

from healthapp.user import User

#-------------------------------------------------------------------------------------------------------#

# class for start menu of the app
class HealthApp(toga.App):

    def startup(self, main_window=None):
        # Create the apps data folder
        # self.paths.data is the directory where we can read/write to and have it persist after reboot/update etc etc.
        self.paths.data.mkdir(parents=True, exist_ok=True)

        # Create the main window
        if main_window is None:
            self.main_window = toga.MainWindow(title=self.formal_name)
        else:
            self.main_window = main_window

        # Login/Register
        from healthapp.login import showAuthPage
        showAuthPage(self)
    
    def login_handler(self, user: User):
        self.user = user # Holds all user info. (see User class for details)
        print("User logged in: " + str(user))
        self.show_main()

    def show_main(self):
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self, self.app)

    def update_content(self, content) -> None:
        self.main_window.content = content
        self.main_window.show()

#-------------------------------------------------------------------------------------------------------#
