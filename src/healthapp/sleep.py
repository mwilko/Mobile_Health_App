import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border

class Sleep():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        footer_box = toga.Box(style=Pack(padding=20))

        # objects for behavioural analysis
        s_label = toga.Label("How many hours of sleep do you get per night?", style=Pack(font_size=15, padding=(0, 10)))
        self.s_text_input = toga.TextInput(placeholder='hours')

        submit_button = toga.Button('Submit', on_press=self.sleep_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        submit_box = create_border(submit_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        # for loop added incase of future expansion
        for label in [s_label]:
            if label == s_label:
                main_box.add(label)
                main_box.add(self.s_text_input)
            else:    
                print("Error: Object not found")

        # add buttons to the main box
        for button in [submit_box, back_box]:
            if button != back_box:
                main_box.add(button)
            else:
                footer_box.add(button)

        # add main_box to the main container
        main_container.add(main_box)
        main_container.add(footer_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def sleep_handler(self, widget):
        #add logic
        print("Lifestyle button pressed!")
        # Access the value attribute of the TextInput widget to get the user's input
        sleep_duration = self.s_text_input.value
        print(f"Sleep duration: {sleep_duration}")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app) 