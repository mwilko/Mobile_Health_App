#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
#-------------------------------------------------------------------------------------------------------#

class Nutrition():
    def __init__(self, app: HealthApp):
        self.app = app
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:

        content = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))
        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        n_label = toga.Label("How much calories do you consume per day: ", style=Pack(font_size=15, padding=(0, 10)))
        nless_1000_button = toga.Button('Less than 1000 calories', on_press=self.n_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        nless_1000_box = create_border(nless_1000_button, inner_color="#fbf5cc")

        n1000_1499_button = toga.Button('1000 - 1500 calories', on_press=self.n_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        n1000_1499_box = create_border(n1000_1499_button, inner_color="#fbf5cc")

        n1500_2000_button = toga.Button('1500 - 2000 calories', on_press=self.n_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        n1500_2000_box = create_border(n1500_2000_button, inner_color="#fbf5cc")

        n2000_plus_button = toga.Button('More than 2000 calories', on_press=self.n_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        n2000_plus_box = create_border(n2000_plus_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        #formatting the layout
        header_box.add(n_label)

        main_box.add(toga.Label(""))
        for button in [nless_1000_box, n1000_1499_box, n1500_2000_box,
                        n2000_plus_box, back_box]:
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

    def n_handler(self, widget):
        #add logic
        print("Nutrition button pressed!")
        # Access the label attribute of the button widget to get the user's selection
        nutrition = widget.text
        print(f"Nutrition: {nutrition}")

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_menu()