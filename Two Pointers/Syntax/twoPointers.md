# Two Pointers Technique

## Concept
The **Two Pointers** technique involves using two pointers, **L (left)** and **R (right)**, to traverse an array. These pointers can start at various positions depending on the problem.

- Typically, **L** starts at index `0`, and **R** starts at index `arr.length - 1`.
- The pointers move towards each other, adjusting based on given conditions.
- This technique is often used in problems like **palindromes**, **target sum**, and **sorted array operations**.

### Comparison with Sliding Window
- The **sliding window** technique is a variation of two pointers where the window expands or contracts.
- In **two pointers**, the movement of `L` and `R` is usually based on conditions like value comparison or target matching.

---

## 1. Checking if a String is a Palindrome
A **palindrome** is a sequence that reads the same forwards and backwards.  
Using the **two pointers** approach:

### Algorithm
1. Start **L** at index `0` and **R** at index `word.length - 1`.
2. Compare the characters at **L** and **R**:
   - If they are not equal, return `False`.
   - Otherwise, move **L** forward and **R** backward.
3. Repeat until **L** meets **R**.
4. If all pairs match, return `True`.

### Code Implementation
```python
def isPalindrome(word):
    L, R = 0, len(word) - 1
    while L < R:
        if word[L] != word[R]:
            return False
        L += 1
        R -= 1
    return True
```

### Time Complexity
- **O(n)**, where `n` is the length of the string.
- Each character is visited only once.

---

## 2. Finding Two Numbers that Sum to a Target
### Problem
Given a **sorted** array, find two indices whose values sum to a given `target`.  
*Assumption:* There is exactly one valid pair.

### Naïve Approach
- Check every pair of numbers (`O(n²)` time complexity).

### Optimized Two Pointers Approach
1. Start **L** at index `0` and **R** at index `arr.length - 1`.
2. Compute the sum of `nums[L] + nums[R]`:
   - If **sum is too large**, decrement `R` to reduce it.
   - If **sum is too small**, increment `L` to increase it.
   - If the **sum matches the target**, return `[L, R]`.
3. Repeat until **L meets R**.

### Code Implementation
```python
def targetSum(nums, target):
    L, R = 0, len(nums) - 1
    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            return [L, R]
```

### Why Does This Work?
- Since the array is **sorted**, reducing `R` ensures we move to smaller numbers, and increasing `L` moves to larger numbers.
- This **guarantees** that we will find the correct pair in `O(n)` time.

### Time Complexity
- **O(n)**, since each element is checked at most once.

---

## Key Takeaways
✔ The **Two Pointers** technique efficiently solves problems by moving pointers based on conditions.  
✔ It works best with **sorted arrays** and problems involving **comparisons**.  
✔ Typical problems include:
  - **Palindrome checking**
  - **Target sum**
  - **Merging sorted arrays**
  - **Removing duplicates in-place**
  - **Finding closest pair in a sorted array**
