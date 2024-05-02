#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
#-------------------------------------------------------------------------------------------------------#

class Sleep():
    def __init__(self, app: HealthApp):
        self.app = app
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:

        content = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))
        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5))

        # objects for behavioural analysis
        header_label = toga.Label("Sleep Schedule: ", style=Pack(font_size=15, padding=(0, 10)))

        s_label = toga.Label("How many hours of sleep do you get?", style=Pack(font_size=15, padding=(0, 10)))

        self.s_text_input = toga.TextInput(placeholder='hours', style=Pack(background_color="#fbf5cc"), value=self.app.user.sleep)
        s_text_input_box = create_border(self.s_text_input, inner_color="#fbf5cc")

        submit_button = toga.Button('Submit', on_press=self.sleep_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        submit_box = create_border(submit_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        header_box.add(header_label)

        main_box.add(toga.Label(""))
        main_box.add(s_label)
        main_box.add(s_text_input_box)

        # add buttons to the main box
        for button in [submit_box, back_box]:
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

    def sleep_handler(self, widget):
        sleep_duration = self.s_text_input.value
        if sleep_duration.isnumeric() and int(sleep_duration) > 0:
            self.app.user.sleep = int(sleep_duration)
            self.app.user.save()
            self.app.main_window.info_dialog('Success', 'Sleep saved successfully')
        else:
            self.app.main_window.error_dialog("Error!", "Input must be a positive integer.\nPlease try again.")

    def back_handler(self, widget):
        self.app.show_menu()