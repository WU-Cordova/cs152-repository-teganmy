from typing import Iterable, Optional
from datastructures.ibag import IBag, T

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.__bag: dict[T, int] = {}
        if items: 
            for item in items:
                self.add(item)

    def add(self, item: T) -> None:
        if item == None: 
            raise TypeError("Cannot add None type")
        elif item in self.__bag:
            self.__bag[item] += 1
        else:
            self.__bag[item] = 1
                 
    def remove(self, item: T) -> None:
        if item not in self.__bag:
            raise ValueError("Item not in bag")
        elif item in self.__bag:
            if self.__bag[item] > 1:
                self.__bag[item] -= 1
            else:
                self.__bag.pop(item)

    def count(self, item: T) -> int:
        if item == None: 
            raise ValueError("Cannot remove None type")
        elif not(item in self.__bag):
            count = 0
        else:
            count = self.__bag.get(item)
        return count

    def __len__(self) -> int:
        length = 0
        for item in self.__bag:
            length += self.count(item)
        return length

    def distinct_items(self) -> Iterable[T]:
        distinct = set()
        for item in self.__bag:
            distinct.add(item)
        return distinct

        def __str__(self, distinct) -> str:
            return ', '.join(str([item for items in distinct]))

    def __contains__(self, item) -> bool:
        return item in self.__bag

    def clear(self) -> None:
        self.__bag.clear()
        