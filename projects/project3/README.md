1. Menu: Since the menu is a fixed set of items, I decided an array would be a good option. It doesn't require resizing
since nothing is added to the menu after its initial creation, and the array allows for fast (linear) item lookup.
2. Customer Order: Originally I tried to use a linked list for this structure, but I had difficulty understanding how
the structure could best support orders, so I switched to a linked list. This means that a customer would be able to add
a drink without having to resize the whole structure, and if I implemented completing one drink at a time from the order,
removing items from the front would not require shifting everything up, making it more efficient.
3. Order Confirmation: stack (liststack?)
4. Open Orders Queue: For the open orders queue, I decided to use a deque. The linked list based structure means that
when an order is added to or removed from the front of the queue one node is removed instead of everything needing to be shifted
down (linear vs constant time).
5. Completed Orders/EOD Report: I chose a bag because it contains counts for each item, which is useful 
for something like a summary of drinks ordered, as well as which dinstinctive drink choices customers made.

Limitations: Customer must give int input for menu choice, quantity of drinks, and drink number or program errors;
Customer can put in customization input but it is not repeated back to them in order summary. If I had more time, 
I would change some things about the formatting (for example, when users are prompted to add drink numbers I would
include a list of corresponding drinks) and I would like to figure out a better way to include the customization in
the order summaries. Finally, I tried to add a system where one drink at a time would be marked complete, but I didn't
iron it out in time.

To run program: from program.py click run; program will print main menu and ask user to make their first choice.
User can choose from options 1-6 to make different choices with the system, and press 6 when they wish to exit.

## Example program
![alt text](image.png)
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 1
Drink: Black Coffee  Price: $3.50
Drink: Latte  Price: $4.50
Drink: Mocha  Price: $5.50
Drink: Chai  Price: $4.50
Drink: Hot Chocolate  Price: $4.00
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 2
What's your name? Tegan
How many drinks would you like to order? 2
Drink #1: Enter drink number (1-5): 1
Any customization for Black Coffee? No
Drink #2: Enter drink number (1-5): 3
Any customization for Mocha? No
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 2
What's your name? Adam
How many drinks would you like to order? 3
Drink #1: Enter drink number (1-5): 3
Any customization for Mocha? Whipped Cream
Drink #2: Enter drink number (1-5): 4
Any customization for Chai? no
Drink #3: Enter drink number (1-5): 5
Any customization for Hot Chocolate? Extra hot
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 3
Order for Tegan: Black Coffee, Mocha
Order for Adam: Mocha, Chai, Hot Chocolate
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 4
Completed order for Tegan!
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 3
Order for Adam: Mocha, Chai, Hot Chocolate
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 4
Completed order for Adam!
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 3
There are no open orders
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 4
The queue is empty; there are no open orders!
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 5
End of day report:
Drinks              Qty Sold            Total     
Hot Chocolate       1                   4.00      
Black Coffee        1                   3.50      
Mocha               2                   11.00     
Chai                1                   4.50      
Total Revenue:                          23.00
Welcome To The Bistro!
        1. Display Menu
        2. Take New Order
        3. View Open Orders
        4. Mark Next Order as Complete
        5. View End-of-Day Report
        6. Exit
Main Menu:
What would you like to do? 6