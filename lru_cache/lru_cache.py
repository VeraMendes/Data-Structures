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

        # self.limit = limit
        ## self.size = 0
        # self.order = DoublyLinkedList()
        # self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):

        # if doesn't exist in cache
        if key not in self.storage:
            return None
        else:
            # key is in cache
            # move to end of list to be considered most recently used
            node = self.storage[key]
            self.cache.move_to_front(node)
            # retrieve value for respective key
            return node.value[1]

        # # key is not in cache - return none
        # if key not in self.storage:
        #     return None
        # else:
        #     # key is in cache
        #     # move it to most recently used
        #     node = self.storage[key]
        #     self.order.move_to_end(node)
        #     # return value
        #     return node.value[1]
     
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

        # if key exists
        if key in self.storage:
            # overwrite the value
            node = self.storage[key]
            node.value = (key, value)
            # move to the head (most recently used)
            self.cache.move_to_front(node)
            return
        
        # size is at max limit
        if self.current == self.max:
            # evict the oldest one
            key_of_oldest = self.cache.tail.value[0]
            del self.storage[key_of_oldest]
            self.cache.remove_from_tail()
            # update current number of nodes that is holding
            self.current -= 1

        # add to cache
        self.cache.add_to_head((key, value))
        # update current number of nodes that is holding
        self.current += 1
        # add it to storage
        self.storage[key] = self.cache.head


        # # if item/key already exists
        # if key in self.storage:
        #     # overwrite the value
        #     # where is the value stored?
        #     node = self.storage[key]
        #     node.value = (key,value)
        #     # move to the tail (most recently used)
        #     self.order.move_to_end(node)
        #     return

        #  # size is at limit
        # if len(self.order) == self.limit:
        #     # evict the oldest one
        #     index_of_oldest = self.order.head.value[0]
        #     del self.storage[index_of_oldest]
        #     self.order.remove_from_head()

        
        # # add to order
        # self.order.add_to_tail((key,value))
        # # add it to storage
        # self.storage[key] = self.order.tail
