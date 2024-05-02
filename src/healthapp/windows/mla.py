# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.app import HealthApp
from healthapp.style import create_border
from healthapp.machine_learning import perform_prediction
# -------------------------------------------------------------------------------------------------------#


class MLA():
    def __init__(self, app: HealthApp):
        self.app = app

        self.hd_label = toga.Label("Heart Disease Prediction:  N/A",
                                   style=Pack(font_size=15, padding=(5, 5)))
        self.d_label = toga.Label("Diabetes Prediction:  Coming Soon",
                                   style=Pack(font_size=15, padding=(5, 5)))
        self.sd_label = toga.Label("Sleep Disorder Prediction:  Coming Soon",
                                   style=Pack(font_size=15, padding=(5, 5)))

    def get_content(self) -> toga.Box:
        content = toga.Box(style=Pack(
            direction=COLUMN, background_color="#e0965e"))

        # Main box + choice box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5))

        # button for behavioural analysis
        title_label = toga.Label("Health Analysis",
                               style=Pack(font_size=20, padding=(0, 2)))
        header_box.add(title_label)
        
        main_box.add(self.hd_label)
        main_box.add(self.d_label)
        main_box.add(self.sd_label)

        refresh_button = toga.Button('Refresh Analysis', on_press=self.refresh_handler, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        refresh_box = create_border(refresh_button, inner_color="#fbf5cc")
        footer_box.add(refresh_box)

        main_black_box.add(main_box)

        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

    def refresh_handler(self, widget):
        prediction_percentage = self.prediction_handler()
        if(prediction_percentage == "Unknown"):
            # show alert to user, data is missing:
            self.app.main_window.error_dialog("Data Missing", "BMI data is missing, please go to main menu and fill out 'personal details'.")
            self.hd_label.text = f"Heart Disease Prediction:  N/A"
        else:
            self.hd_label.text = f"Heart Disease Prediction:  {prediction_percentage:.2f}%"

        #self.d_label.text = "Diabetes Prediction:  Coming Soon"
        #self.sd_label.text = "Sleep Disorder Prediction:  Coming Soon"
    
    def get_input_data(self):
        # Construct the input data list using the user's attributes
        input_data = [
        [self.app.user.highbp, self.app.user.highcol, self.app.user.bmi, self.app.user.smoker, self.app.user.stroke, self.app.user.diabetes,
         self.app.user.physact, self.app.user.alcohol, self.app.user.physhealth, self.app.user.diffwalking, self.app.user.sex, self.app.user.age]
        ]
        
        return input_data

    def prediction_handler(self):
        # Get the input data for prediction
        input_data = self.get_input_data()

        # Perform prediction using the input data
        try:
            prediction_result = perform_prediction(self.app, input_data)
        except Exception as e:
            print("MLA Error:", e)
            prediction_result = "Unknown"

        return prediction_result