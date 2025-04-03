import tkinter as tk
import random # importing necessary modules
import logging
from datetime import datetime

logging.basicConfig( # set up settings for logging, writing game results in file
    filename="battleship_results.log", # creating file
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S" # set up time
)

class Board: # creating class Board which include information ship placing, ship hitting, and ship sunking
    def __init__(self, size=10):
        self.size = size # Field size
        self.grid = [[" "] * size for _ in range(size)] # creating empty field

    def place_ship(self, ship): # method placing ship in field
        for x,y in ship.coords:
            self.grid[y][x] = ship.symbol # set the ship symbol to the coordinates on the field

    def hit(self, x, y): # methods for hand
        if self.grid[y][x] == " ": # checking hit from coordinates
            self.grid[y][x] = "."
            return False
        elif self.grid[y][x] in {".", "X"}: # checking for hitting in coordinates
            return False
        else:
            self.grid[y][x] = "X" # checking hit
            return True

    def all_ships_sunk(self): # checking all ships hitted or no
        return all(cell in {"X", " ", "."} for row in self.grid for cell in row)

class Ship: #creating Ship class
    def __init__(self, size, symbol):
        self.size = size # ship size
        self.symbol = symbol # symbol ship in the field
        self.coords = [] # coordinates ship in field

    def no_adjacent_ships(self, x, y, board): # check if there are other ships near the placed ship vertically and horizontally
        # checking no neighboring ships around the cell
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < board.size and 0 <= ny < board.size:
                    if board.grid[ny][nx] != " ":  # if cell busy with another ship
                        return False
        return True

    def generate_coords(self, board): # generating random coordinates for placing ship
        while True:
            x = random.randint(0, 9) # random coords for x
            y = random.randint (0, 9) # random coords for y
            direction = random.choice(["horizontal", "vertical"]) # direction horizontal or vertical
            if direction == "horizontal" and x + self.size <= board.size:
                coords = [(x + i, y) for i in range(self.size)] # horizontal coords
            elif direction == "vertical" and y + self.size <= board.size:
                coords = [(x, y + i) for i in range(self.size)] # vertical coords
            else:
                continue

            if all(board.grid[y][x] == " " and self.no_adjacent_ships(x, y, board) for x, y in coords):
                self.coords = coords  # saving ship coords
                break

class Player: #create class Player which included information about ship size for player and computer
    def __init__(self, name):
        self.name = name # player name
        self.board = Board() # creating field for player
        # creating a list of ships(different size and symbol)
        self.ships = [Ship(5, "A"), Ship(4, "B"), Ship(3, "C"), Ship(3, "D"), Ship(2, "E")]
        for ship in self.ships:
            ship.generate_coords(self.board) #generate ship coords
            self.board.place_ship(ship) # placing ship in field

class GameGUI: # main class, which game graphical interface manager
    def __init__(self, root):
        self.root = root # saving link for main page tkinker
        self.root.title("Battleship") # main page subtitle
        self.game_over = False # flag of the game finishing, initially False

        # creating two player: one for player, one for computer
        self.player = Player("Player") # creating object class Player for player
        self.computer = Player("Computer") # creating object class Player for computer

        self.computer_shots = set() #saving coords of shots computer, for not shoots again

        # Create 2D arrays of buttons to draw the players fields
        self.buttons_player = [[None] * 10 for _ in range(10)] # player field
        self.buttons_computer = [[None] * 10 for _ in range(10)] # player computer
        self.create_boards() # method for creating and drawing game boards

    def create_boards(self): # The method creates graphic fields of players and places them in the window
        frame = tk.Frame(self.root) # create container for placing both field
        frame.pack(pady=20) # add indentation at the top

        # create field for player
        player_frame = tk.Frame(frame) # create separate container for the player's field
        player_frame.pack(side=tk.LEFT, padx=20) # place the field to the left with an indentation

        # Header above the player's field
        tk.Label(player_frame, text="Your field", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=11)

        # adding the column number (1-10) on top
        for x in range(10):
            tk.Label(player_frame, text=str(x + 1), width=2).grid(row=1, column=x + 1)

        # fill the player's field with button-cells
        for y in range(10):
            # adding letters (A-J) left from lines
            tk.Label(player_frame, text=chr(65 + y), width=2).grid(row=y + 2, column=0)
            for x in range(10):
                # getting cell symbol  (if there is ship, show him, otherwise empty string )
                btn_text = self.player.board.grid[y][x] if self.player.board.grid[y][x] != " " else " "
                btn = tk.Button(player_frame, text=btn_text, width=2, height=1)
                btn.grid(row=y + 2, column=x + 1)  # placing button in the grid
                self.buttons_player[y][x] = btn  # save button in the array

        # creating field for computer
        computer_frame = tk.Frame(frame) # create conteiner for computer field
        computer_frame.pack(side=tk.RIGHT, padx=20) # placing the field on the right

        # Header above the computer field
        tk.Label(computer_frame, text="Computer field", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=11)

        # adding the column number (1-10) on top for computer
        for x in range(10):
            tk.Label(computer_frame, text=str(x + 1), width=2).grid(row=1, column=x + 1)

        # filling the computer field with button-cells
        for y in range(10): # adding letters from left
            tk.Label(computer_frame, text=chr(65 + y), width=2).grid(row=y + 2, column=0)
            for x in range(10): # the computer fields button react when players shot
                btn = tk.Button(computer_frame, text=" ", width=2, height=1,command=lambda x=x, y=y: self.make_move(x, y))
                btn.grid(row=y + 2, column=x + 1)
                self.buttons_computer[y][x] = btn  # saving button in array

        # adding status line, which says whose move now
        self.status_label = tk.Label(self.root, text="Your move!", font=("Arial", 14))
        self.status_label.pack()

    def make_move(self, x, y): # method of processing player move(shooting computer field)
        if self.game_over: # if game finished, ignor pressing
            return

        # checking, we are shoots in cell previosly
        if self.computer.board.grid[y][x] in {"X", "."}:
            self.status_label.config(text="You've already shot here ") # printing warning
            return









