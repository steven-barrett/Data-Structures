import collections

"""
Decided to put in some notes as to why I used an ordered dictionary instead of doubly linked list:

 The implementation is much cleaner as the order is handled by the OrderDict now. For each get and set operation,
 we first pop the item, then put back to update its timestamp. The element in the head of sequence is the least used item, 
 so it's the candidate to expire if the maximum capacity is reached. This is where I did my research on ordereddict...
 https://www.geeksforgeeks.org/ordereddict-in-python/
"""

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.capacity = limit
        self.size = 0
        self.cache = collections.OrderedDict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return None

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
        try:
            self.size += 1
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
                self.size = self.capacity
        self.cache[key] = value

    # Test if adding a new one acts like it should (removing the least recently used)
    def displayContents(self):
        for k in self.cache:
            print(self.cache[k])


cache = LRUCache(10)

cache.set('1', 10)
cache.set('2', 20)
cache.set('3', 30)
cache.set('4', 40)
cache.set('5', 50)
cache.set('6', 60)
cache.set('7', 70)
cache.set('8', 80)
cache.set('9', 90)
cache.set('10', 100)

# Add one more item than the cache can hold to see if it functions correctly
cache.set('11', 110)

# Display all the values to see the results
print(cache.displayContents())
print('Total items in cache: ', cache.size)
