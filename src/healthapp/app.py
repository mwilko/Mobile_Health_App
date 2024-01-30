"""
Health Application to detect chronic conditions with machine learning for decision making and pose detection
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER


class HealthApp(toga.App):

    def startup(self):
        # Create the main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        
        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))

        # logo image
        # logo_image_path = ""

        # title label
        title_label = toga.Label("Health Application", style=Pack(font_size=20, padding=(0, 10)))

        # start button
        start_button = toga.Button('Start', on_press=self.start_button_handler, style=Pack(padding=10))

        # add components to the main box
        main_box.add(title_label)
        main_box.add(start_button)

        # add main_box to the main container
        main_container.add(main_box)

        # Choice box for additional content
        choice_box = toga.Box(style=Pack(padding=20))

        # button for choices
        analyse_gait_button = toga.Button('Analyse Gait', on_press=self.analyse_gait_handler, style=Pack(padding=10))
        physical_button = toga.Button('Physical', on_press=self.physical_handler, style=Pack(padding=10))
        behavioural_button = toga.Button('Behavioural', on_press=self.behavioural_handler, style=Pack(padding=10))

        # add buttons to the choice box
        choice_box.add(analyse_gait_button)
        choice_box.add(physical_button)
        choice_box.add(behavioural_button)

        # add choice_box to the main container
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

        # Show the main window
        self.main_window.show()

    def analyse_gait_handler(self, widget):
        #add logic
        print("Analyse Gait button pressed!")

    def physical_handler(self, widget):
        #add logic
        print("Physical button pressed!")

    def behavioural_handler(self, widget):
        #add logic
        print("Behavioural button pressed!")

    def start_button_handler(self, widget):
        # add logic for start button
        print("Start button pressed!")

def main():
    return HealthApp()