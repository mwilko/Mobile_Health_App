# -------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW

from healthapp.app import HealthApp
from healthapp.style import create_border

from healthapp.windows.choice_menu import ChoiceMenu as cm
import random
import math
# -------------------------------------------------------------------------------------------------------#


class CognitiveMemory():
    print("CognitiveMemory class")

    def __init__(self, app: HealthApp):
        self.app = app
        self.selected_tiles = []
        self.board = []
        self.status_label = None
        self.game_board = []
        self.tile_button = toga.Button('?', on_press=self.tile_clicked, style=Pack(width=50, height=50, padding=5))
        
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
        self.back_box = create_border(back_button, inner_color="#fbf5cc")

        header_box.add(self.memory_label)
        
        main_box.add(toga.Label(""))
        main_box.add(play_box)
        main_box.add(toga.Label(""))
        
        main_black_box.add(main_box)
        
        for button in [self.back_box]:
            footer_box.add(button)

        for box in [header_box, main_black_box, footer_box]:
            main_container.add(box)

        self.app.update_content(main_container)

    def play_game(self, widget):
        # game setup
        tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        print("Tiles before generating board:", tiles)
        self.board = self.generate_board(tiles)
        print("board:", self.board)
        
        self.game_board, self.status_label = self.create_board_ui(self.board, self.selected_tiles)
        
        # add components to the main box
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))
        main_box.add(self.game_board)
        main_box.add(self.status_label)
        
        self.app.update_content(main_box)

    
    def update_ui(self, index1, index2):
        button_container = self.game_board.children[index1 // 4]  # Get the row container
        button = button_container.children[index1 % 4]  # Get the button within the row
        button.label = self.board[index1]  # Update the button's label
        
        button_container = self.game_board.children[index2 // 4]  # Get the row container
        button = button_container.children[index2 % 4]  # Get the button within the row
        button.label = self.board[index2]  # Update the button's label

    def generate_board(self, tiles):
        board = tiles * 2 # creates pairs of tiles
        random.shuffle(board)
        print("Board length:", len(board))
        return board
    
    def create_board_ui(self, board, selected_tiles):
        # calculate the number of rows and columns
        rows = int(math.sqrt(len(board)))
        cols = rows

        # create a grid layout for the game board
        game_board = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))
        for i in range(rows):
            row = toga.Box(style=Pack(direction=ROW, alignment=CENTER))
            for j in range(cols):
                index = i * cols + j
                if index < len(board):
                    tile_button = toga.Button('?', on_press=self.tile_clicked, style=Pack(width=50, height=50, padding=5))
                    tile_button.tile_index = index # store the tile index
                    row.add(tile_button)
            game_board.add(row)
            
        # status label to display feedback
        status_label = toga.Label('Memory Game', style=Pack(padding=10))
        return game_board, status_label
    
    def tile_clicked(self, widget):
        index = widget.tile_index
        print("Clicked index:", index)
        print("clicked: ", self.board[index])
        if index not in self.selected_tiles:
            widget.label = self.board[index]
            self.selected_tiles.append(index)
            self.check_tiles()
            
    def check_tiles(self):
        if len(self.selected_tiles) == 2:
            index1, index2 = self.selected_tiles
            if self.board[index1] == self.board[index2]:
                self.game_board.children[index1 // 4].children[index1 % 4].label = self.board[index1]
                self.game_board.children[index2 // 4].children[index2 % 4].label = self.board[index2]
                self.status_label.text = 'Match!'
                self.update_ui(index1,index2)
                # Remove matched tiles from the selected_tiles list
                self.selected_tiles = []
            else:
                self.status_label.text = 'Try again!'
                self.reset_tiles()
        if len(self.selected_tiles) == 16:
            self.status_label.text = 'Congratulations! You won!'
            
    def reset_tiles(self):
        for index in self.selected_tiles:
            self.game_board.children[index // 4].children[index % 4].label = '?'
        self.selected_tiles = []
        

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_cognitive()
