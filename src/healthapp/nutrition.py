import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border

class Nutrition():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        footer_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        n_label = toga.Label("Select the number of calories you consume per day: ", style=Pack(font_size=15, padding=(0, 10)))
        nless_1000_button = toga.Button('Less than 1000 calories', on_press=self.n_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        nless_1000_box = create_border(nless_1000_button)

        n1000_1499_button = toga.Button('1000 - 1500 calories', on_press=self.n_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        n1000_1499_box = create_border(n1000_1499_button)

        n1500_2000_button = toga.Button('1500 - 2000 calories', on_press=self.n_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        n1500_2000_box = create_border(n1500_2000_button)

        n2000_plus_button = toga.Button('More than 2000 calories', on_press=self.n_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        n2000_plus_box = create_border(n2000_plus_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        #formatting the layout
        header_box.add(n_label)

        for button in [nless_1000_box, n1000_1499_box, n1500_2000_box,
                        n2000_plus_box, back_box]:
            if button != back_box:
                main_box.add(button)
            else:
                footer_box.add(button)

        # add main_box to the main container
        for box in [header_box, main_box, footer_box]:
            main_container.add(box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def n_handler(self, widget):
        #add logic
        print("Nutrition button pressed!")
        # Access the label attribute of the button widget to get the user's selection
        nutrition = widget.text
        print(f"Nutrition: {nutrition}")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)