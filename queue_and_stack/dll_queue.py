from doubly_linked_list import Doubly_Linked_List
import sys
sys.path.append('../doubly_linked_list.py')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = Doubly_Linked_List()
        # self.storage.__init__()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if (self.size > 0):
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.storage.length



test = Queue()
test.enqueue(5)
test.enqueue(6)
test.enqueue(7)
print(test.len())
