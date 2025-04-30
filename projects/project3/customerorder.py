from projects.project3.drink import Drink
from projects.project3.orderitem import OrderItem
from datastructures.linkedlist import LinkedList
from datastructures.hashmap import HashMap

class CustomerOrder:
    def __init__(self, name: str, items: list):
        self.cust_name = name
        self.items = items
        self.order = LinkedList((name, items))

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        string = ', '.join([str(item) for item in self.items])
        return f"Order for {self.cust_name}: {items_str}"