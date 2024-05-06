# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
# -------------------------------------------------------------------------------------------------------#


class Diabetes():
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

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        # label + button for diabetes
        diabetes_label = toga.Label("Do you have diabetes?", style=Pack(
            color='black', font_size=15, padding=(0, 5)))

        yes_button = toga.Button('Yes', on_press=self.diabetes_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        yes_box = create_border(
            yes_button, inner_color="#fbf5cc")

        no_button = toga.Button('No', on_press=self.diabetes_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        no_box = create_border(
            no_button, inner_color="#fbf5cc")

        # adding labels to page
        header_box.add(diabetes_label)

        main_box.add(toga.Label(""))
        for button in [yes_box, no_box, back_box]:
            if button != back_box:
                main_box.add(button)
                main_box.add(toga.Label(""))
            else:
                footer_box.add(button)

        main_black_box.add(main_box)

        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

    def diabetes_handler(self, widget):
        # Update the diabetes variable based on the user's selection
        self.app.user.diabetes = (1 if widget.text == 'Yes' else 0)
        self.app.user.save()
        self.app.main_window.info_dialog('Success', 'Diabetes saved successfully')

    def back_handler(self, widget):
        self.app.show_lifestyle()
