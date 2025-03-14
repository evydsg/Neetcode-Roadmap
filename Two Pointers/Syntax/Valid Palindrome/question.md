
# Valid Palindrome

## Problem Statement

Given a string `s`, return `true` if it is a palindrome, otherwise return `false`.

A palindrome is a string that reads the same forward and backward. It is also **case-insensitive** and **ignores all non-alphanumeric characters**.

## Examples

### Example 1

**Input:**  
```plaintext
s = "Was it a car or a cat I saw?"
```

**Output:**  
```plaintext
true
```

**Explanation:**  
After considering only alphanumeric characters, we have `"wasitacaroracatisaw"`, which is a palindrome.

---

### Example 2

**Input:**  
```plaintext
s = "tab a cat"
```

**Output:**  
```plaintext
false
```

**Explanation:**  
The filtered string is `"tabacat"`, which is **not** a palindrome.
