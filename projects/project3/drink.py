# File: AdvItem.py

"""This module defines a class that models an item in Adventure."""

#########################################################################
# Your job in this assignment is to fill in the definitions of the      #
# methods listed in this file, along with any helper methods you need.  #
# You won't need to work with this file until Milestone #4.  In my      #
# solution, none of the milestones required any public methods beyond   #
# the ones defined in this starter file.                                #
#########################################################################
from enum import Enum
from dataclasses import dataclass
class DrinkFlavor(Enum):
    BLACK_COFFEE = "Black Coffee"
    LATTE = "Latte"
    MOCHA = "Mocha"
    CHAI = "Chai"
    HOT_CHOCOLATE = "Hot Chocolate"
    
    def __str__(self):
        return str(self.value)

class DrinkPrice(Enum):
    BLACK_COFFEE = 3.50
    LATTE = 4.50
    MOCHA = 5.50
    CHAI = 4.50
    HOT_CHOCOLATE = 4.00

    def __str__(self):
        return str(self.value)


class Drink:
    name = DrinkFlavor
    size: str = "Medium"
    price = DrinkPrice
    