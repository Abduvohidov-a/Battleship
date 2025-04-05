# Battleship
BATTLESHIP
GitHub Repository: https://github.com/Abduvohidov-a/Battleship
Identification
- Name: Sardor Abduvohdiov
- P-number: P465811
- Course code: IY499
  
Declaration of Own Work
I confirm that this assignment is my own work.
Where I have referred to academic sources, I have provided in-text citations and included the sources in the final reference list.

Introduction
This a Battleship game, writted in python language with using tkinker library for graphic visualation. In this game i realised game again computer, which randomly choose where shoot, game writed with used object-oriented-programming where all entity have classifayed, also used logging library for file handling, which save result after game in another file who won, used random module for writing logic for computer enemy and placing ships, and datetime module for saving when enemy or player won. 

GAME Features:
1. Realising graphic interface with using tkinker, player and computer field shown side-by-side
2. Game play with a simple playing, and nice interface
3. Random ship placing with logic, to avoid ships from being placed next to each other
4. Miss and Hit effect, when player or computer hit marked red cell "X" writed, when miss blue cell "."
5. Computer logic, they randomly shoot to cell, while avoiding repeating the same position.
6. Win detection, game stopped when all ship sunks
7. Module structure, all components are built in a clear and reusable object-oriented way.
8. Using logging, all game results savings after game with writing who win and when
9. Error handling, to manage invalid user input like repeated clicks.
10. Realise simple search method, inside "SHIP" class, in "generate_coords" func, i realise simple search method
"if all(board.grid[y][x] == " " and self.no_adjacent_ships(x, y, board) for x, y in coords):" in this block of code, It is a linear walk through the list of coordinates with condition checking. That is, it is a simple search algorithm with filtering.

Installation
To run the game, ensure you have Python installed, and then install the required dependencies using:
pip install -r requirements.txt

How to Play
- Click on the computer’s grid to fire at a cell.
- A red “X” indicates a hit, a blue “.” indicates a miss.
- Sink all computer ships before yours are sunk.
- Player always starts first.
  
Running the Game
python main.py

Running Unit Tests
python UnitTest.py

Game Elements
- Player board and computer board.
- Five ships of different sizes: Aircraft Carrier (5), Battleship (4), Cruiser (3), Submarine (3), Destroyer (2).
- Logging system records results in a .log file.
- Buttons for each cell that change appearance based on hits/misses.
  
Libraries Used
- Tkinter
- random
- logging
- datetime
  
Project Structure
- main.py: Main game logic and GUI
- ErrorHandling/: (if any) directory for error management classes
- battleship_results.log: Log file generated after game ends
- UnitTest.py: Script for running tests (optional)
  
Unit Tests (optional)
The project includes optional unit tests to validate the game logic. Navigate to the project directory and run the test file to verify functionality.
