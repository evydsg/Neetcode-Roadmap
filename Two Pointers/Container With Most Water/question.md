# 🧊 Container With Most Water

You are given an integer array `height` where `height[i]` represents the height of the *i<sup>th</sup>* bar.

You may choose any two bars to form a container. Return the **maximum amount of water** a container can store.

## 🧠 Intuition

The amount of water a container can store is determined by the **shorter** of the two bars multiplied by the **distance** between them. So we want to maximize:

```
water = min(height[i], height[j]) * (j - i)
```

## 🔍 Examples

### Example 1:

**Input:**
```
height = [1, 7, 2, 5, 4, 7, 3, 6]
```

**Output:**
```
36
```

### Example 2:

**Input:**
```
height = [2, 2, 2]
```

**Output:**
```
4
```

## ✅ Constraints

- `2 <= height.length <= 10⁵`
- `0 <= height[i] <= 10⁴`


