# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
# -------------------------------------------------------------------------------------------------------#


class Stroke():
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

        # label + button for behavioural analysis

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        # label + button for stroke
        stroke_label = toga.Label("Have you had a stroke?", style=Pack(
            color='black', font_size=15, padding=(0, 5)))

        yesstroke_button = toga.Button('Yes', on_press=self.stroke_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        yesstroke_box = create_border(yesstroke_button, inner_color="#fbf5cc")

        nostroke_button = toga.Button('No', on_press=self.stroke_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        nostroke_box = create_border(nostroke_button, inner_color="#fbf5cc")

        # adding labels to page
        header_box.add(stroke_label)

        main_box.add(toga.Label(""))
        for button in [yesstroke_box, nostroke_box, back_box]:
            if button != back_box:
                main_box.add(button)
                main_box.add(toga.Label(""))
            else:
                footer_box.add(button)

        main_black_box.add(main_box)

        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

      #   # Stroke labels
      #   main_box.add(toga.Label(""))
      #   main_box.add(stroke_label)
      #   main_box.add(yesstroke_box)
      #   main_box.add(nostroke_box)
      #   main_box.add(toga.Label(""))

    def stroke_handler(self, widget):
        # Update the stroke variable based on the user's selection
        self.app.user.stroke = (1 if widget.text == 'Yes' else 0)
        self.app.user.save()

    def back_handler(self, widget):
        self.app.show_lifestyle()
