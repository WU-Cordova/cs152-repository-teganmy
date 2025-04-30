from projects.project3.bistrosystem import System
from projects.project3.drink import Drink, DrinkFlavor, DrinkPrice

def main():
    bistro = System()
    bistro.new_order()
    while bistro.orders_complete == False:
        bistro.order_option()

if __name__ == '__main__':
    main()
