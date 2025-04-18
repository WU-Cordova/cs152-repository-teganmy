class Cell:
    def __init__(self, alive: bool = False):
        """ Constructor for the Cell class. As a default, sets the cell to be alive, and records 
        state of alive-ness as an attribute."
        """
        self.alive = alive
    
    def next_state(self, neighbors: int) -> bool:
        """ Function to determine whether a cell will be alive in the next generation
        based on how many neighbors it has. Takes in a number of neighbors and returns a boolean
        corresponding to whether it is alive (True) or not (False).
        """
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
        """Cell property describing whether it is alive."""
        return self.alive

    @is_alive.setter
    def is_alive(self, alive: bool):
        """ Function to set the cell's state to living.
        """
        self.alive = alive

    def __eq__(self, value):
        """Function to see if the state of a given value matches that of the cell."""
        if isinstance(value, Cell):
            return self.alive == value.alive
        return False

    def __str__(self): return "🦠" if self.alive else " "