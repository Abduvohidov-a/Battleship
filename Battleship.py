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
        if self.grid[y][x] == " ":
            self.grid[y][x] = "."
            return False
        elif self.grid[y][x] in {".", "X"}:
            return False
        else:
            self.grid[y][x] = "X"
            return True

    def all_ships_sunk(self):
        return all(cell in {"X", " ", "."} for row in self.grid for cell in row)