class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity #Store capacity
        self.dictionary = {} #map key to nodes
        

        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    #Remove from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next , nxt.prev = next, prev

    #Insert node at the right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.dictionary:
            self.remove(self.dictionary[key])
            self.insert(self.dictionary[key])

            return self.dictionary[key].val
        
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.remove(self.dictionary[key])
            
        self.dictionary[key] = Node(key, value)
        self.insert(self.dictionary[key])
            
     
        if self.capacity >= len(self.dictionary):
            #remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.dictionary[lru.key]

                