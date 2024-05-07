# -------------------------------------------------------------------------------------------------------#
import asyncio
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
# -------------------------------------------------------------------------------------------------------#


class HeartRate():
    def __init__(self, app: HealthApp):
        self.app = app
        self.timer = None
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:

        content = toga.Box(style=Pack(
            direction=COLUMN, background_color="#e0965e"))

        # Main box + choice box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5))

        # button for behavioural analysis
        hr_label1 = toga.Label("Feel your pulse until the timer reaches 0",
                               style=Pack(font_size=15, padding=(0, 2)))
        hr_label2 = toga.Label("Record the beats per minute",
                               style=Pack(font_size=15, padding=(0, 10)))

        self.hr_text_input = toga.TextInput(
            placeholder='BPM', style=Pack(background_color="#fbf5cc"), value=self.app.user.heart_rate)
        hr_text_input_box = create_border(
            self.hr_text_input, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        submit_button = toga.Button('Submit', on_press=self.submit_handler, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        sumbit_box = create_border(submit_button, inner_color="#fbf5cc")

        main_box.add(toga.Label(""))
        # formatting the layout
        for label in [hr_label1, hr_label2]:
            if label == hr_label1:
                header_box.add(label)
            else:
                main_box.add(label)
                main_box.add(hr_text_input_box)

        for button in [back_box, sumbit_box]:
            if button != back_box:
                main_box.add(button)
                main_box.add(toga.Label(""))
            else:
                footer_box.add(button)

        main_box.add(toga.Label(""))
        main_box.add(toga.Label(f"Timer: {self.timer if self.timer is not None else '60'}",
                                style=Pack(font_size=15, padding=(0, 10))))
        bar = toga.ProgressBar(style=Pack(padding=10, width=self.app.main_window.size[0] - 60), running=False, max=60, value=(self.timer or 60))
        main_box.add(bar)
        self.timer_button = toga.Button('Start Timer' if self.timer is None else 'Reset Timer', on_press=self.timer_toggle, style=Pack(
            background_color="#fbf5cc", padding=(-3)))
        self.timer_box = create_border(
            self.timer_button, inner_color="#fbf5cc")
        main_box.add(self.timer_box)
        main_box.add(toga.Label(""))

        main_black_box.add(main_box)

        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

    def timer_toggle(self, widget):
        # start background task
        if self.timer == None:
            self.app.loop.create_task(self.background_handler(self.app))
        else:
            self.timer = None
            self.app.update_content(self.get_content())

    async def background_handler(self, app, **kwargs):
        self.timer = 61
        while self.timer is not None and self.timer > 0:
            self.timer -= 1
            self.app.update_content(self.get_content())
            await asyncio.sleep(1)

        if self.timer == 0:
            self.timer = None
            self.app.main_window.error_dialog("Time's up!", "Please submit your heart rate.")
            self.app.update_content(self.get_content())

    def submit_handler(self, widget):
        heart_rate = self.hr_text_input.value
        if heart_rate is None:  # Check for empty input
            self.app.main_window.error_dialog(
                'Error', 'Please enter a valid heart rate')
            return
        if not heart_rate.isdigit():  # Check for non-numeric input
            self.app.main_window.error_dialog(
                'Error', 'Please enter a valid heart rate')
            return
        if int(heart_rate) <= 0:  # Check for heart rate below 0
            self.app.main_window.error_dialog(
                'Error', 'Please enter a valid heart rate')
            return
        if int(heart_rate) > 200:  # Check for heart rate above 200
            self.app.main_window.error_dialog(
                'Error', 'Please enter a valid heart rate')
            return
        self.app.user.heart_rate = heart_rate
        self.app.user.save()
        self.app.main_window.info_dialog(
            'Success', 'Heart rate saved successfully')

    def back_handler(self, widget):
        self.timer = None
        self.app.show_menu()
