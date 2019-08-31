"""
LRU Cache
"""

from collections import deque
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cap = capacity
        self.cache = dict()
        self.cache_order = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key is None:
            return -1
        return self.cache.get(key, -1)

    def set(self, key, value):
        if (self.cap==0):
            print("Can't perform operations on 0 capacity cache")
            return
        if len(self.cache_order) >= self.cap:
            del self.cache[self.cache_order.popleft()]
        self.cache_order.append(key)
        self.cache[key] = value


#Test Case 1
print("Test Case 1")
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns 3 because the cache reached it's capacity and 3 was the least recently used entry


#Test Case 2
print("Test Case 2")
our_cache2 = LRU_Cache(0)
our_cache2.set(1, 1)
# should print some warning message like "Can't perform operations on 0 capacity cache"
print(our_cache2.get(1))
# should return -1

#Test Case 3
print("Test Case 3")
our_cache3 = LRU_Cache(2)
our_cache3.set(1, 1)
our_cache3.set(2, 2)
our_cache3.set(1, 10)
print(our_cache3.get(1)) # should return 10
print(our_cache3.get(2)) # should return 2
