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
