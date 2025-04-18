from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.data_type = data_type
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.size = 0

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        if not isinstance(sequence, Sequence):
            raise ValueError('starting_sequence must be a valid sequence type')
        linked_list: LinkedList[T] = LinkedList(data_type = data_type)
        for item in sequence:
            if not isinstance(item, data_type):
                raise TypeError("Item is not the correct type.")
            linked_list.append(item)
        return linked_list
        

    def append(self, item: T) -> None:
        if not isinstance(item, self.data_type):
                raise TypeError("Item is not the correct type.")
        new_node: LinkedList.Node = LinkedList.Node(data=item)

        if self.empty:
            self.head = self.tail = new_node

        else:
            if self.tail:
                self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self.size += 1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self.data_type):
                raise TypeError("Item is not the correct type.")
        new_node: LinkedList.Node = LinkedList.Node(data=item)

        if self.empty:
            self.head = self.tail = new_node

        else:
            if self.head:
                self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def insert_before(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type):
            raise TypeError("Items are not the same type.")
        if not isinstance(item, self.data_type):
            raise TypeError("Items are not the same type.")
        if self.head and self.head.data == target:
            self.prepend(item)
            return

        travel = self.head

        while travel: #while travel is not None
            if travel.data == target:
                break
            travel = travel.next
        
        if travel is None:
            raise ValueError(f"The target item {target} is not in the linked list.")
        
        new_node: LinkedList.Node = LinkedList.Node(data=item)
        #new_node.previous = .previous
        travel.previous.next = new_node
        new_node.next = travel
        travel.previous = new_node
        self.size += 1


    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type):
            raise TypeError("Items are not the same type.")
        if not isinstance(item, self.data_type):
            raise TypeError("Items are not the same type.")
        if self.tail and self.tail.data == target:
            self.append(item)
        
        travel = self.head

        while travel: #while travel is not None
            if travel.data == target:
                break
            travel = travel.next
        
        if travel is None:
            raise ValueError(f"The target item {target} is not in the linked list.")

        new_node: LinkedList.Node = LinkedList.Node(data=item)
        new_node.next = travel.next
        new_node.previous = travel

        if travel.next:
             travel.next.previous = new_node
        else:
            self.tail = new_node
        
        travel.next = new_node

        self.size += 1

    def remove(self, item: T) -> None:
        if self.empty:
            raise IndexError("The linked list is empty.")
        if not isinstance(item, self.data_type):
            raise TypeError("Items are not the same type.")

        travel = self.head

        while travel: #while travel is not None
            if travel.data == item:
                break
            travel = travel.next
        
        if travel is None:
            raise ValueError(f"The item {item} is not in the linked list.")

        travel.previous.next = travel.next
        travel.next.previous = travel.previous

        self.size -= 1


    def remove_all(self, item: T) -> None:
        if self.empty:
            raise IndexError("The linked list is empty.")
        if not isinstance(item, self.data_type):
            raise TypeError("Item is not the correct type.")

        travel = self.head
        while travel:
            next_node = travel.next
            if travel.data == item:
                if travel is self.head:
                    self.head = travel.next
                    self.head.previous = None
                if travel is self.tail:
                    self.tail = travel.previous
                    self.tail.next = None
                else:
                    travel.previous.next = travel.next
                    travel.next.previous = travel.previous
                self.size -= 1
            travel = travel.next

    def pop(self) -> T:
        if self.empty:
            raise IndexError("The linked list is empty.")
        data = self.tail.data
        if self.head is self.tail:
            self.head = self.tail = None
        self.tail = self.tail.previous
        self.size -= 1
        return data

    def pop_front(self) -> T:
        if self.empty:
            raise IndexError("The linked list is empty.")
        data = self.head.data
        if self.head is self.tail:
            self.head = self.tail = None
        self.head = self.head.next
        self.size -= 1
        return data

    @property
    def front(self) -> T:
        if not self.head or self.size == 0:
            raise IndexError("The linked list is empty.")
        return self.head.data

    @property
    def back(self) -> T:
        if not self.tail or self.size == 0:
            raise IndexError("The linked list is empty.")
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None and self.tail is None and self.size == 0

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        self.size = 0
        self.head = self.tail = None

    def __contains__(self, item: T) -> bool:
        if not isinstance(item, self.data_type):
            raise TypeError("Item is not the correct type.")
        travel = self.head

        while travel: #while travel is not None
            if travel.data == item:
                break
            travel = travel.next
        
        if travel is None:
            return False
        
        return True

    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self
        

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration

        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        travel = self.tail
        while travel:
            yield travel.data
            travel = travel.previous
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if self.size != len(other):
            return False
        self_travel = self.head
        other_travel = other.head

        while self_travel and other_travel: #while travel is not None
            if self_travel.data != other_travel.data:
                return False
            self_travel = self_travel.next
            other_travel = other_travel.next
        
        return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.size}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
