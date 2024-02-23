import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border

class HeartRate():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box + choice box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        footer_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        hr_label1 = toga.Label("Feel your pulse until the timer reaches 0", style=Pack(font_size=15, padding=(0, 2)))
        hr_label2 = toga.Label("Record the beats per minute", style=Pack(font_size=15, padding=(0, 2)))
        self.hr_text_input = toga.TextInput(placeholder='BPM')

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        submit_button = toga.Button('Submit', on_press=self.hr_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        sumbit_box = create_border(submit_button)

        # formatting the layout
        for label in [hr_label1, hr_label2]:
            if label == hr_label1:
                header_box.add(label)
            else:
                main_box.add(label)
                main_box.add(self.hr_text_input)

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # NEED TO ADD TIMER FUNCTIONALITY
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                
        for button in [back_box, sumbit_box]:
            if button != back_box:
                main_box.add(button)
            else:
                footer_box.add(button)

        # add main_box to the main container
        for box in [header_box, main_box, footer_box]:
            main_container.add(box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def hr_handler(self, widget):
        #add logic
        print("Heart Rate button pressed!")

        heart_rate = self.hr_text_input.value
        print(f"Heart rate: {heart_rate}")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)