from projects.project3.drink import Drink

class OrderItem:
    def __init__(self, drink, customization = None):
        """ Constructor for the OrderItem class. Documents customer's drink, customizations for that drink, 
        and stores the drink-customization pair in a dictionary.
        """
        self.drink = drink
        self.customization = customization
        self.order = {self.drink.name: self.customization}

    def __str__(self) -> str:
        """
        Returns a string representation of the order item.

        Returns:
            str: A string representation of the order item.
        """
        return str(self.order)    