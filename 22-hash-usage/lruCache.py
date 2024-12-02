# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations
# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value cooresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
# If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
# A key is considered used if a get or a put operation is called on it.
# Ensure that get and put each run in O(1)O(1) average time complexity.

class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value 
        self.prev = self.next = None 

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = dict() # map key to node 
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    # remove node from the list 
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev
        # pass 

    # insert node at the right 
    def insert(self, node ):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node 
        node.next, node.prev = nxt, prev 
        # pass 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val 
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete LRU from the cache
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]

        