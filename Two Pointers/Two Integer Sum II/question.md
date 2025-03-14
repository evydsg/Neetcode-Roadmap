
# Two Integer Sum II

## Problem Statement

Given an array of integers `numbers` that is **sorted in non-decreasing order**, find **two distinct numbers** that add up to a given `target`.

Return the indices **(1-based indexing)** of these two numbers as `[index1, index2]`, ensuring that `index1 < index2`.  
Each input has exactly **one valid solution**, and the same element cannot be used twice.

Your solution must use **O(1) additional space**.

## Example

### Example 1

**Input:**
```plaintext
numbers = [1, 2, 3, 4]
target = 3
```

**Output:**
```plaintext
[1, 2]
```

**Explanation:**
The sum of `1` and `2` is `3`. Since the array is **1-indexed**, `index1 = 1`, `index2 = 2`.  
We return `[1, 2]`.

## Constraints
- `2 <= numbers.length <= 10^4`
- `-10^9 <= numbers[i] <= 10^9`
- `numbers` is sorted in non-decreasing order.
- There is exactly **one** valid solution.