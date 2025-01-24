class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = {} #map key to nodes
        self.size = 0

        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        

    def get(self, key: int) -> int:
        if key in self.dictionary:
            return self.dictionary[key].val
        
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary[key] = value
            return
        else:
            if self.capacity == len(self.dictionary):

                