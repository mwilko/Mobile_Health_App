#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.app import HealthApp
from healthapp.style import create_border
#-------------------------------------------------------------------------------------------------------#

class Cognition():
    # Images would be imported into this class for the cognitive analysis, planning to add to the choice box
    # putting the image the user makes this decision based on inside of the 'choice_box' 

    def __init__(self, app: HealthApp):  
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20)) # for label
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5)) # for submit + back buttons

        # button for behavioural analysis
        c_label = toga.Label("Select your cognitive test: ", style=Pack(font_size=15, padding=(0, 10)))

        spelling_button = toga.Button('Spelling', on_press=self.spelling_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        spelling_box = create_border(spelling_button, inner_color="#fbf5cc")

        memory_button = toga.Button('Memory', on_press=self.memory_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        memory_box = create_border(memory_button, inner_color="#fbf5cc")

        maths_button = toga.Button('Maths', on_press=self.maths_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        maths_box = create_border(maths_button, inner_color="#fbf5cc")

        submit_button = toga.Button('Submit', on_press=self.c_class_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        submit_box = create_border(submit_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        # add the label to the header box
        header_box.add(c_label)

        main_box.add(toga.Label(""))
        for button in [spelling_box, memory_box, maths_box]:
            main_box.add(button)
        main_box.add(toga.Label(""))

        main_black_box.add(main_box)

        for button in [submit_box, back_box]:
            # add the submit and back buttons to the footer_box
            footer_box.add(button) 

        # add boxes to the main container
        for box in [header_box, main_black_box, footer_box]:
            main_container.add(box)

        # set the main container as the content of the main window
        self.app.update_content(main_container)

    def spelling_handler(self, widget):
        #add logic
        print("Spelling button pressed!")
        self.app.show_cognitive_spell()

    def memory_handler(self, widget):
        #add logic
        print("Memory button pressed!")
        self.app.show_cognitive_memory()

    def maths_handler(self, widget):
        #add logic
        print("Maths button pressed!")
        self.app.show_cognitive_math()

    def c_class_handler(self, widget):
        #add logic
        print("Submit button pressed!")

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_menu()