import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # in queue, we always add to the tail
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        # checking for cases where there is no elements in the queue
        if self.size == 0:
            return None
        # when removing from queue, remove from head
        else:
            next = self.storage.head.value
            self.storage.remove_from_head()
            self.size -= 1
            return next

    def len(self):
        # size of queue
        return self.size
