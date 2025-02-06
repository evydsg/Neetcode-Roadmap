```md
# 304. Range Sum Query 2D - Immutable

**Difficulty:** Medium  
**Topics:** Prefix Sum, 2D Array  
**Companies:** Various  

---

## **Problem Statement**

Given a 2D matrix `matrix`, handle multiple queries of the following type:

- **Calculate the sum** of the elements inside the rectangle defined by its upper-left corner `(row1, col1)` and lower-right corner `(row2, col2)`.

### **Implement the `NumMatrix` Class**
- `NumMatrix(int[][] matrix)`: Initializes the object with the integer matrix `matrix`.
- `int sumRegion(int row1, int col1, int row2, int col2)`: Returns the sum of elements in the defined rectangle.

**Requirement:**  
- The `sumRegion` function **must run in O(1) time complexity**.

---

## **Example 1**

### **Input**
```plaintext
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
```

### **Output**
```plaintext
[null, 8, 11, 12]
```

### **Explanation**
```java
NumMatrix numMatrix = new NumMatrix([
    [3, 0, 1, 4, 2], 
    [5, 6, 3, 2, 1], 
    [1, 2, 0, 1, 5], 
    [4, 1, 0, 1, 7], 
    [1, 0, 3, 0, 5]
]);

numMatrix.sumRegion(2, 1, 4, 3); // returns 8 (sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // returns 11 (sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // returns 12 (sum of the blue rectangle)
```
