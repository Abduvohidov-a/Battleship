import tkinter as tk
import random   # importing necessary modules

class Board: # creating class Board which include information ship placing, ship hitting, and ship sunking
    def __init__(self, size=10):
        self.size = size # Field size
        self.grid = [[" "] * size for _ in range(size)] # creating empty field

    def place_ship(self, ship): # method placing ship in field
        for x,y in ship.coords:
            self.grid[y][x] = ship.symbol # set the ship symbol to the coordinates on the field
