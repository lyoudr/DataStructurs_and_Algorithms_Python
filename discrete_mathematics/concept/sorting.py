from typing import List, Dict

# Bubble Sort
def bubble_sort(arr: List):           # O(n2)
    for j in range(1, len(arr)):      # O(n-1)
        i = 0
        while i + 1 <= len(arr) - 1:  # n, n-1, n-2, ..., 1
            pre = arr[i]
            nxt = arr[i+1]
            if pre > nxt:
                # change value
                arr[i+1] = pre
                arr[i] = nxt
            i += 1
    return arr


# Insertion Sort
# O(n2)
def insertion_sort(arr: List):
    sor_arr = [arr[0]]
    for e in arr[1:]:
        cur = 0
        while cur < len(sor_arr):
            if e < sor_arr[cur]:
                sor_arr.insert(cur, e)
                break
            elif cur == len(sor_arr)-1:
                sor_arr.insert(cur+1, e)
                break
            else:
                cur += 1
    return sor_arr


# Greedy Agorithm
def greedy(n: int) -> Dict:
    coins = {
        '25': 25,
        '10': 10,
        '5': 5,
        '1': 1
    }
    resp = {'25': 0, '10': 0, '5': 0, '1': 0}
    for val in coins.values():
        while n >= val:
            n = n - val
            resp[str(val)] = resp.get(str(val)) + 1
    return resp

