#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.app import HealthApp
from healthapp.style import create_border

from healthapp.windows.choice_menu import ChoiceMenu as cm

import random
import os
#-------------------------------------------------------------------------------------------------------#
class CognitiveSpell():
    def __init__(self, app: HealthApp):  
        self.app = app
        self.end = False
        self.question_number = 0
        self.correct_answers = 0
        self.max_questions = 10
        # load questions from file
        filename = os.path.join(os.path.dirname(__file__), '..', 'resources', 'questions.txt')
        self.questions = self.load_questions(filename)
        self.choice1_button = toga.Button('', on_press=self.choice_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        self.choice2_button = toga.Button('', on_press=self.choice_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        self.choice3_button = toga.Button('', on_press=self.choice_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        #load first question and set up ui
        self.load_new_question()
        self.setup_ui()

    def load_questions(self, filename):
        # load questions from text file
        try:
            with open(filename, 'r') as file:
                questions = [line.strip().split(",") for line in file.readlines()]
                return questions
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []
        
    def load_new_question(self):
        # load a new question
        if self.question_number < self.max_questions:
            self.question_number += 1
            # if there are questions remaining
            if self.questions:
                # choose a random question from the list and remove to avoid repeats
                self.current_question = random.choice(self.questions)
                self.questions.remove(self.current_question) # remove the chosen question so it cannot be chosen again
                self.correct_spelling = self.current_question[3] # fourth word is the correct one
                self.update_question_ui()
            else:
                self.end_game()
        else:
            self.end_game()
            
    def update_question_ui(self):
        # update ui with current question and choices
        self.choice1_button = toga.Button(f'{self.current_question[0]}', on_press=self.choice_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        self.choice2_button = toga.Button(f'{self.current_question[1]}', on_press=self.choice_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        self.choice3_button = toga.Button(f'{self.current_question[2]}', on_press=self.choice_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))

    def choice_handler(self, widget):
        selected_spelling = widget.text
        # if the game has not ended
        if not self.end:
            if selected_spelling == self.correct_spelling:
                self.correct_answers += 1
                cm.increment_score()
            self.load_new_question()
            self.setup_ui()
        
    def end_game(self):
        self.end = True
        self.app.main_window.info_dialog(f"You have answered {self.correct_answers} spellings correctly!", "\nYou have been returned to the Cognitive Test Menu.")
        self.app.show_cognitive()
        
    def setup_ui(self):
        # setup user interface
        if not self.end:
            container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))
            header_box = toga.Box(style=Pack(padding=20))
            main_box = toga.Box(style=Pack(direction=COLUMN, padding=(2,2), background_color="#fbf5cc"))
            main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0,18,18), background_color="black"))
            footer_box = toga.Box(style=Pack(padding=5))    
        
            cs_label = toga.Label("Spell the word correctly: ", style=Pack(font_size=15, padding=(0,10)))

            back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
            back_box = create_border(back_button, inner_color="#fbf5cc")
        
            header_box.add(cs_label)
            main_box.add(toga.Label(""))
            for button in [self.choice1_button, self.choice2_button, self.choice3_button]:
                main_box.add(create_border(button, inner_color="#fbf5cc"))
            main_box.add(toga.Label(""))

            main_black_box.add(main_box)
            for button in [back_box]:
                footer_box.add(button)
            for box in [header_box, main_black_box, footer_box]:
                container.add(box)

            self.app.update_content(container)

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_cognitive()