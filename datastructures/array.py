# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
import copy


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type:  type=object) -> None: 
         # Check that starting sequence is of valid sequence type
        if not isinstance(starting_sequence, Sequence):
            raise ValueError('starting_sequence must be a valid sequence type')
        self.__logical_size: int = len(starting_sequence)
        self.__physical_size: int = self.__logical_size
        self.__data_type: type = data_type

        # Check that starting sequence only has 1 type of data
        for index in range(self.__logical_size):
            if not isinstance(starting_sequence[index], self.__data_type):
                raise TypeError('Items in starting sequence are not all the same type')
        
        # Create array
        self.__elements = np.empty(self.__logical_size, dtype = self.__data_type)

        if self.__data_type not in (int, float, complex):
        # Initialize array
            for index in range(self.__logical_size):
                self.__elements[index] = copy.deepcopy(starting_sequence[index])
        else:
            for index in range(self.__logical_size):
                self.__elements[index] = copy.copy(starting_sequence[index])

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if not isinstance (index, int | slice):
            raise TypeError("Function requires index or slice")
        if isinstance(index, int):
            if index > self.__logical_size:
                raise IndexError("Index out of bounds")
            return self.__elements[index]
        elif isinstance(index, slice):
            start = index.start
            stop = index.stop
            step = index.step
            if start is not None:
                if start > self.__logical_size:
                    raise IndexError("Index out of bounds")
            if stop is not None:
                if stop > self.__logical_size:
                    raise IndexError("Index out of bounds")
                    # check if start and stop are in bounds. If they are not,
                    # raise an exception
            return Array(starting_sequence = self.__elements[start:stop:step].tolist(), data_type = self.__data_type)
    
    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(item, self.__data_type):
                raise TypeError('Items in starting sequence are not all the same type')
        self.__elements[index] = item

    def append(self, data: T) -> None:

        # If array is at max capacity, double the array size
        if (self.__physical_size == self.__logical_size):
            self.__physical_size *= 2

            # Create new array
            newArray = np.empty(self.__physical_size, dtype = self.__data_type)

            # Initialize array
            for index in range(self.__logical_size):
                newArray[index] = self.__elements[index]
            self.__elements[index]
        
        # Add the new element to the end
        self.__elements[len(self)-1] = data
        self.__logical_size += 1
        
            
    def append_front(self, data: T) -> None:
        # If array is at max capacity, double the array size
        if self.__physical_size == self.__logical_size:
            self.__physical_size *= 2

            # Create new array
            newArray = np.empty(self.__physical_size, dtype = self.__data_type)

            # Initialize array
            for index in range(self.__logical_size):
                newArray[index] = self.__elements[index]
            self.__elements[index]
        
        # Traverse the array backwards
        for index in reversed(range(self.__logical_size)):
            # Move every element forward by 1
            self.__elements[index + 1] = self.__elements[index]
        
        # Add the new element to the front
        self.__elements[0] = data
        self.__logical_size += 1

    def pop(self) -> None:
        if (self.__logical_size <= self.__physical_size/4):
            self.__physical_size = self.__physical_size/2

        newArray = np.empty(self.__physical_size, dtype = self.__data_type)

        for index in range(self.__logical_size):
            newArray[index] = self.__elements[index]
        
    def pop_front(self) -> None:
        if (self.__logical_size <= self.__physical_size/4):
            self.__physical_size = self.__physical_size/2

        newArray = np.empty(self.__physical_size, dtype = self.__data_type)

        for index in range(self.__logical_size):
            newArray[index-1] = self.__elements[index]

    def __len__(self) -> int: 
        return self.__logical_size

    def __eq__(self, other: object) -> bool: 
        if not isinstance(other, Array):
            return False
        if self.__logical_size != len(other):
            return False
        for i in range(len(other)):
            if other[i] != self.__elements[i]:
                return False
        return True
    
    def __iter__(self) -> Iterator[T]:
        return iter(self.__elements) 

    def __reversed__(self) -> Iterator[T]:
        reversed_elements = reversed(self.__elements)
        return iter(reversed_elements)

    def __delitem__(self, index: int) -> None:
        if (self.__logical_size <= self.__physical_size/4):
            self.__physical_size = self.__physical_size/2

        self.__elements = np.delete(self.__elements, index)
                
    def __contains__(self, item: Any) -> bool:
        return item in self.__elements 

    def clear(self) -> None:
        del(self.__elements)

        self.__physical_size = 0
        self.__logical_size = 0
        self.__elements = np.empty(self.__physical_size, dtype = self.__data_type)

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical_size}, Physical: {len(self.__elements)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')