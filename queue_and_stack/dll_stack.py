from doubly_linked_list import Doubly_Linked_List
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = Doubly_Linked_List()
        # self.storage.__init__()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if(self.size > 0):
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.storage.__len__()


#  follows the LIFO rule of stacks
stack = Stack()
stack.push(0)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
print(stack.storage.head.value)
