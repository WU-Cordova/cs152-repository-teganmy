class Order:
    def __init__(self):
        """ Constructor for the Game class. Sets score, deck, hand, and "game-over" attributes for the players.
        """
        self.menu = Array(starting_sequence = ["Black Coffee", "Latte", "Mocha", "Chai", "Hot Chocolate"])
        self.dealer_hand = []