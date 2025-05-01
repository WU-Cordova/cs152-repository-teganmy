from typing import List
from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit
from time import sleep

class GameController:
    def __init__(self, grid: Grid) -> None:
        """ Constructor for the GameController class. Creates a grid and a list of past grids in order
        to check.
        """
        self.grid = grid
        self.history: List[Grid] = []
    
    def run(self) -> None:
        """ Function to run each simulation. Allows the reader to choose between automatic and manual modes
        and displays each generation accordingly. Progresses the state of the cells in each generation, and 
        ends the simulation when the cells reach a state of stability.
        """

        gameMode = input("Please hit 'a' for automatic mode or 'm' for manual: ")

        kbhit = KBHit()
        generation = 0
        print("Press 'q' to quit.")


        if gameMode == "a":
            while True:
                print(f"Generation {generation}:")
                self.grid.display()
                sleep(1)
                if kbhit.kbhit():
                    key = kbhit.getch()

                    if key == 'q':
                        print("You hit quit.")
                        return
                generation += 1
                self.history.append(self.grid)
                self.grid = self.grid.next_generation()
                if len(self.history) > 3:
                    if (self.grid == self.history[-1]) or (self.grid == self.history[-2]):
                        print(f"Generation {generation}:")
                        self.grid.display()
                        print(f"Game ended after {generation} generations.")
                        return

        if gameMode == "m":
            print("Press 's' to continue to next step.")                
            while True:
                sleep(0.1)
                if kbhit.kbhit():
                    key = kbhit.getch()

                    if key == 'q':
                        print("You hit quit.")
                        return
                
                    elif key == 's':
                        print(f"Generation {generation}:")
                        self.grid.display()
                        generation += 1
                        self.history.append(self.grid)
                        self.grid = self.grid.next_generation()

                        if len(self.history) > 3:
                            if (self.grid == self.history[-1]) or (self.grid == self.history[-2]):
                                print(f"Generation {generation}:")
                                self.grid.display()
                                print(f"Game ended after {generation} generations.")
                                return