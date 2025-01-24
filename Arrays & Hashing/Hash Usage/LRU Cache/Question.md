# 146. LRU Cache

**Difficulty:** Medium  
**Topics:** Design, Data Structures  

---

## Problem Statement

Design a data structure that follows the constraints of a **Least Recently Used (LRU)** cache.

### Class Definition
Implement the `LRUCache` class:

1. **`LRUCache(int capacity)`**  
   - Initialize the LRU cache with a positive size `capacity`.

2. **`int get(int key)`**  
   - Return the value of the `key` if the key exists, otherwise return `-1`.

3. **`void put(int key, int value)`**  
   - Update the value of the `key` if it exists.  
   - Otherwise, add the key-value pair to the cache.  
   - If the number of keys exceeds the cache capacity, evict the **least recently used (LRU)** key.

### Constraints
- Both `get` and `put` must run in **O(1)** average time complexity.

---

## Examples

### Example 1
**Input:**  
```plaintext
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
