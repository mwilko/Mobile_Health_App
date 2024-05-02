# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
# -------------------------------------------------------------------------------------------------------#


class PersonalDetails():
    def __init__(self, app: HealthApp):
        self.app = app
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:
        content = toga.Box(style=Pack(
            direction=COLUMN, background_color="#e0965e"))
        # Main box for the initial content
        header_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(20, 20, 0)))
        main_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5))

        # label for personal details
        header_label = toga.Label(
            "Age, Height, Weight and BMI: ", style=Pack(font_size=20, padding=(10, 5)))
        age_label = toga.Label("Age: ", style=Pack(
            color='black', font_size=15, padding=(0, 15)))
        height_label = toga.Label("Height: ", style=Pack(
            color='black', font_size=15, padding=(0, 15)))
        weight_label = toga.Label("Weight: ", style=Pack(
            color='black', font_size=15, padding=(0, 15)))
        bmi_label = toga.Label("BMI: ", style=Pack(
            color='black', font_size=15, padding=(0, 15)))

        # text input + button for physical analysis
        self.age_input = toga.TextInput(placeholder='Enter your age', style=Pack(
            color='black', background_color="#fbf5cc"), value=self.app.user.age)
        age_input_box = create_border(
            self.age_input, inner_color="#fbf5cc", padding=(2, 13, 0))

        self.height_input = toga.TextInput(placeholder='cm', style=Pack(
            color='black', background_color="#fbf5cc"), value=self.app.user.height)
        height_input_box = create_border(
            self.height_input, inner_color="#fbf5cc", padding=(2, 13, 0))

        self.weight_input = toga.TextInput(placeholder='kg', style=Pack(
            color='black', background_color="#fbf5cc"), value=self.app.user.weight)
        weight_input_box = create_border(
            self.weight_input, inner_color="#fbf5cc", padding=(2, 13, 0))
        # BMI -------------------------------------------------------------------------
        self.app.user.update_bmi()
        self.bmi_label = toga.Label(
            format(self.app.user.bmi), style=Pack(color='black'))
        bmi_box = create_border(
            self.bmi_label, inner_color="#fbf5cc", padding=(2, 13, 0))
        # ------------------------------------------------------------------------------

        submit_button = toga.Button('Submit', on_press=self.submit_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        submit_box = create_border(submit_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(
            color='black', background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        header_box.add(header_label)

        # add labels and respective buttons to the main box
        # Creates a space in background colour. ("Spacer")
        main_box.add(toga.Label(""))
        for TextInput in [age_input_box, height_input_box, weight_input_box]:
            # match the TextInput with the respective label
            if TextInput == age_input_box:
                main_box.add(age_label)
                main_box.add(TextInput)
                # Creates a space in background colour. ("Spacer")
                main_box.add(toga.Label(""))
            elif TextInput == height_input_box:
                main_box.add(height_label)
                main_box.add(TextInput)
                # Creates a space in background colour. ("Spacer")
                main_box.add(toga.Label(""))
            elif TextInput == weight_input_box:
                main_box.add(weight_label)
                main_box.add(TextInput)
                # Creates a space in background colour. ("Spacer")
                main_box.add(toga.Label(""))
            else:
                main_box.add(bmi_label)
                main_box.add(TextInput)
                # Creates a space in background colour. ("Spacer")
                main_box.add(toga.Label(""))

        # BMI------------------------------------
        main_box.add(bmi_label)
        main_box.add(bmi_box)
        # BMI------------------------------------

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
        # Access the value attribute of the TextInput widgets to get the user's input
        age = self.age_input.value
        if age == "":
            age = None
        else:
            if age.isnumeric() and int(age) > 0:
                age = int(age)
            else:
                self.app.main_window.error_dialog(
                    "Error!", "Invalid age input,\nPlease enter a valid age.")
                return
        height = self.height_input.value
        if height == "":
            height = None
        else:
            if height.isdecimal() and float(height) > 0:
                height = float(height)
            else:
                self.app.main_window.error_dialog(
                    "Error!", "Invalid height input,\nPlease enter a valid height.")
                return
        weight = self.weight_input.value
        if weight == "":
            weight = None
        else:
            if weight.isdecimal() and float(weight) > 0:
                weight = float(weight)
            else:
                self.app.main_window.error_dialog(
                    "Error!", "Invalid weight input,\nPlease enter a valid weight. (Use full numbers, no decimals)")
                return

        self.app.user.age = age
        self.app.user.height = height
        self.app.user.weight = weight
        self.app.user.update_bmi()
        self.app.user.save()

        # Update the BMI label
        self.bmi_label.text = format(self.app.user.bmi)
        self.app.main_window.info_dialog(
            "Success!", "Details saved! Your BMI has been updated.")

    def back_handler(self, widget):
        self.app.show_menu()
