from typing import List
from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit
from time import sleep

class GameController:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.history: List[Grid] = []
    
    def run(self) -> None:

        print("Press 'q' to quit.")
        kbhit = KBHit()
        generation = 0
        
        while True:
            print(f"Generation {generation}:")
            self.grid.display()
            sleep(1)
            if kbhit.kbhit():
                key = kbhit.getch()

                if key == 'q':
                    print("You hit quit.")
                    return
            self.history.append(self.grid)
            self.grid = self.grid.next_generation()
            if len(self.history) > 3:
                if (self.grid == self.history[-1]) or (self.grid == self.history[-2]):
                    return
            generation += 1