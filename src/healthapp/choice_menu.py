import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border

# ChoiceMenu class for the choice menu
class ChoiceMenu:
    def __init__(self, main_window, app):
        # store app in a variable
        self.app = app
        self.main_window = main_window

        print("ChoiceMenu class running...")

        # Create the ml box as per prototype
        # ml results would be displayed inside of the box
        machine_learning_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        # Choice box for additional content
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20, background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Label for the choice menu
        name_label = toga.Label(f"Welcome, {self.app.user.first} {self.app.user.last}", style=Pack(font_size=12, padding=(5, 10)))
        ml_label = toga.Label("Machine Learning Algorithm has no data", style=Pack(font_size=15, padding=(0, 10)))

        machine_learning_box.add(name_label)
        machine_learning_box.add(ml_label)

        # button for choices
        analyse_gait_button = toga.Button('Analyse Gait', on_press=self.gait_analysis_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        gait_box = create_border(analyse_gait_button)

        personal_details_button = toga.Button('Personal Details', on_press=self.personal_details_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        pd_box = create_border(personal_details_button)

        sleep_button = toga.Button('Sleep', on_press=self.sleep_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        sleep_box = create_border(sleep_button)

        lifestyle_button = toga.Button('Lifestyle', on_press=self.lifestyle_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        lifestyle_box = create_border(lifestyle_button)

        cognition_button = toga.Button('Cognition', on_press=self.cognition_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        cognition_box = create_border(cognition_button)

        heart_rate_button = toga.Button('Heart Rate', on_press=self.heart_rate_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        heart_rate_box = create_border(heart_rate_button)

        nutrition_button = toga.Button('Nutrition', on_press=self.nutrition_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        nutrition_box = create_border(nutrition_button)

        main_box.add(toga.Label("")) # Creates a space in background colour. ("Spacer")
        for box in [gait_box, pd_box, sleep_box, lifestyle_box,
                     cognition_box, heart_rate_box, nutrition_box]:
            main_box.add(box)
        main_box.add(toga.Label("")) # Creates a space in background colour. ("Spacer")


        # add boxes to the main container
        main_container.add(machine_learning_box)
        main_container.add(main_box)


        # set the main container as the content of the main window
        self.app.update_content(main_container)
    
    # buttons to select the choice, takes the user to the respective page
    def gait_analysis_handler(self, widget):
        #add logic
        print("Gait Analysis button pressed!")
        AnalyseGait(self.app.main_window, self.app)

    def personal_details_handler(self, widget):
        print("Personal Details button pressed!")
        PersonalDetails(self.app.main_window, self.app) 

    def sleep_handler(self, widget):
        print("Sleep button pressed!")
        Sleep(self.app.main_window, self.app)

    def lifestyle_handler(self, widget):
        print("Lifestyle button pressed!")
        Lifestyle(self.app.main_window, self.app)

    def cognition_handler(self, widget):
        print("Cognition button pressed!")
        Cognition(self.app.main_window, self.app)

    def heart_rate_handler(self, widget):
        print("Heart Rate button pressed!")
        HeartRate(self.app.main_window, self.app)

    def nutrition_handler(self, widget):
        print("Nutrition button pressed!")
        Nutrition(self.app.main_window, self.app)

#-------------------------------------------------------------------------------------------------------#

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

#-------------------------------------------------------------------------------------------------------#

class PersonalDetails():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window 
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        footer_box = toga.Box(style=Pack(padding=20))

        # label for personal details
        age_label = toga.Label("Age: ", style=Pack(font_size=15, padding=(0, 10)))
        height_label = toga.Label("Height: ", style=Pack(font_size=15, padding=(0, 10)))
        weight_label = toga.Label("Weight: ", style=Pack(font_size=15, padding=(0, 10)))

        # text input + button for physical analysis
        self.age_input = toga.TextInput(placeholder='Enter your age')
        self.height_input = toga.TextInput(placeholder='cm')
        self.weight_input = toga.TextInput(placeholder='kg')

        submit_button = toga.Button('Submit', on_press=self.submit_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        submit_box = create_border(submit_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        # add labels and respective buttons to the main box
        for TextInput in [self.age_input, self.height_input, self.weight_input]:
            # match the TextInput with the respective label
            if TextInput == self.age_input:
                main_box.add(age_label)
                main_box.add(TextInput)
            elif TextInput == self.height_input:
                main_box.add(height_label)
                main_box.add(TextInput)
            else:
                main_box.add(weight_label)
                main_box.add(TextInput)

        # add buttons to the main box
        for button in [submit_box, back_box]:
            if button != back_box:
                main_box.add(button)
            else:
                footer_box.add(button)
        
        # add main_box to the main container
        main_container.add(main_box)
        main_container.add(footer_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def submit_handler(self, widget):
        #add logic
        print("Submit button pressed!")
        # Access the value attribute of the TextInput widgets to get the user's input
        age = self.age_input.value
        height = self.height_input.value
        weight = self.weight_input.value
        print(f"Age: {age}, Height: {height}, Weight: {weight}")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)

#-------------------------------------------------------------------------------------------------------#

class Sleep():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        footer_box = toga.Box(style=Pack(padding=20))

        # objects for behavioural analysis
        s_label = toga.Label("How many hours of sleep do you get per night?", style=Pack(font_size=15, padding=(0, 10)))
        self.s_text_input = toga.TextInput(placeholder='hours')

        submit_button = toga.Button('Submit', on_press=self.sleep_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        submit_box = create_border(submit_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        # for loop added incase of future expansion
        for label in [s_label]:
            if label == s_label:
                main_box.add(label)
                main_box.add(self.s_text_input)
            else:    
                print("Error: Object not found")

        # add buttons to the main box
        for button in [submit_box, back_box]:
            if button != back_box:
                main_box.add(button)
            else:
                footer_box.add(button)

        # add main_box to the main container
        main_container.add(main_box)
        main_container.add(footer_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def sleep_handler(self, widget):
        #add logic
        print("Lifestyle button pressed!")
        # Access the value attribute of the TextInput widget to get the user's input
        sleep_duration = self.s_text_input.value
        print(f"Sleep duration: {sleep_duration}")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)  

#-------------------------------------------------------------------------------------------------------#

class Lifestyle():
    def __init__(self, main_window, app):  # accept a main_window argument

        self.main_window = main_window
        self.app = app

        # Create an instance of variable to store the user's selection
        self.exercise_selection = None

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        footer_box = toga.Box(style=Pack(padding=20))

        # label + button for behavioural analysis
        exercise_label = toga.Label("How much exercise do you get per week?", style=Pack(font_size=15, padding=(0, 5)))
        e60_button = toga.Button('Less than 60 mins', on_press=self.lifestyle_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        e60_box = create_border(e60_button)

        e60_119_button = toga.Button('60 - 119 mins', on_press=self.lifestyle_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        e60_119_box = create_border(e60_119_button)

        e120_180_button = toga.Button('120 - 180 mins', on_press=self.lifestyle_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        e120_180_box = create_border(e120_180_button)

        e180_plus_button = toga.Button('More than 180 mins', on_press=self.lifestyle_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        e180_plus_box = create_border(e180_plus_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)
        
        header_box.add(exercise_label)

        for button in [e60_119_box, e60_box, e120_180_box,
                        e180_plus_box, back_box]:
            if button != back_box:
                main_box.add(button)
            else:
                footer_box.add(button)

        # add main_box to the main container
        main_container.add(header_box)
        main_container.add(main_box)
        main_container.add(footer_box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def lifestyle_handler(self, widget):
        #add logic
        print("Exercise Handler ran!")
        # Access the label attribute of the button widget to get the user's selection
        self.exercise_selection = widget.text
        print(f"Sleep duration: {self.exercise_selection}")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)

#-------------------------------------------------------------------------------------------------------#
        
class Cognition():
    # Images would be imported into this class for the cognitive analysis, planning to add to the choice box
    # putting the image the user makes this decision based on inside of the 'choice_box' 

    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20)) # for label
        main_box = toga.Box(style=Pack(padding=20)) # for cognitive choices
        choice_box = toga.Box(style=Pack(padding=20)) # for choice of the correct cognitive analysis
        footer_box = toga.Box(style=Pack(padding=20)) # for submit + back buttons

        # button for behavioural analysis
        c_label = toga.Label("Select the next image in the sequence: ", style=Pack(font_size=15, padding=(0, 10)))
        submit_button = toga.Button('Submit', on_press=self.c_class_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        submit_box = create_border(submit_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        for button in [submit_box, back_box]:
            if button != back_box or button != submit_box:
                choice_box.add(button) # add the choice image button to the choice_box
                                       # assuming thats how the cognitive analysis will be done
                
            else: # add the submit and back buttons to the footer_box
                footer_box.add(button) 

        # add boxes to the main container
        for box in [header_box, main_box, choice_box, footer_box]:
            main_container.add(box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def c_class_handler(self, widget):
        #add logic
        print("Cognitive button pressed!")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)

#-------------------------------------------------------------------------------------------------------#
        
class HeartRate():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box + choice box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        footer_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        hr_label1 = toga.Label("Feel your pulse until the timer reaches 0", style=Pack(font_size=15, padding=(0, 2)))
        hr_label2 = toga.Label("Record the beats per minute", style=Pack(font_size=15, padding=(0, 2)))
        self.hr_text_input = toga.TextInput(placeholder='BPM')

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        submit_button = toga.Button('Submit', on_press=self.hr_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        sumbit_box = create_border(submit_button)

        # formatting the layout
        for label in [hr_label1, hr_label2]:
            if label == hr_label1:
                header_box.add(label)
            else:
                main_box.add(label)
                main_box.add(self.hr_text_input)

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # NEED TO ADD TIMER FUNCTIONALITY
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                
        for button in [back_box, sumbit_box]:
            if button != back_box:
                main_box.add(button)
            else:
                footer_box.add(button)

        # add main_box to the main container
        for box in [header_box, main_box, footer_box]:
            main_container.add(box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def hr_handler(self, widget):
        #add logic
        print("Heart Rate button pressed!")

        heart_rate = self.hr_text_input.value
        print(f"Heart rate: {heart_rate}")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)

#-------------------------------------------------------------------------------------------------------#

class Nutrition():
    def __init__(self, main_window, app):  # accept a main_window argument
        self.main_window = main_window
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        footer_box = toga.Box(style=Pack(padding=20))

        # button for behavioural analysis
        n_label = toga.Label("Select the number of calories you consume per day: ", style=Pack(font_size=15, padding=(0, 10)))
        nless_1000_button = toga.Button('Less than 1000 calories', on_press=self.n_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        nless_1000_box = create_border(nless_1000_button)

        n1000_1499_button = toga.Button('1000 - 1500 calories', on_press=self.n_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        n1000_1499_box = create_border(n1000_1499_button)

        n1500_2000_button = toga.Button('1500 - 2000 calories', on_press=self.n_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        n1500_2000_box = create_border(n1500_2000_button)

        n2000_plus_button = toga.Button('More than 2000 calories', on_press=self.n_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        n2000_plus_box = create_border(n2000_plus_button)

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(padding=(-6, -4, -6, -4), background_color="#fbf5cc"))
        back_box = create_border(back_button)

        #formatting the layout
        header_box.add(n_label)

        for button in [nless_1000_box, n1000_1499_box, n1500_2000_box,
                        n2000_plus_box, back_box]:
            if button != back_box:
                main_box.add(button)
            else:
                footer_box.add(button)

        # add main_box to the main container
        for box in [header_box, main_box, footer_box]:
            main_container.add(box)

        # set the main container as the content of the main window
        self.main_window.content = main_container

    def n_handler(self, widget):
        #add logic
        print("Nutrition button pressed!")
        # Access the label attribute of the button widget to get the user's selection
        nutrition = widget.text
        print(f"Nutrition: {nutrition}")

    def back_handler(self, widget):
        print("Back button pressed!")
        # pass self as the app instance to the ChoiceMenu class
        from healthapp.choice_menu import ChoiceMenu
        ChoiceMenu(self.main_window, self.app)
