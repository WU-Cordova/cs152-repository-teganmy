from datastructures.array import Array
class System:
    def __init__(self):
        """ Constructor for the Game class. Sets score, deck, hand, and "game-over" attributes for the players.
        """
        self.menu = Array(starting_sequence = ["Black Coffee", "Latte", "Mocha", "Chai", "Hot Chocolate"])

    def start_order(self) -> None:
        """ Creates a Multi-Deck of cards and deals to each of the players, 
        printing information on the inital hand and score 
        """
        deck = Deck()
        self.shuffled = shuffle(deck)

        self.player_hand = deal(self.shuffled)
        self.dealer_hand = deal(self.shuffled)

        while (sum(card.card_face.face_value() for card in self.dealer_hand) < 17):
            self.dealer_hand = deal(self.shuffled)
        
        self.player_score = sum(card.card_face.face_value() for card in self.player_hand)
        self.dealer_score = sum(card.card_face.face_value() for card in self.dealer_hand)
        
        print("Initial Deal:")
        print(f"Player's Hand: {"".join(str(card) for card in self.player_hand)} with a face value of: {self.player_score}")
        print(f"Dealer's Hand: {(self.dealer_hand[0])} [Hidden] with a face value of: {(self.dealer_hand[0].card_face.face_value())}\n")