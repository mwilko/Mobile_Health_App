# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
# -------------------------------------------------------------------------------------------------------#


class Exercise():
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
        exercise_label = toga.Label("How many minutes of exercise\ndo you do per week?", style=Pack(color='black', font_size=15, padding=(0, 10)))

        self.text_input = toga.TextInput(placeholder='30 Minutes', style=Pack(background_color="#fbf5cc"), value=self.app.user.exercise)
        text_input_box = create_border(self.text_input, inner_color="#fbf5cc")

        submit_button = toga.Button('Submit', on_press=self.exercise_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        submit_box = create_border(submit_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        # adding labels to page
        header_box.add(exercise_label)

        main_box.add(toga.Label(""))
        for button in [text_input_box, submit_box, back_box]:
            if button != back_box:
                main_box.add(button)
                main_box.add(toga.Label(""))
            else:
                footer_box.add(button)

        main_black_box.add(main_box)

        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

    def exercise_handler(self, widget):
        exercise_duration = self.text_input.value
        if exercise_duration.isnumeric() and int(exercise_duration) > 0:
            self.app.user.exercise = int(exercise_duration)
            self.app.user.save()
            self.app.main_window.info_dialog('Success', 'Saved successfully')
        else:
            self.app.main_window.error_dialog("Error!", "Input must be a positive integer.\nPlease try again.")


    def back_handler(self, widget):
        self.app.show_lifestyle()
