from __future__ import annotations
import os
from typing import Iterator, Sequence, List

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T

class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]): #handling second bracket
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            self.row_index = row_index
            self.array = array
            self.num_cols = num_columns
            self.data_type: type = data_type
             
        def map_index(self, row_index: int, column_index) -> int:
            return row_index * self.num_cols + column_index

        def __getitem__(self, column_index: int) -> T:
            # 1. ⛈️ If out of bounds, raise an IndexError
            # 2. ⛈️ Translate the `row_index` and `column_index` into a 1D `index`
            # 3. Return array[index]
            if column_index < 0 or column_index >= self.num_cols:
                raise IndexError("Index out of bounds")
            index: int = self.map_index(self.row_index, column_index)
            return self.array[index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            # This is the second bracket operator
            # 1. ⛈️ If out of bounds, raise an IndexError
            # 2. ⛈️ If `value` is not an instance of the right type, raise a TypeError.
            if (column_index < 0 or column_index >= self.num_cols):
                raise IndexError("Index out of bounds")
            if not isinstance(value, self.data_type):
                raise TypeError("Value is not the correct type")

            #Convert the `row_index` and `column_index` into a 1D `index`
            index: int = self.map_index(self.row_index, column_index)
            #Set array[index] = value  
            self.array[index] = value

        def __iter__(self) -> Iterator[T]:
             for column_index in range(self.num_cols):
                yield self[column_index]

        def __reversed__(self) -> Iterator[T]:         
            for column_index in range(self.num_cols - 1, -1, -1):
                yield self[column_index]

        def __len__(self) -> int:
            return self.num_cols
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_cols)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_cols - 1)])}, {str(self[self.num_cols - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, Sequence):
            raise ValueError('starting_sequence must be a valid sequence type')
        self.data_type: type = data_type

        self.rows_len = len(starting_sequence)
        self.cols_len = len(starting_sequence[0])

        for rows in starting_sequence:
            if not isinstance (rows, Sequence):
                raise ValueError('each row must be a valid sequence type')
            for item in rows:
                if not isinstance(item, self.data_type):
                    raise ValueError('all items must be the same data type')
            if len(rows) != self.cols_len:
                raise ValueError('all rows must be the same length')
    
        array_list = []
        for row in range(self.rows_len):
            for col in range(self.cols_len):
                array_list.append(starting_sequence[row][col])
        self.num_rows = len(starting_sequence)
        self.elements2d = Array(starting_sequence = array_list, data_type = data_type)

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        pylist2d: List[List[T]] = []
        for row in range(rows):
            pylist2d.append([])
            for col in range(cols):
                pylist2d[row].append(data_type())

        return Array2D(starting_sequence = pylist2d, data_type = data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        return Array2D.Row(row_index, self.elements2d, self.cols_len, self.data_type)

    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row_index in range(self.num_rows):
            yield self[row_index]
    
    def __reversed__(self):
        for row_index in range(self.num_rows - 1, -1, -1):
            yield self[row_index]
    
    def __len__(self): 
        return self.rows_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.rows_len} Rows x {self.cols_len} Columns, items: {str(self)}'

    def __eq__(self, other: object) -> bool: 
        if not isinstance(other, Array2D):
            return False
        if self.rows_len != len(other):
            return False
        if self.cols_len != len(other[0]):
            return False
        for r in range(len(other)):
            for c in range(len(other[0])):
                if self[r][c] != other[r][c]:
                    return False
        return True


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')