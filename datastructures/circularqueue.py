from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue. The queue
        is circular in the sense that the front and rear pointers wrap around the
        array when they reach the end. The queue is full when the rear pointer is
        one position behind the front pointer. The queue is empty when the front
        and rear pointers are equal. This implementation uses a fixed-size array.
    """

    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        ''' Initializes the CircularQueue object with a maxsize and data_type.
        
            Arguments:
                maxsize: The maximum size of the queue
                data_type: The type of the elements in the queue
        '''
        # initialize front_index to 0
        self.front_index: int = 0
        # initialize _count to 0
        self._count: int = 0
        # initialize _maxsize to maxsize
        self._maxsize = maxsize
        self._queue = Array([0] * maxsize, data_type)
        # initialize _queue as array with maxsize and data_type

    def enqueue(self, item: T) -> None:
        ''' Adds an item to the rear of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.rear
                3
                >>> q.enqueue(4)
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.enqueue(6)
                IndexError('Queue is full')
            
            Arguments:
                item: The item to add to the queue
                
            Raises:
                IndexError: If the queue is full
        '''

        # raise indexerror if full
        if self.full:
            raise IndexError("Queue is full.")

        next_position = (self.front_index + self._count) % self._maxsize
        self._queue[next_position] = item
        self._count += 1
       
        # update _count (!!!!)

    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.dequeue()
                1
                >>> q.dequeue()
                2
                >>> q.dequeue()
                3
                >>> q.dequeue()
                IndexError('Queue is empty')
                >>> q.dequeue()
                IndexError('Queue is empty')

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        # raise indexerror if empty
        if self.empty:
            raise IndexError("Queue is empty.")
        item_to_return = self._queue[self.front_index]

        self._queue[self.front_index] = 0

        # update _fr0nt_index to (_front _ 1) % _maxsize
        self.front_index = self.front_index + 1 % self._maxsize

        self._count -= 1
        # upate count!!!
        return item_to_return

    def clear(self) -> None:
        ''' Removes all items from the queue '''
        for i in range(len(self._queue)):
            del self._queue[self.front_index]
        self._count = 0

    @property
    def front(self) -> T:
        ''' Returns the item at the front of the queue without removing it

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        # raise indexerror for underflow (empty)
        if self.empty:
            raise IndexError("Queue is empty.")
        return self._queue[self.front_index]

    @property
    def full(self) -> bool:
        ''' Returns True if the queue is full, False otherwise 
        
            Returns:
                True if the queue is full, False otherwise
        '''
        return self._count == self._maxsize 

    @property
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise
        
            Returns:
                True if the queue is empty, False otherwise
        '''
        return self._count == 0
    
    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the queue
        
            Returns:
                The maximum size of the queue
        '''
        return self._maxsize 

    def __eq__(self, other: object) -> bool:
        ''' Returns True if this CircularQueue is equal to another object, False otherwise
        
            Equality is defined as:
                - The front and rear pointers are equal
                - The elements between the front and rear pointers are equal, even if they are in different positions
                
            Arguments:
                other: The object to compare this CircularQueue to
                
            Returns:
                True if this CircularQueue is equal to another object, False otherwise
        '''
        if (self._count != other._count):
            return False
        for i in range(self._count):
            self_pos = (self.front_index + i) % self._maxsize
            other_pos = (other.front_index + i) % other._maxsize
            if self._queue[self_pos] != other._queue[other_pos]:
                return False
        return True
        # same count
        # same items from front to rear (need to focus on items being equal in order instead of indexes) - can still be equal in terms of front and rear but have different index locations
        
    
    def __len__(self) -> int:
        ''' Returns the number of items in the queue
        
            Returns:
                The number of items in the queue
        '''
        return self._count

    def __str__(self) -> str:
        ''' Returns a string representation of the CircularQueue
        
            Returns:
                A string representation of the queue
        '''
        return str(self._queue)

    def __repr__(self) -> str:
        ''' Returns a developer string representation of the CircularQueue object
        
            Returns:
                A string representation of the CircularQueue object
        '''
        return f'ArrayQueue({repr(self._queue)})'
                                  
