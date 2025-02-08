# The game starts with a shuffled deck containing multiple decks of cards.
# The player and dealer are each dealt two cards.
# The dealer's initial hand should only show one card face up. The other card should be hidden.
# The player chooses to "Hit" or "Stay".
# If the player hits, they receive another card. If they exceed 21, they lose.
# When the player stays, the dealer reveals their hand and draws until reaching at least 17.
# The winner of a round is determined based on the final scores.
# The game should prompt the player to determine if they wish to play again or quit.

# class Game:
#     def __init__(self, player1: Character, player2: Character) -> None:
#         """ Constructor for the Game class. Sets the players to instance variables.
#         Args:   
#             player1 (Character): The first player.
#             player2 (Character): The second player.
#         """
#         self.__player: Character = player1
#         self.__dealer: Character = player2

#     def shuffle(self, attacker: Character, defender: Character) -> None:
#         """ Attacks the defender. Algorithm: 
#             1. Roll a random number between 1 and 6 for the attack.
#             2. Subtract the attack value from the defender's health.
#             3. If the defender's health is less than or equal to 0, they are defeated.
#             4. Print the result of the attack.
#         Args:
#             attacker (Character): The attacker.
#             defender (Character): The defender. 
#         """
#         attackRoll: int = random.randint(1, 6)

#         #character_types = list(CharacterType)
#         # print(f"Character types: {character_types}")
#         # random_character_type = random.choice(character_types)
#         # print()

#         damage = attackRoll * attacker.attack_power
#         defender.health -= damage
#         print(f"This attack dealt {damage}")
#         if (defender.health <= 0):
#             print(f"{defender.name} defeated!")


#     def start_battle(self) -> None:
#         """ Starts the battle between the two players. Algorithm: 
#             1. While both players are alive, do the following:
#                 1.1. Player 1 attacks Player 2.
#                 1.2. If Player 2 is defeated, break the loop.
#                 1.3. Player 2 attacks Player 1.
#                 1.4. If Player 1 is defeated, break the loop.
#             2. Print the result of the battle.
#         """
#         turn: int = 0
#         while self.__player1.health > 0 and self.__player2.health > 0:
#             if turn % 2 == 0:
#                 self.attack(self.__player1, self.__player2)
#             else:
#                 attack(self, self.__player2, self.__player1)
#             turn += 1
#         winner: Character = self.__player1 if self__player1.health > 0 else self.__player2
#         print(f"{winner.name} wins the battle!")
