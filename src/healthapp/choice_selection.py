import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class ChoiceMenu(toga.App):
    def startup(self):
        choice_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        #button for choices
        analyse_gait_button = toga.Button('Analyse Gait', on_press=self.analyse_gait_button_handler, style=Pack(padding=10))
        physical_button = toga.Button('Physical', on_press=self.physical_button_handler, style=Pack(padding=10))
        behavioural_button = toga.Button('Behavioural', on_press=self.behavioural_button_handler, style=Pack(padding=10))

        #add buttons to the choice box
        choice_box.add(analyse_gait_button)
        choice_box.add(physical_button)
        choice_box.add(behavioural_button)

        #choices box as the main content for the file
        self.main_window.content = choice_box

    def analyse_gait_handler(self, widget):
        #add logic
        print("Analyse Gait button pressed!")

    def physical_handler(self, widget):
        #add logic
        print("Physical button pressed!")

    def behavioural_handler(self, widget):
        #add logic
        print("Behavioural button pressed!")