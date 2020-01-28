from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if (value < self.value):
            if (not self.left):
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

        # Return True if the tree contains the value
        # False if it does not
    def contains(self, target):
        if (self.value == target):
            return True

        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        bft = Queue()
        bft.enqueue(node)
        while bft:
            item = bft.dequeue()
            if (not item):
                break
            print(item.value)
            if (item.left):
                bft.enqueue(item.left)
            if (item.right):
                bft.enqueue(item.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        dft = Stack()
        dft.push(node)
        while dft:
            item = dft.pop()
            if (not item):
                break
            print(item.value)
            if (item.left):
                dft.push(item.left)
            if (item.right):
                dft.push(item.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)


def cb(value):
    print(value)


BST = BinarySearchTree(20)
BST.insert(50)
BST.insert(11)
BST.insert(42)
BST.insert(9)
BST.insert(16)
BST.insert(10)
BST.insert(15)
BST.insert(4)
BST.insert(3)
BST.insert(0)
BST.bft_print(BST)

print("START TEST")
print(BST.get_max())
print(BST.contains(6))
print(BST.for_each(cb))
print("END TEST")
