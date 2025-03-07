class Cell:
    def __init__(self, alive: bool = False):
        self.alive = alive
    
    def next_state(self, neighbors: int) -> bool:
        #do this with is_alive setter and/or match cases?
        if neighbors == 0 or neighbors == 1:
            return False
        elif neighbors == 2:
            return self.alive
        elif neighbors == 3:
            return True
        elif neighbors >= 4:
            return False

    @property
    def is_alive(self) -> bool: 
        return self.alive

    @is_alive.setter
    def is_alive(self, alive: bool):
        self.alive = alive

    def __eq__(self, value):
        if isinstance(value, Cell):
            return self.alive == value.alive
        return False

    def __str__(self): return "🦠" if self.alive else " "