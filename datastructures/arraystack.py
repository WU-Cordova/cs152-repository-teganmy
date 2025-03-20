import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        self._maxsize = max_size
        self.data_type = data_type
        self._top = -1
        self.size = 0
        self.stack = Array([0] * max_size, data_type)

    def push(self, item: T) -> None:
        ''' Pushes an item onto the stack.
        
            Arguments:
                item: T -- The item to push onto the stack.
        '''
        if self.full:
            raise IndexError("Full!")
        
        self._top += 1
        self.stack[self._top] = item
        self.size += 1

    def pop(self) -> T:
        ''' Pops an item from the stack.

            Returns:
                T -- The item popped from the stack.
        '''
        if self.empty:
            raise IndexError("Empty!")
        
        to_return = self.stack[self._top]
        self._top -= 1
        self.size -= 1
        return to_return

    def clear(self) -> None:
        for i in range(self.size):
            del self.stack[i]
        self.size = 0

    @property
    def peek(self) -> T:
        ''' Returns the top item on the stack without removing it.

            Returns:
                T -- The top item on the stack.
        '''
        return self.stack[self._top]

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self._maxsize

    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        return self.size == self._maxsize

    @property
    def empty(self) -> bool:
        return self.size == 0

    def __eq__(self, other: object) -> bool:
        if self.size != other.size:
            return False
        for i in range(self.size):
            if self.stack[i] != other.stack[i]:
                return False
        return True


    def __len__(self) -> int:
       return self.size
    
    def __contains__(self, item: T) -> bool:
       return item in self.stack

    def __str__(self) -> str:
        return str([int(self.stack[i]) for i in range(self._top + 1)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self._maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

