import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border

class PersonalDetails():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window 
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        footer_box = toga.Box(style=Pack(padding=20))

        # label for personal details
        age_label = toga.Label("Age: ", style=Pack(font_size=15, padding=(0, 10)))
        height_label = toga.Label("Height: ", style=Pack(font_size=15, padding=(0, 10)))
        weight_label = toga.Label("Weight: ", style=Pack(font_size=15, padding=(0, 10)))

        # text input + button for physical analysis
        self.age_input = toga.TextInput(placeholder='Enter your age')
        self.height_input = toga.TextInput(placeholder='cm')
        self.weight_input = toga.TextInput(placeholder='kg')

        submit_button = toga.Button('Submit', on_press=self.submit_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        submit_box = create_border(submit_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        # add labels and respective buttons to the main box
        for TextInput in [self.age_input, self.height_input, self.weight_input]:
            # match the TextInput with the respective label
            if TextInput == self.age_input:
                main_box.add(age_label)
                main_box.add(TextInput)
            elif TextInput == self.height_input:
                main_box.add(height_label)
                main_box.add(TextInput)
            else:
                main_box.add(weight_label)
                main_box.add(TextInput)

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

    def submit_handler(self, widget):
        #add logic
        print("Submit button pressed!")
        # Access the value attribute of the TextInput widgets to get the user's input
        age = self.age_input.value
        height = self.height_input.value
        weight = self.weight_input.value
        print(f"Age: {age}, Height: {height}, Weight: {weight}")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)