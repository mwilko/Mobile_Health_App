#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.app import HealthApp
from healthapp.style import create_border

from healthapp.windows.choice_menu import ChoiceMenu as cm
#-------------------------------------------------------------------------------------------------------#

class CognitiveMath():
    print("CognitiveMath class")
    def __init__(self, app: HealthApp):  
        self.app = app
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        header_box = toga.Box(style=Pack(padding=20)) # for label
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5))

        cs_label = toga.Label("Select the correct equation: ", style=Pack(font_size=15, padding=(0, 10)))

        choice1_button = toga.Button('6x7 = 44', on_press=self.choice1_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        choice1_box = create_border(choice1_button, inner_color="#fbf5cc")

        choice2_button = toga.Button('5x12 = 55', on_press=self.choice2_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        choice2_box = create_border(choice2_button, inner_color="#fbf5cc")

        choice3_button = toga.Button('12x12 = 144', on_press=self.choice3_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        choice3_box = create_border(choice3_button, inner_color="#fbf5cc")

        submit_button = toga.Button('Submit', on_press=self.cs_class_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        submit_box = create_border(submit_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        header_box.add(cs_label)

        main_box.add(toga.Label(""))
        for button in [choice1_box, choice2_box, choice3_box]:
            main_box.add(button)
        main_box.add(toga.Label(""))

        main_black_box.add(main_box)

        for button in [submit_box, back_box]:
            footer_box.add(button)

        for box in [header_box, main_black_box, footer_box]:
            main_container.add(box)

        self.app.update_content(main_container)

    def choice1_handler(self, widget):
        print("Choice 1 button pressed! (Incorrect)")
        print(f"Cognitive Score: {cm.cognitive_score}")
        self.app.main_window.info_dialog("Incorrect Answer!", "You have answered incorrectly! \nYou have been returned to the Cognitive Test Menu.")
        self.app.show_cognitive()
    
    def choice2_handler(self, widget):
        print("Choice 2 button pressed! (Incorrect)")
        print(f"Cognitive Score: {cm.cognitive_score}")
        self.app.main_window.info_dialog("Incorrect Answer!", "You have answered incorrectly! \nYou have been returned to the Cognitive Test Menu.")
        self.app.show_cognitive()

    def choice3_handler(self, widget):
        print("Choice 3 button pressed! (Correct)")
        cm.increment_score()
        print(f"Cognitive Score: {cm.cognitive_score}")
        self.app.main_window.info_dialog("Correct Answer!", "You have answered correctly! \nYou have been returned to the Cognitive Test Menu.")
        self.app.show_cognitive()

    def cs_class_handler(self, widget):
        #add logic
        print("Submit button pressed!")

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_cognitive()