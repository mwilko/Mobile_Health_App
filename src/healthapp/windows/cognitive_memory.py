# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW

from healthapp.app import HealthApp
from healthapp.style import create_border

from healthapp.windows.choice_menu import ChoiceMenu as cm
import random
import math
import asyncio
# -------------------------------------------------------------------------------------------------------#


class CognitiveMemory():
    print("CognitiveMemory class")

    def __init__(self, app: HealthApp):
        self.app = app
        self.selected_tiles = []
        self.end_selected = []
        self.board = []
        self.status_label = None
        self.game_board = []
        # initialise the tile button with a question mark
        self.tile_button = toga.Button('?', on_press=self.tile_clicked, style=Pack(width=50, height=50, padding=5))
        self.status_label = toga.Label('', style=Pack(background_color="#e0965e", padding=10))
        self.tries = 0
        
        # create main container box and other boxes
        main_container = toga.Box(style=Pack(
            direction=COLUMN, background_color="#e0965e"))

        header_box = toga.Box(style=Pack(padding=20))  # for label
        main_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(
            direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5))

        self.memory_label = toga.Label("Memory Game", style=Pack(font_size=15, padding=(0, 10)))
       
        play_button = toga.Button('Play Memory Game', on_press=self.play_game, style=Pack(background_color="#fbf5cc", padding=(-3)))
        play_box = create_border(play_button, inner_color="#fbf5cc")
        
        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        header_box.add(self.memory_label)
        
        main_box.add(toga.Label(""))
        main_box.add(play_box)
        main_box.add(toga.Label(""))
        
        main_black_box.add(main_box)
        
        for button in [back_box]:
            footer_box.add(button)

        for box in [header_box, main_black_box, footer_box]:
            main_container.add(box)

        # update the app content with the main container
        self.app.update_content(main_container)

    async def play_game(self, widget):
        # game setup - generate a new board and update the ui
        tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.board = self.generate_board(tiles)
        
        # shows the full board before hiding it after 5 seconds
        self.update_ui(show_full_board=True)
        await asyncio.sleep(5)
        self.update_ui()
    
    def update_ui(self, show_full_board=False):
        # update the ui with the game board and status label
        main_container = toga.Box(style=Pack(
            direction=COLUMN, background_color="#e0965e"))
        header_box = toga.Box(style=Pack(padding=20))
        footer_box = toga.Box(style=Pack(padding=5))
        
        exit_button = toga.Button('Exit', on_press=self.back_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        exit_box = create_border(exit_button, inner_color="#fbf5cc")
        if show_full_board:
            self.game_board = self.create_board_ui(self.board, show_full_board=True)
        else:
            self.game_board = self.create_board_ui(self.board)
        
        # add components to the main box
        main_box = toga.Box(style=Pack(background_color="#e0965e", direction=COLUMN, alignment=CENTER))
        main_box.add(self.game_board)
        main_box.add(self.status_label)
       
        for button in [exit_box]:
            footer_box.add(button)        

        for box in [header_box, main_box, footer_box]:
            main_container.add(box)
        
        # update the app content with the main container
        self.app.update_content(main_container)

    def generate_board(self, tiles):
        # generate a new game board by shuffling the tiles
        board = tiles * 2 # creates pairs of tiles
        random.shuffle(board)
        return board
    
    def create_board_ui(self, board, show_full_board=False):
        # calculate the number of rows and columns
        rows = int(math.sqrt(len(board)))
        cols = rows

        # create a grid layout for the game board
        game_board = toga.Box(style=Pack(background_color="#e0965e", direction=COLUMN, alignment=CENTER))
        if show_full_board:
            for i in range(rows):
                row = toga.Box(style=Pack(direction=ROW, alignment=CENTER))
                for j in range(cols):
                    index = i * cols + j
                    if index < len(board):
                        tile_button = toga.Button(f'{board[index]}', style=Pack(background_color="#fbf5cc", width=50, height=50, padding=5))
                        row.add(tile_button)
                game_board.add(row)
        else:
            for i in range(rows):
                row = toga.Box(style=Pack(direction=ROW, alignment=CENTER))
                for j in range(cols):
                    index = i * cols + j
                    if index < len(board):
                        if index in self.end_selected:
                            tile_button = toga.Button(f'{board[index]}', style=Pack(background_color="#fbf5cc", width=50, height=50, padding=5))
                        else:
                            tile_button = toga.Button('?', on_press=self.tile_clicked, style=Pack(background_color="#fbf5cc", width=50, height=50, padding=5))
                            tile_button.tile_index = index # store the tile index
                        row.add(tile_button)
                game_board.add(row)
        
        return game_board
    
    def tile_clicked(self, widget):
        # handle the tile click event
        index = widget.tile_index
        if index not in self.selected_tiles:
            widget.label = self.board[index]
            self.selected_tiles.append(index)
            self.check_tiles()
            
    def check_tiles(self):
        # check if two tiles are selected and compare them
        if len(self.selected_tiles) == 2:
            index1, index2 = self.selected_tiles
            if self.board[index1] == self.board[index2]:
                # if the tiles match, update ui, increment score and reset selected tiles
                self.game_board.children[index1 // 4].children[index1 % 4].label = self.board[index1]
                self.game_board.children[index2 // 4].children[index2 % 4].label = self.board[index2]
                self.status_label.text = 'Match!'
                self.end_selected.append(index1)
                self.end_selected.append(index2)
                self.update_ui()
                # Remove matched tiles from the selected_tiles list
                self.selected_tiles = []
            else:
                # if tiles don't match, increment tries, reset tiles and update ui
                self.status_label.text = 'Try again!'
                self.tries += 1
                self.reset_tiles()
                self.update_ui()
        if len(self.end_selected) == 16:
            # if all the tiles are matched, end the game
            self.status_label.text = 'Congratulations! You won!'
            self.end_game()
            
    def reset_tiles(self):
        # reset the selected and matched tiles
        for index in self.selected_tiles:
            self.game_board.children[index // 4].children[index % 4].label = '?'
        self.selected_tiles = []
        self.end_selected = []
        
    def end_game(self):
        # calculate the score based on tries and end game message
        score = 20 - (self.tries // 2)
        if score > 0 and score <= 10:
            for i in range(score):
                self.app.user.cognitive += 1
                self.app.user.save()
        # if the score is bigger than 10 - cognitive score will be 10
        elif score > 10:
            for i in range(10):
                self.app.user.cognitive += 1
                self.app.user.save()
        self.app.main_window.info_dialog("Congratulations!", f"You gained {score} points! \nYou have been returned to the Cognitive Test Menu.")
        self.app.show_cognitive()

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_cognitive()