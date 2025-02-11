from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace
from projects.project1.multideck import Deck, shuffle, deal
import random

class Game:
    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0 #sum(card.card_face.face_value() for card in self.player_hand)
        self.dealer_score = 0 #sum(card.card_face.face_value() for card in self.dealer_hand)
        self.deck = None
        self.over = False

    def start_game(self) -> None:
        deck = Deck()
        self.shuffled = shuffle(deck)
        print(f'length: {len(self.shuffled)}')

        self.player_hand = deal(self.shuffled)
        self.dealer_hand = deal(self.shuffled)

        while (sum(card.card_face.face_value() for card in self.dealer_hand) < 17):
            self.dealer_hand = deal(self.shuffled)
        
        self.player_score = sum(card.card_face.face_value() for card in self.player_hand)
        self.dealer_score = sum(card.card_face.face_value() for card in self.dealer_hand)
        print(self.player_score)
        print(self.dealer_score)
        
        print("Initial Deal:")
        print(f"Player's Hand: {"".join(str(card) for card in self.player_hand)} with a face value of: {self.player_score}")
        print(f"Dealer's Hand: {(self.dealer_hand[0])} [Hidden] with a face value of: {(self.dealer_hand[0].card_face.face_value())})\n")

    def round(self):
        print(f"Player's Hand: {"".join(str(card) for card in self.player_hand)} | Score: {sum(card.card_face.face_value() for card in self.player_hand)}")
        move = input("Would you like to (H)it or (S)tay? ")
        if (move == "H"):
            card = random.choice(list(self.shuffled.distinct_items()))
            self.player_hand.append(card)          
            self.player_score += card.card_face.face_value()
            if (self.player_score > 21):
                print(f"Player's Hand: {"".join(str(card) for card in self.player_hand)} | Score: {self.player_score}")
                print("Bust! You went over 21.\n")
                print(f"Dealer's Hand: {"".join(str(card) for card in self.dealer_hand)} | Score: {self.dealer_score}")
                print("Dealer wins! Player busted.\n")
                self.over = True
        elif (move == "S"):
            print(f"Dealer's Hand: {"".join(str(card) for card in self.dealer_hand)} | Score: {self.dealer_score}")
            if(self.dealer_score > self.player_score):
                print("Dealer wins!")
                self.over = True
            else:
                print("Player wins!")
                self.over = True
