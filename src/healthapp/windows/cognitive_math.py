#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.app import HealthApp
from healthapp.style import create_border

from healthapp.windows.choice_menu import ChoiceMenu as cm
import random
#-------------------------------------------------------------------------------------------------------#

class CognitiveMath():
    def __init__(self, app: HealthApp):  
        self.app = app
        self.end = False
        self.question_number = 0
        self.correct_answers = 0
        self.max_questions = 10
        self.current_question = ""
        self.correct_answer = None
        self.answer_input = None
        self.divide = False # flag to indicate if current question involves division
        # load first question and set up ui
        self.load_new_question()
        self.setup_ui()

    def generate_question(self):
        # generate random arithmetic question
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        operator = random.choice(['+', '-', '*', '/'])

        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        elif operator == '*':
            answer = num1 * num2
        elif operator == '/':
            # if division, set the divide flag
            self.divide = True
            answer = num1 / num2
         
        question_text = f"{num1} {operator} {num2} = ?"
        return question_text, answer
    
    def load_new_question(self):
        # load new question if max number of questions has not been reached
        if self.question_number < self.max_questions:
            self.question_number += 1
            self.current_question, self.correct_answer = self.generate_question()
            self.setup_ui()
        else:
            self.end_game()
            
    def choice_handler(self, widget):
        # handle user's input
        if not self.end:
            user_answer = self.answer_input.value.strip()
            try:
                # round user answer to 3 significant figures
                user_answer = round(float(user_answer), 3)
                correct_rounded = round(self.correct_answer, 3)
                if user_answer == correct_rounded:
                    self.correct_answers += 1
                    cm.cognitive_score += 1
            except ValueError:
                pass

        self.load_new_question()

            
    def end_game(self):
        # end the game
        self.end = True
        self.app.main_window.info_dialog(f"You have answered {self.correct_answers} questions correctly!", "\nYou have been returned to the Cognitive Test Menu.")
        self.app.show_cognitive()
        
    def setup_ui(self):
        # set up user interface for displaying questions and receiving answers
        if not self.end:
            container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))
            header_box = toga.Box(style=Pack(padding=20))
            main_box = toga.Box(style=Pack(direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
            main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
            footer_box = toga.Box(style=Pack(padding=5))
            
            question_label = toga.Label(self.current_question, style=Pack(font_size=15, padding=(0, 10)))
            self.answer_input = toga.TextInput(style=Pack(padding=(0, 10)))

            submit_button = toga.Button('Submit', on_press=self.choice_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
            submit_box = create_border(submit_button, inner_color="#fbf5cc")
            back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
            back_box = create_border(back_button, inner_color="#fbf5cc")

            if self.divide:
                # add a label indicating to round to 3 s.f. for division
                divide_label = toga.Label("(round to 3 significant figures)", style=Pack(font_size=10, padding=(0, 10)))
                header_box.add(question_label)
                header_box.add(divide_label)
                self.divide = False # reset the divide flag
            else:
                header_box.add(question_label)
            main_box.add(self.answer_input)
            main_black_box.add(main_box)

            for button in [submit_box, back_box]:
                footer_box.add(button)

            for box in [header_box, main_black_box, footer_box]:
                container.add(box)

            self.app.update_content(container)

    def back_handler(self, widget):
        self.app.show_cognitive()