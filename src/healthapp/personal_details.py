#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
#-------------------------------------------------------------------------------------------------------#

class PersonalDetails():
    def __init__(self, main_window, app: HealthApp):  # accept a main_window argument
        self.main_window = main_window 
        self.app = app
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:

        content = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))
        # Main box for the initial content
        header_box = toga.Box(style=Pack(direction=COLUMN, padding=(20, 20, 0)))
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=20))

        # label for personal details
        header_label = toga.Label("Age, Height and Weight: ", style=Pack(font_size=20, padding=(5, 10)))
        age_label = toga.Label("Age: ", style=Pack(font_size=15, padding=(0, 10)))
        height_label = toga.Label("Height: ", style=Pack(font_size=15, padding=(0, 10)))
        weight_label = toga.Label("Weight: ", style=Pack(font_size=15, padding=(0, 10)))

        # text input + button for physical analysis
        self.age_input = toga.TextInput(placeholder='Enter your age')
        age_input_box = create_border(self.age_input)

        self.height_input = toga.TextInput(placeholder='cm')
        height_input_box = create_border(self.height_input)

        self.weight_input = toga.TextInput(placeholder='kg')
        weight_input_box = create_border(self.weight_input)

        submit_button = toga.Button('Submit', on_press=self.submit_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        submit_box = create_border(submit_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        header_box.add(header_label)

        # add labels and respective buttons to the main box
        main_box.add(toga.Label("")) # Creates a space in background colour. ("Spacer")
        for TextInput in [age_input_box, height_input_box, weight_input_box]:
            # match the TextInput with the respective label
            if TextInput == age_input_box:
                main_box.add(age_label)
                main_box.add(TextInput)
            elif TextInput == height_input_box:
                main_box.add(height_label)
                main_box.add(TextInput)
            else:
                main_box.add(weight_label)
                main_box.add(TextInput)

        # add buttons to the main box
        for button in [submit_box, back_box]:
            if button != back_box:
                main_box.add(button)
                main_box.add(toga.Label(""))
            else:
                footer_box.add(button)


        main_black_box.add(main_box)
        
        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

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