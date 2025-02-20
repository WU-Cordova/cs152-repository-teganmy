from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace
from projects.project1.multideck import Deck, shuffle, deal
import random

class Game:
    def __init__(self):
        """ Constructor for the Game class. Sets score, deck, hand, and "game-over" attributes for the players.
        """
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0 
        self.dealer_score = 0 
        self.deck = None
        self.over = False

    def start_game(self) -> None:
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
        if (self.player_score == 21):
            print("Player wins!")
            self.over = True
        elif (self.dealer_score == 21):
            print(f"Dealer's Hand: {"".join(str(card) for card in self.dealer_hand)} | Score: {self.dealer_score}")
            print("Dealer wins!")
            self.over = True

    def check_aces(self, hand):
        """ Checks how many aces the player is holding (for conversion between 1 and 11).
        Args:   
            hand: The hand of cards the player is holding
        """
        aces = 0
        for card in hand:
            if card.card_face == CardFace.ACE:
                aces += 1
        return aces

    def round(self):
        """ While both players have less than or equal to 21 points, they will play rounds. 
        Player can choose to hit or stay, picking up cards and calculating score."""

        print(f"Player's Hand: {"".join(str(card) for card in self.player_hand)} | Score: {sum(card.card_face.face_value() for card in self.player_hand)}")
        move = input("Would you like to (H)it or (S)tay? ")
        if (move == "H"):
            card = random.choice(list(self.shuffled.distinct_items()))
            self.player_hand.append(card)
            self.shuffled.remove(card)
            self.player_score += card.card_face.face_value()

            aces = self.check_aces(self.player_hand)
            if ((self.player_score > 21) and aces > 0):
                while ((self.player_score > 21) and aces > 0):
                    self.player_score -= 10  
                    aces -= 1

            if (self.player_score > 21):
                print(f"Player's Hand: {"".join(str(card) for card in self.player_hand)} | Score: {self.player_score}")
                print("Bust! You went over 21.\n")
                print(f"Dealer's Hand: {"".join(str(card) for card in self.dealer_hand)} | Score: {self.dealer_score}")
                print("Dealer wins! Player busted.\n")
                self.over = True

        elif (move == "S"):
            print(f"fwoo Dealer's Hand: {"".join(str(card) for card in self.dealer_hand)} | Score: {self.dealer_score}")
            if(self.dealer_score > self.player_score):
                print("Dealer wins!")
                self.over = True
            else:
                print("Player wins!")
                self.over = True
