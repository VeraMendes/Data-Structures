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

        # if self.node is None:
        #     return
        # if there is a left, go there and print it
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        # then go right and recurse
        if node.right:
            self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        # create queue
        bft_queue = Queue()
        # add root to queue
        bft_queue.enqueue(node)
        # while queue is not empty
        while bft_queue.len() > 0:
        # node = pop head of queue
            temp = bft_queue.dequeue()
            # DO THE THING!!! (print)
            print(temp.value)
            # add children of node to queue
            if temp.left:
                bft_queue.enqueue(temp.left)
            if temp.right:
                bft_queue.enqueue(temp.right)

        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
  
        # create stack
        dft_stack = Stack()
        # add root to stack
        dft_stack.push(node)
        # while stack is not empty
        while dft_stack.len() > 0:
            # node = pop top of stack
            temp = dft_stack.pop()
            # DO THE THING!!! (print)
            print(temp.value)
            # add children of node to stack
            if temp.left:
                dft_stack.push(temp.left)
            if temp.right:
                dft_stack.push(temp.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):

        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        # then go right and recurse
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        if node.left:
            self.post_order_dft(node.left)
        # then go right and recurse
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
