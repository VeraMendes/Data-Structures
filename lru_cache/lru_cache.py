import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.max = limit
        self.current = 0
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if doesn't exist in the storage
        if key not in self.storage:
            return None
        else:
            # move to end of list to be considered most recently used
            node = self.storage[key]
            self.cache.move_to_end(node)
            # retrieve value for key
            return node.value
     
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        value = self.storage[key]
        if key in self.storage:
            self.cache.delete(value)
            # self.storage.get(key)
            # self.storage.update(value)
            self.current -= 1
        
        if self.current <= self.max:
            self.cache.add_to_tail(value)
            value = self.cache_list.tail
            self.current += 1

        if self.current > self.max:
            self.cache.remove_from_head(value)
            self.current -= 1
            self.cache.add_to_tail(value)
            self.current += 1

            # remove_key = list(self.cache.head.value.keys())[-1]
            # del self.storage[remove_key]
            # self.cache.delete(self.cache[-1])

        # if key in self.storage:
        #     self.get()

        # if self.current > self.max:
        #     self.cache.remove_from_head()
        #     self.cache.add_to_tail({key:value})

        # elif self.current <= self.max:
        #     self.cache.add_to_tail({key:value})
        #     self.current += 1
        #     self.storage[key] = value

        # if self.cache.get(key) is None:
        #     if self.current > self.max:
        #         prev_node = self.cache.remove_from_head()
        #         prev_key = list(prev_node)[-1]
        #         del self.cache[prev_key]
        #     self.cache.add_to_tail({key:value})
        #     new_node = self.tail
        #     self.cache[key] = new_node

        # else:
        #     node = self.cache[key]
        #     node.value.update({key:value})
        #     self.cache.move_to_end(node)

        # for key, value in self.storage.items():
