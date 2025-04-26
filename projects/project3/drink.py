# File: AdvItem.py

"""This module defines a class that models an item in Adventure."""

#########################################################################
# Your job in this assignment is to fill in the definitions of the      #
# methods listed in this file, along with any helper methods you need.  #
# You won't need to work with this file until Milestone #4.  In my      #
# solution, none of the milestones required any public methods beyond   #
# the ones defined in this starter file.                                #
#########################################################################

class Drink:

    def __init__(self, name, description, location):
        """Creates an AdvItem from the specified properties.

        Args:
            name (str): the unique name of the item
            description (str): a short description of the item
            location (str): the name of the location where the item first appears
        """
        self.name = name
        self.description = "Medium"
        self.price = price
        self.customization = customization

    def __str__(self):
        """Converts an AdvItem to a string."""
        return self.get_name()

    def get_name(self):
        """Returns the name of this item."""
        return self.name

    def get_description(self):
        """Returns the description of this item."""
        return self.description

    def get_price(self):
        """Returns the price of this item."""
        return self.price
