from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace
from projects.project1.multideck import Deck, shuffle, deal

def main():
    # card_faces = [face.value for face in list (CardFace)]
    # print(f'faces: {card_faces} and len {len(card_faces)}')

    # cards = []
    # print(f'suits:{list(CardSuit)}')
    # print(f'faces: {list(CardFace)}')

    # for suit in list(CardSuit):
    #     for face in list(CardFace):
    #         cards.append(Card(suit.value, face.value))
    # print(f'deck:{list(cards)}')

    deck = Deck()
    #print(list(deck.cards))
    shuffled = shuffle(deck)
    hand = deal(shuffled)
    print(hand)

if __name__ == '__main__':
    main()
