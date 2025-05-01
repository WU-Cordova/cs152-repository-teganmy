from projects.project3.drink import Drink
from projects.project3.orderitem import OrderItem
from datastructures.linkedlist import LinkedList

class CustomerOrder:
    def __init__(self, name: str, items: list):
        """ Constructor for the CustomerOrder class. Sets customer's name, items in their order (list), and a linked list of the items.
        """
        self.cust_name = name
        self.items = items
        self.order = LinkedList.from_sequence(items)

    def __str__(self) -> str:
        """
        Returns a string representation of the order.

        Returns:
            str: A string representation of the order.
        """
        string = ', '.join([str(item.drink.name) for item in self.items])
        return f"Order for {self.cust_name}: {string}"