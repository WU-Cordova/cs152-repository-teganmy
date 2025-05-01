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
        """ Prints initial menu information so customer knows what their choices are.
        """
        print(("""Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit"""))

    def order_option(self) -> None:
        """ Creates new order once customer has chosen their first option 
        and runs program according to customer input.
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
                    print(menu)

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
                    self.open_orders.append(custOrder)
                    print(menu)

                case 3:
                    if len(self.open_orders) == 0:
                        print("There are no open orders")                
                    else:
                        for order in self.open_orders:
                            print(str(order))
                    print(menu)
                          
                case 4:
                    if len(self.order_queue) == 0:
                        print("The queue is empty; there are no open orders!")
                    else:
                        recent = self.order_queue.dequeue()
                        del(self.open_orders[0])
                        print(f"Completed order for {recent.cust_name}!")
                    print(menu)

                case 5: 
                    print("End of day report:")
                    print(f"{'Drinks':<20}{'Qty Sold':<20}{'Total':<10}")
                    total = 0 
                    for item in self.report.distinct_items():
                        print(f"{str(item.name):<20}{self.report.count(item):<20}{str(item.price * self.report.count(item))+"0":<10}")
                        total += item.price * self.report.count(item)
                    print(f"{'Total Revenue:':<39} {total}0")
                    print(menu)

                case 6:
                    self.orders_complete = True

                case 7:
                    print("Please enter a valid choice.")
        check_option(option)
