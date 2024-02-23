import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border

class Lifestyle():
    def __init__(self, main_window, app):  # accept a main_window argument

        self.main_window = main_window
        self.app = app

        # Create an instance of variable to store the user's selection
        self.exercise_selection = None

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        footer_box = toga.Box(style=Pack(padding=20))

        # label + button for behavioural analysis
        exercise_label = toga.Label("How much exercise do you get per week?", style=Pack(font_size=15, padding=(0, 5)))
        e60_button = toga.Button('Less than 60 mins', on_press=self.lifestyle_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        e60_box = create_border(e60_button)

        e60_119_button = toga.Button('60 - 119 mins', on_press=self.lifestyle_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        e60_119_box = create_border(e60_119_button)

        e120_180_button = toga.Button('120 - 180 mins', on_press=self.lifestyle_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        e120_180_box = create_border(e120_180_button)

        e180_plus_button = toga.Button('More than 180 mins', on_press=self.lifestyle_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        e180_plus_box = create_border(e180_plus_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)
        
        header_box.add(exercise_label)

        for button in [e60_119_box, e60_box, e120_180_box,
                        e180_plus_box, back_box]:
            if button != back_box:
                main_box.add(button)
            else:
                footer_box.add(button)

        # add main_box to the main container
        main_container.add(header_box)
        main_container.add(main_box)
        main_container.add(footer_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def lifestyle_handler(self, widget):
        #add logic
        print("Exercise Handler ran!")
        # Access the label attribute of the button widget to get the user's selection
        self.exercise_selection = widget.text
        print(f"Sleep duration: {self.exercise_selection}")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)