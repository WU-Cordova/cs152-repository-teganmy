from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace
from projects.project1.multideck import Deck, shuffle, deal
from projects.project1.game import Game

def main():
    """Creates a game and uses the round function to continue it until a player hits 21; 
    offers the user the option to start new games."""
    game = Game()
    game.start_game()

    while (game.over == False and game.player_score < 21 and game.dealer_score < 21):
        game.round()            

    playing = input("Would you like to play again? (Y)es or (N)o: ")
    while (playing == "Y"):
        game = Game()
        game.start_game()
        while (game.over == False and game.player_score < 21 and game.dealer_score < 21):
            game.round()            
        playing = input("Would you like to play again? (Y)es or (N)o: ")
    print("Game over! Thanks for playing :)")

if __name__ == '__main__':
    main()
