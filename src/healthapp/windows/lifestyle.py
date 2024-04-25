# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
# -------------------------------------------------------------------------------------------------------#


class Lifestyle():
    def __init__(self, app: HealthApp):
        self.app = app
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:
        content = toga.Box(style=Pack(
            direction=COLUMN, background_color="#e0965e"))
        # Create an instance of variable to store the user's selection
        self.exercise_selection = None

        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5))

        # label + button for behavioural analysis
        lifestyle_label = toga.Label("Select a lifestyle test: ", style=Pack(
            color='black', font_size=14, padding=(0, 5)))

        exercise_button = toga.Button('Exercise', on_press=self.exercise_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        exercise_box = create_border(exercise_button, inner_color="#fbf5cc")

        highbp_button = toga.Button('Blood Pressure', on_press=self.highbp_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        highbp_box = create_border(highbp_button, inner_color="#fbf5cc")

        highcol_button = toga.Button('Cholesterol', on_press=self.highcol_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        highcol_box = create_border(highcol_button, inner_color="#fbf5cc")

        smoker_button = toga.Button('Smoker', on_press=self.smoker_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        smoker_box = create_border(smoker_button, inner_color="#fbf5cc")

        stroke_button = toga.Button('Stroke', on_press=self.stroke_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        stroke_box = create_border(stroke_button, inner_color="#fbf5cc")

        diabetes_button = toga.Button('Diabetes', on_press=self.diabetes_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        diabetes_box = create_border(diabetes_button, inner_color="#fbf5cc")

        alcohol_button = toga.Button('Alcohol', on_press=self.alcohol_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        alcohol_box = create_border(alcohol_button, inner_color="#fbf5cc")

        walking_button = toga.Button('Walking', on_press=self.walking_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        walking_box = create_border(walking_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        # adding labels to page
        header_box.add(lifestyle_label)

        main_box.add(toga.Label(""))
        for button in [exercise_box, walking_box, highbp_box, highcol_box,
                       diabetes_box, smoker_box, stroke_box, back_box]:
            if button != back_box:
                main_box.add(button)
            else:
                footer_box.add(button)
        main_box.add(toga.Label(""))

        main_black_box.add(main_box)

        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

    def exercise_handler(self, widget):
        print("Exercise button pressed!")
        self.app.show_mla_exercise()

    def highbp_handler(self, widget):
        print("High blood pressure button pressed!")
        self.app.show_mla_highbp()

    def highcol_handler(self, widget):
        print("High cholesterol button pressed!")
        self.app.show_mla_highcol()

    def smoker_handler(self, widget):
        print("Smoker button pressed!")
        self.app.show_mla_smoker()

    def stroke_handler(self, widget):
        print("Stroke button pressed!")
        self.app.show_mla_stroke()

    def diabetes_handler(self, widget):
        print("Diabetes button pressed!")
        self.app.show_mla_diabetes()

    def alcohol_handler(self, widget):
        print("Alcohol button pressed!")
        self.app.show_mla_alcohol()

    def walking_handler(self, widget):
        print("Walking button pressed!")
        self.app.show_mla_walking()

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_menu()
