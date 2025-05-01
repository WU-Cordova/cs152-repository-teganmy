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
    