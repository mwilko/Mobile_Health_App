# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
# -------------------------------------------------------------------------------------------------------#


class Nutrition():
    def __init__(self, app: HealthApp):
        self.app = app
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:

        content = toga.Box(style=Pack(
            direction=COLUMN, background_color="#e0965e"))
        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5))

        h_label = toga.Label("Nutrition", style=Pack(font_size=20, padding=(0, 10)))
        header_box.add(h_label)

        n_label = toga.Label("How many calories do you consume\nroughly, per day (eg 1500): ",
                             style=Pack(font_size=15, padding=(5, 15)))
        
        self.cal_input = toga.TextInput(placeholder='1500 Calories', style=Pack(background_color="#fbf5cc", padding=(0, 0)))
        cal_input_box = create_border(self.cal_input, inner_color="#fbf5cc", padding=(0, 13, 0))

        submit_button = toga.Button('Submit', on_press=self.submit_handler, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        submit_box = create_border(submit_button, inner_color="#fbf5cc")


        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        for button in [n_label, cal_input_box, submit_box, back_box]:
            if button != back_box:
                main_box.add(button)
                main_box.add(toga.Label(""))
            else:
                footer_box.add(button)

        main_black_box.add(main_box)

        # add main_box to the main container
        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

    def submit_handler(self, widget):
        calories = self.cal_input.value
        if calories == "":
            self.app.main_window.error_dialog('Error', 'Please enter the number of calories you consume daily.')
            return
        if not calories.isdigit():
            self.app.main_window.error_dialog('Error', 'Please enter a valid number of calories.')
            return
        if int(calories) <= 0:
            self.app.main_window.error_dialog('Error', 'Please enter a valid number of calories.')
            return
        self.app.user.calories = int(calories)
        self.app.user.save()
        self.app.main_window.info_dialog('Success', 'Calories saved successfully')

    def back_handler(self, widget):
        self.app.show_menu()
