import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # in stack, we always add to the tail
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        # checking for cases where there is no elements in the stack
        if self.size == 0:
            return None
        # when removing from stack, remove from tail
        else:
            prev = self.storage.tail.value
            self.storage.remove_from_tail()
            self.size -= 1
            return prev

    def len(self):
        # size of stack
        return self.size
