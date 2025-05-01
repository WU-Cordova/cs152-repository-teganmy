import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT, VT]]] = \
            Array(starting_sequence = [LinkedList(data_type = tuple) for _ in range (number_of_buckets)], 
                data_type = LinkedList)
        
        self._count: int = 0
        self._load_factor: float = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function

    def _get_bucket_index(self, key: KT, bucket_size: int) -> int:
        bucket_index = self._hash_function(key)
        return bucket_index % bucket_size

    def __getitem__(self, key: KT) -> VT:
        for (k, v) in self._buckets[self._get_bucket_index(key, len(self._buckets))]:
            if k == key:
                return v
        raise KeyError(f"{key} not found in hashmap.")

    def _resize(self) -> None:
        next_size = self._next_prime(len(self._buckets) * 2)
        new = Array(starting_sequence = [LinkedList(data_type = tuple) for _ in range (next_size)], 
                data_type = LinkedList)
        for bucket in self._buckets:
            current = bucket.head
            while current:
                key, value = current.data
                bucket_index = self._get_bucket_index(key, next_size)
                new[bucket_index].append((key, value))
                current = current.next
        
        self._buckets = new

    def _next_prime(self, n: int) -> int:
        def is_prime(num: int, check: int = 2) -> bool:
            if num < 2:
                return False
            if check * check > num:
                return True
            if num % check == 0:
                return False

            return is_prime(num, check + 1)

        while not is_prime(n):
            n += 1
        return n

    def __setitem__(self, key: KT, value: VT) -> None:
        if self._count / len(self._buckets) >= self._load_factor:
            self._resize()
        
        bucket_index = self._get_bucket_index(key, len(self._buckets))
        bucket = self._buckets[bucket_index]
        for item in bucket:
            if item[0] == key:
                bucket.insert_after(item, (key, value))
                bucket.remove(item)
        bucket.append((key, value))
        self._count += 1

    def keys(self) -> Iterator[KT]:
        for bucket in self._buckets:
            current = bucket.head
            while current:
                key, _ = current.data
                yield key
                current = current.next
        
    def values(self) -> Iterator[VT]:
        for bucket in self._buckets:
            current = bucket.head
            while current:
                _, value = current.data
                yield value
                current = current.next

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for bucket in self._buckets:
            current = bucket.head
            while current:
                key, value = current.data
                yield (key, value)
                current = current.next
            
    def __delitem__(self, key: KT) -> None:
        bucket_index: int = self._get_bucket_index(key, len(self._buckets))
        bucket_chain: LinkedList = self._buckets[bucket_index]

        for (k, v) in bucket_chain:
            if k == key:
                bucket_chain.remove((k, v))
                self._count -= 1
                return
        raise KeyError(f"{key} not found in hashmap.")

    
    def __contains__(self, key: KT) -> bool:
        bucket_index: int = self._get_bucket_index(key, len(self._buckets))
        bucket_chain: LinkedList = self._buckets[bucket_index]

        for (k, v) in bucket_chain:
            if k == key:
                return True

        return False
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        return iter(self.keys()) 
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("HashMap.__eq__() is not implemented yet.")

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)