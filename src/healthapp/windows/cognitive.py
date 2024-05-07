# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.app import HealthApp
from healthapp.style import create_border
# -------------------------------------------------------------------------------------------------------#


class Cognition():
    # Images would be imported into this class for the cognitive analysis, planning to add to the choice box
    # putting the image the user makes this decision based on inside of the 'choice_box'

    def __init__(self, app: HealthApp):
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(
            direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20))  # for label
        header_box
        main_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        # for submit + back buttons
        footer_box = toga.Box(style=Pack(padding=5))

        # button for behavioural analysis
        cognitive_score_label = toga.Label(
            f"Your Cognitive Score is Currently: {self.app.user.cognitive}", style=Pack(font_size=15, padding=(0, 10)))

        spelling_button = toga.Button('Spelling', on_press=self.spelling_handler, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        spelling_box = create_border(spelling_button, inner_color="#fbf5cc")

        memory_button = toga.Button('Memory', on_press=self.memory_handler, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        memory_box = create_border(memory_button, inner_color="#fbf5cc")

        maths_button = toga.Button('Maths', on_press=self.maths_handler, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        maths_box = create_border(maths_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        reset_score_button = toga.Button('Reset Score', on_press=self.reset_score_handler, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        reset_score_box = create_border(
            reset_score_button, inner_color="#fbf5cc")

        # add the label to the header box
        header_box.add(cognitive_score_label)

        main_box.add(toga.Label(""))
        for button in [spelling_box, memory_box, maths_box]:
            main_box.add(button)
        main_box.add(toga.Label(""))

        main_black_box.add(main_box)

        for button in [reset_score_box, back_box]:
            # add the reset score and back buttons to the footer_box
            footer_box.add(button)

        # add boxes to the main container
        for box in [header_box, main_black_box, footer_box]:
            main_container.add(box)

        # set the main container as the content of the main window
        self.app.update_content(main_container)

    def spelling_handler(self, widget):
        self.app.show_cognitive_spell()

    def memory_handler(self, widget):
        self.app.show_cognitive_memory()

    def maths_handler(self, widget):
        self.app.show_cognitive_math()

    def reset_score_handler(self, widget):
        self.app.user.cognitive = 0
        self.app.user.save()
        self.app.show_cognitive()

    def back_handler(self, widget):
        self.app.show_menu()
