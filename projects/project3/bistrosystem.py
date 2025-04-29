from datastructures.array import Array
from projects.project3.drink import Drink, DrinkFlavor, DrinkPrice
from projects.project3.orderitem import OrderItem
from datastructures.bag import Bag

class System:
    def __init__(self):
        """ Constructor for the System class. Defines menu, orders, and creates "End-Of-Day Report.
        """
        drinks = []
        for flavor in DrinkFlavor:
            price = DrinkPrice[flavor.name]
            drink = Drink()
            drink.name = flavor
            drink.price = price.value
            drinks.append(drink)
        self.menu = Array(starting_sequence = drinks)
        self.report = Bag()

    def start_order(self) -> None:
        """ Creates a Multi-Deck of cards and deals to each of the players, 
        printing information on the inital hand and score 
        """
        menu = ("""Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit""")


        option = input("What would you like to do? ")
        print(menu)
        if option == "1":
            for item in self.menu:
                print(f"Drink: {item.name}  Price: ${item.price:.2f}")
            print(menu)
        if option == "2":
            name = input("What's your name? ")
            drinkCount = int(input("How many drinks would you like to order? "))
            order = CustomerOrder()
            for i in range(drinkCount):
                drink = input("Drink #1: Enter drink number (1-5):")
                self.report.add(drink)
                customization = (f"Any customization for {drink}?")
                order_item = OrderItem(drink, customization)
                order.append(order_item)

            print(menu)
                    # create order item with drink and customizaton
                    # add order to queue
                    # repeat back order with stack

        # while option != "6":
        #     main_menu(option)
        # #match cases for 1, 2, 3, 4, 5, 6
        # def main_menu(choice):
        #     match option:
        #         case "1":
        #             for item in self.menu:
        #                 print(f"Drink: {item.name}  Price: ${item.price:.2f}")
    
        