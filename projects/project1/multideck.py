from datastructures.bag import Bag
from projects.project1.card import Card, CardFace, CardSuit
import random
class Deck:
    def __init__(self):
        """ Constructor for the Game class. Includes cards attribute and function to create a new deck."""
        self.cards = []
        self.make_deck()

    def make_deck(self):
        """Adds each card from the Card class to a new deck."""
        for suit in list(CardSuit):
            for face in list(CardFace):
                self.cards.append(Card(face, suit))

def shuffle(deck):
    """Function to create a Multi-Deck with 2, 4, 6, or 8 decks.
        Args:   
            deck: The deck that will be multiplied to create a multi-deck.
        """
    multiDeck = Bag()
    decks = 1
    while(decks % 2 != 0):
        decks = random.randint(2,8)
    for d in range(decks):
        for card in deck.cards:
            multiDeck.add(card)
    return multiDeck

def deal(multiDeck):
    """ Function to deal cards to each of the players, who start with 2 for each game.
        Args:   
            multiDeck: the set of cards from which the hands are dealt.
        """
    hand = []
    for i in range(2):
        card = random.choice(list(multiDeck.distinct_items()))
        hand.append(card)
        multiDeck.remove(card)
    return(hand)
