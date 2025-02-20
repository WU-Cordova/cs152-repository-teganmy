
from datastructures.bag import Bag
def main():
    
    print("Hello, World!")
    bag = Bag()
    bag.add(8)
    bag.add(8)
    bag.add(9)
    
    print(bag.distinct_items())


if __name__ == '__main__':
    main()
