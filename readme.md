# 🚀 Radix Sort & Counting Sort Implementation with Performance Optimization

This repository contains a bottom-up implementation and optimization of **Radix Sort** built upon a simple stable **Counting Sort** algorithm in Python. 

Rather than just writing a working script, this project focuses on iterative code refactoring to eliminate dynamic memory allocation overhead and redundant string-reversal operations.

---

## 📌 Key Implementation Features

### 1. Guaranteed Stable Sort
* During the digit-wise Counting Sort phase, the algorithm traverses the array in **reverse order (`range(len - 1, -1, -1)`)**. This preserves the original relative order of duplicate elements, perfectly meeting the criteria for a Stable Sort.

### 2. Readability & Memory Optimization
* **In-place Prefix Sum:** The cumulative sum is computed directly inside the existing count array (`corrent`), minimizing extra variable overhead.
* **Pre-allocated Arrays:** To avoid Python's dynamic memory reallocation overhead caused by repeated `.append()`, the output array is pre-allocated (`[0] * len(lists)`) and populated via direct index mapping (Random Access).

### 3. Redundant Operation Elimination (Digit Caching)
* In standard implementations, numbers are repeatedly converted to strings and reversed (`sapart`) for every single digit place (1s, 10s, 100s...).
* To resolve this performance bottleneck, the final optimized version parses the digits **exactly once** at the beginning and manages data as **`(original_number, digit_list)` tuples (Pairs)** throughout the entire sorting lifecycle.

---

## 🛠️ Code Structure & Files

### 1. `radix_sort.py` (Final Optimized Version)
The complete Radix Sort algorithm that utilizes the `Pair` pattern to cache digit extractions and maximize time complexity efficiency.

```python
# Counting Sort per individual digit place (1s, 10s, 100s...)
def counting_sort_by_digit(pairs, digit_index):
    corrent = [0] * 10

    # 1. Count frequencies using the pre-cached digit lists
    for num, tlist in pairs:
        digit = tlist[digit_index] if digit_index < len(tlist) else 0
        corrent[digit] += 1

    # 2. In-place Prefix Sum calculation
    for i in range(1, len(corrent)):
        corrent[i] += corrent[i - 1]

    # 3. Pre-allocate array and sort backwards to maintain stability
    sorted_pairs = [0] * len(pairs)
    for i in range(len(pairs) - 1, -1, -1):
        num, tlist = pairs[i]
        digit = tlist[digit_index] if digit_index < len(tlist) else 0
        corrent[digit] -= 1
        sorted_pairs[corrent[digit]] = (num, tlist)

    return sorted_pairs
