#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.app import HealthApp
from healthapp.style import create_border

from healthapp.machine_learning import perform_prediction
#-------------------------------------------------------------------------------------------------------#

# ChoiceMenu class for the choice menu
class ChoiceMenu:
    def __init__(self, app: HealthApp):
        # store app in a variable
        self.app = app
        self.app.update_content(self.get_content())

        print("ChoiceMenu class running...")

    def get_content(self) -> toga.Box:

        content = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))
        # Create the ml box as per prototype
        # ml results would be displayed inside of the box
        machine_learning_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        # Choice box for additional content
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))

        # Label for the choice menu
        name_label = toga.Label(f"Welcome, {self.app.user.first} {self.app.user.last}", style=Pack(font_size=12, padding=(5, 10)))
        ml_label = toga.Label("Machine Learning Algorithm has no data", style=Pack(font_size=15, padding=(0, 10)))
        
        # Calculate prediction percentage -----------------------------------------
        #input_data = [[1, 1, 100, 1, 1, 1, 1, 1, 1, 1, 1, 70]]  # Example input data
        #prediction_percentage = perform_prediction(input_data)

        # Update ML label text with prediction percentage
        prediction_percentage = self.prediction_handler()
        ml_label.text = f"Prediction: {prediction_percentage:.1f}%"

        machine_learning_box.add(name_label)
        machine_learning_box.add(ml_label)

        machine_learning_box.add(name_label)
        machine_learning_box.add(ml_label)
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

        nutrition_button = toga.Button('Nutrition', on_press=self.prediction_handler, style=Pack(color = 'black', background_color="#fbf5cc", padding=(-3)))
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
        print("Pose Analysis button pressed!")
        from healthapp.windows.analyse_pose import AnalysePose
        AnalysePose(self.app)

    def personal_details_handler(self, widget):
        print("Personal Details button pressed!")
        from healthapp.windows.personal_details import PersonalDetails
        PersonalDetails(self.app) 

    def sleep_handler(self, widget):
        print("Sleep button pressed!")
        from healthapp.windows.sleep import Sleep
        Sleep(self.app)

    def lifestyle_handler(self, widget):
        print("Lifestyle button pressed!")
        from healthapp.windows.lifestyle import Lifestyle
        Lifestyle(self.app)

    def cognition_handler(self, widget):
        print("Cognition button pressed!")
        from healthapp.windows.cognitive import Cognition
        Cognition(self.app)

    def heart_rate_handler(self, widget):
        print("Heart Rate button pressed!")
        from healthapp.windows.heart_rate import HeartRate
        HeartRate(self.app)

    def nutrition_handler(self, widget):
        print("Nutrition button pressed!")
        from healthapp.windows.nutrition import Nutrition
        Nutrition(self.app)
        
    def get_input_data(self):
       
        # Construct the input data list using the user's attributes
        input_data = [
        [self.app.user.highbp, self.app.user.highcol, self.app.user.bmi, self.app.user.smoker, self.app.user.stroke, self.app.user.diabetes,
         self.app.user.physact, self.app.user.alcohol, self.app.user.physhealth, self.app.user.diffwalking, self.app.user.sex, self.app.user.age]
        ]
        
        return input_data
    
    def prediction_handler(self):
        print("Prediction button pressed!")

        # Get the input data for prediction
        input_data = self.get_input_data()

        # Perform prediction using the input data
        prediction_result = perform_prediction(self.app, input_data)

        # Display prediction result
        print("Prediction:", prediction_result)
        return prediction_result
