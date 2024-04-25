# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
# -------------------------------------------------------------------------------------------------------#


class Smoker():
    def __init__(self, app: HealthApp):
        self.app = app
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:
        content = toga.Box(style=Pack(
            direction=COLUMN, background_color="#e0965e"))
        # Create an instance of variable to store the user's selection
        self.exercise_selection = None

        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5))

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        # label + button for smoking
        smoker_label = toga.Label("Do you smoke?", style=Pack(
            color='black', font_size=15, padding=(0, 5)))

        yessmoke_button = toga.Button('Yes', on_press=self.smoker_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        yessmoke_box = create_border(yessmoke_button, inner_color="#fbf5cc")

        nosmoke_button = toga.Button('No', on_press=self.smoker_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        nosmoke_box = create_border(nosmoke_button, inner_color="#fbf5cc")

        # adding labels to page
        header_box.add(smoker_label)

        main_box.add(toga.Label(""))
        for button in [yessmoke_box, nosmoke_box, back_box]:
            if button != back_box:
                main_box.add(button)
                main_box.add(toga.Label(""))
            else:
                footer_box.add(button)

        main_black_box.add(main_box)

        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

      #   # Smoker labels
      #   main_box.add(toga.Label(""))
      #   main_box.add(smoker_label)
      #   main_box.add(yessmoke_box)
      #   main_box.add(nosmoke_box)
      #   main_box.add(toga.Label(""))

    def smoker_handler(self, widget):
        # Update the high blood pressure variable based on the user's selection
        if widget.text == 'Yes':
            self.app.user.smoker = 1
        elif widget.text == 'No':
            self.app.user.smoker = 0
        print(f"Smoker: {self.app.user.smoker}")

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_lifestyle()
