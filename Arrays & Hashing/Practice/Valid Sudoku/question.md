
# **Valid Sudoku**
**Solved** ✅

## **Problem Statement**
You are given a **9 x 9** Sudoku board `board`. A Sudoku board is valid if the following rules are followed:

1. Each **row** must contain the digits **1-9** without duplicates.
2. Each **column** must contain the digits **1-9** without duplicates.
3. Each of the nine **3 x 3** sub-boxes of the grid must contain the digits **1-9** without duplicates.

Return `true` if the Sudoku board is valid, otherwise return `false`.

**Note:** A board does not need to be full or be solvable to be valid.

---

## **Example 1**
### **Input:**
```python
board = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]
```
### **Output:**
```python
True
```

---

## **Example 2**
### **Input:**
```python
board = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]
```
### **Output:**
```python
False
```
### **Explanation:**
There are two `'1'`s in the **top-left 3x3 sub-box**, making the board invalid.
