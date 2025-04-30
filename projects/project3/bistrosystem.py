from datastructures.array import Array
from projects.project3.drink import Drink, DrinkFlavor, DrinkPrice
from projects.project3.orderitem import OrderItem
from projects.project3.customerorder import CustomerOrder
from datastructures.bag import Bag
from datastructures.deque import Deque


class System:
    def __init__(self):
        """ Constructor for the System class. Defines menu, orders, and creates End-Of-Day Report.
        """
        drinks = []
        for flavor in DrinkFlavor:
            price = DrinkPrice[flavor.name]
            drink = Drink()
            drink.name = flavor
            drink.price = price.value
            drinks.append(drink)
        self.menu = Array(starting_sequence = drinks)
        self.order_queue = Deque(data_type = CustomerOrder)
        self.report = Bag()
        self.open_orders = []
        self.orders_complete = False

    def new_order(self) -> None:
        print(("""Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit"""))

        #option = input("What would you like to do? ")

    def order_option(self) -> None:
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

        print("Main Menu:")
        option = int(input("What would you like to do? "))
        def check_option(choice):
            match option:
                case 1:
                    for item in self.menu:
                        print(f"Drink: {item.name}  Price: ${item.price:.2f}")

                case 2:
                    name = input("What's your name? ")
                    drinkCount = int(input("How many drinks would you like to order? "))
                    drink_order = []
                    for i in range(drinkCount):
                        drink = int(input(f"Drink #{i+1}: Enter drink number (1-5): "))
                        customization = input(f"Any customization for {self.menu[drink-1].name}? ")
                        order_item = OrderItem(self.menu[drink -1], customization)
                        drink_order.append(order_item)
                        self.report.add(self.menu[drink-1])
                    custOrder = CustomerOrder(name, drink_order)
                    self.order_queue.enqueue(custOrder)
                    self.open_orders.append(CustomerOrder)

                case 3:
                    if len(self.report) == 0:
                        print("There are no open orders")                
                    else:
                        for order in self.open_orders:
                            print(str(order))
                    print(menu)
                            # create order item with drink and customizaton
                            # add order to queue
                            # repeat back order with stack
                case 4:
                    recent = self.order_queue.dequeue()
                    print(f"Completed order for {recent.cust_name}!")

                case 5: 
                    print("End of day report:")
                    
                case 6:
                    self.orders_complete = True

                case 7:
                    print("Please enter a valid choice.")
        check_option(option)

            # while option != "6":
            #     main_menu(option)
            # #match cases for 1, 2, 3, 4, 5, 6
            # def main_menu(choice):
            #     match option:
            #         case "1":
            #             for item in self.menu:
            #                 print(f"Drink: {item.name}  Price: ${item.price:.2f}")
        
            