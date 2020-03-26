import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # bst = BinarySearchTree(new_value)

    # Insert the given value into the tree
    def insert(self, new_value):
        # check if empty
        # if empty put node here/at root
        bst = BinarySearchTree(new_value)

        # if the new value is smaller than value already on node
        if new_value < self.value:
            # go left
            # if left is a empty node
            if self.left is None:
                # leftnode.insertvalue
                self.left = bst
            else:    
                # if left not none, do the whole process of insert        
                self.left.insert(new_value)

        # if the new value is bigger or equal than value already on node
        elif new_value >= self.value:
            # go right
            # if right is a empty node
            if self.right is None:
                # rightnode.insertvalue
                self.right = bst
            else:
                # if right not none, do the whole process of insert              
                self.right.insert(new_value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        # if target is equal to value, return True
        if self.value == target:
            return True

        else:
            # if target is smaller than value
            if target < self.value:
                # go left branch
                # does left node exist?
                # if not return false
                if self.left is None:
                    return False
                else:
                    # continue looking
                    return self.left.contains(target)

            # if target is bigger or equal to value
            elif target >= self.value:
                # go right branch
                # does right node exist?
                # if not return false
                if self.right is None:
                    return False
                else:
                    # continue looking
                    return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
   
        # if there's a right:
        if self.right is None:
            # get max on right
            return self.value
        else:
            # coninue looking on the right branch
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        # apply cb to value
        cb(self.value)

        # if node exists on the left branch, apply cb for each node
        if self.right is not None:
            self.right.for_each(cb)

        # if node exists on the right branch, apply cb for each node
        if self.left is not None:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
