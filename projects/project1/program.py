
from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace

def main():
    card_suits = [suit.value for suit in list (CardSuit)]
    print(card_suits)

    for suit in list(CardSuit):
        for face in list(CardFace):
            card_suits.append(Card(suit.value, face.value))

if __name__ == '__main__':
    main()
