from typing import List
### Search Algorithm

# O(n)
def linear_search(x: int, arr: List):
    for index, e in enumerate(arr):
        if e == x:
            return index
    return None

# O(logn)
def binary_search(x: int, arr: List):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] == x:
            return m
        else:
            if arr[m] > x:
                r = m - 1  
            else:
                l = m + 1
    return 0

