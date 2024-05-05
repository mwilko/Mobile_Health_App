#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.app import HealthApp
from healthapp.windows.mla import MLA
from healthapp.style import create_border
#-------------------------------------------------------------------------------------------------------#

# ChoiceMenu class for the choice menu
class ChoiceMenu:

    cognitive_score = 0 # to store the score of the user's cognitive analysis

    def increment_score():
        ChoiceMenu.cognitive_score += 1
    
    def reset_score():
        ChoiceMenu.cognitive_score = 0

    def __init__(self, app: HealthApp):
        # store app in a variable
        self.app = app

        # With menu bar:
        cont = toga.OptionContainer(content=[
            toga.OptionItem("Main Menu", self.get_content()),
            toga.OptionItem("Health Analysis", MLA(self.app).get_content()),
        ])
        self.app.update_content(cont)

        # Without menu bar:
        # self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:

        content = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))
        # Create the ml box as per prototype
        # ml results would be displayed inside of the box
        machine_learning_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        # Choice box for additional content
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))

        # Label for the choice menu
        name_label = toga.Label(f"Welcome, {self.app.user.first} {self.app.user.last}", style=Pack(color='black', font_size=15, padding=(0, 10)))
        machine_learning_box.add(name_label)
        #--------------------------------------------------------------------------
        # button for choices
        analyse_pose_button = toga.Button('Pose Analysis', on_press=self.pose_analysis_handler, style=Pack(color = 'black', background_color="#fbf5cc", padding=(-3)))
        pose_box = create_border(analyse_pose_button, inner_color="#fbf5cc")

        personal_details_button = toga.Button('Personal Details', on_press=self.personal_details_handler, style=Pack(color = 'black', background_color="#fbf5cc", padding=(-3)))
        pd_box = create_border(personal_details_button, inner_color="#fbf5cc")

        sleep_button = toga.Button('Sleep', on_press=self.sleep_handler, style=Pack(color = 'black', background_color="#fbf5cc", padding=(-3)))
        sleep_box = create_border(sleep_button, inner_color="#fbf5cc")

        lifestyle_button = toga.Button('Lifestyle', on_press=self.lifestyle_handler, style=Pack(color = 'black', background_color="#fbf5cc", padding=(-3)))
        lifestyle_box = create_border(lifestyle_button, inner_color="#fbf5cc")

        cognition_button = toga.Button('Cognition', on_press=self.cognition_handler, style=Pack(color = 'black', background_color="#fbf5cc", padding=(-3)))
        cognition_box = create_border(cognition_button, inner_color="#fbf5cc")

        heart_rate_button = toga.Button('Heart Rate', on_press=self.heart_rate_handler, style=Pack(color = 'black', background_color="#fbf5cc", padding=(-3)))
        heart_rate_box = create_border(heart_rate_button, inner_color="#fbf5cc")

        nutrition_button = toga.Button('Nutrition', on_press=self.nutrition_handler, style=Pack(color = 'black', background_color="#fbf5cc", padding=(-3)))
        nutrition_box = create_border(nutrition_button, inner_color="#fbf5cc")

        main_box.add(toga.Label("")) # Creates a space in background colour. ("Spacer")
        for box in [pose_box, pd_box, sleep_box, lifestyle_box,
                     cognition_box, heart_rate_box, nutrition_box]:
            main_box.add(box)
        main_box.add(toga.Label("")) # Creates a space in background colour. ("Spacer")

        main_black_box.add(main_box) # Outer black border.

        for box in [machine_learning_box, main_black_box]:
            content.add(box)
            
        return content

    # buttons to select the choice, takes the user to the respective page
    def pose_analysis_handler(self, widget):
        from healthapp.windows.analyse_pose import AnalysePose
        AnalysePose(self.app)

    def personal_details_handler(self, widget):
        from healthapp.windows.personal_details import PersonalDetails
        PersonalDetails(self.app) 

    def sleep_handler(self, widget):
        from healthapp.windows.sleep import Sleep
        Sleep(self.app)

    def lifestyle_handler(self, widget):
        from healthapp.windows.lifestyle import Lifestyle
        Lifestyle(self.app)

    def cognition_handler(self, widget):
        from healthapp.windows.cognitive import Cognition
        Cognition(self.app)

    def heart_rate_handler(self, widget):
        from healthapp.windows.heart_rate import HeartRate
        HeartRate(self.app)

    def nutrition_handler(self, widget):
        from healthapp.windows.nutrition import Nutrition
        Nutrition(self.app)
