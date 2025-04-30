from projects.project3.drink import Drink

class OrderItem:
    def __init__(self, drink, customization = None):
        self.drink = drink
        self.customization = customization
        self.order = {self.drink.name: self.customization}

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        return str(self.order)    