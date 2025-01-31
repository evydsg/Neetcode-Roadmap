class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(node):
        self.
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        