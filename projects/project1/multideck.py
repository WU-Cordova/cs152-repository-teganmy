from datastructures.bag import Bag
from projects.project1.card import Card, CardFace, CardSuit
import random
class Deck:
    def __init__(self):
        self.cards = []
        self.make_deck()

    def make_deck(self):
        for suit in list(CardSuit):
            for face in list(CardFace):
                self.cards.append(Card(suit.value, face.value))


def shuffle(deck):
    multiDeck = Bag()
    decks = 1
    while(decks % 2 != 0):
        decks = random.randint(2,8)
    for d in range(decks):
        for card in deck.cards:
            multiDeck.add((card.card_suit, card.card_face))
    return multiDeck

def deal(multiDeck):
    hand = []
    for i in range(2):
        card = random.choice(multiDeck())
        hand.append(card)
        multiDeck.remove(card)
    return(hand)

