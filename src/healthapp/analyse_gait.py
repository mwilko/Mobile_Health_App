import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border


class AnalyseGait():
    def __init__(self, main_window, app):
        self.app = app 
        self.main_window = main_window

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(padding=20))

        # Choice box for additional content
        choice_box = toga.Box(style=Pack(padding=20))
    
        # button for gait analysis
        analyse_gait_button = toga.Button('Analyse Gait', on_press=self.analyse_gait_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        analyse_gait_box = create_border(analyse_gait_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        main_box.add(analyse_gait_box)
        main_box.add(back_box)

        # add choice_box to the main container
        main_container.add(main_box)
        main_container.add(choice_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    async def analyse_gait_handler(self, widget):
        print("Analyse Gait button pressed!")

        # Check the versions of the libraries (error testing)
        #print("TensorFlow version:", tf.__version__)
        #print("OpenCV version:", cv2.__version__)
        #print("TQDM version:", tqdm.__version__)
        #print("Keras package:", keras.__package__)
        #print("TensorFlow Hub version:", hub.__version__)
        
        # Here to make sure numpy gets added (think of it as a little test)
        #n = np.array([1,2,3])
        #print(n)

        # Note this doesnt return on iOS/macOS yet, fully working on android.
        if await self.app.camera.request_permission():
            photo = await self.app.camera.take_photo()
            if photo is None:
                # User cancelled.
                return
            file = str(self.app.paths.data) + "/picture.png"
            photo.save(file)
            self.main_window.info_dialog("Success!", "Photo has been saved to: " + file)
        else:
            self.main_window.info_dialog("Oh no!", "You have not granted permission to take photos")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)