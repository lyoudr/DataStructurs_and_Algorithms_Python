### ALGORITHM 4 The bubble sort
"""
procedure bubblesort(a1, ..., an: real numbers with n >= 2)
for i := 1 to n-1
    for j := 1 to n-i
        if aj > aj+1 then interchange aj and aj+1
"""

def bubblesort(S):
    for i in range(len(S)-1):
        for j in range(i, len(S)-i):
            if S[j] > S[j+1]:
                temp = S[j]
                S[j] = S[j+1]
                S[j+1] = temp 
    return S 

### ALGORITHM 5 The Insertion Sort
"""
procedure insertion_sort(a1, a2, ..., an: real number with n >= 2)
for j := 2 to n
    i := 1
    while aj > ai
        i := i + 1
    m := aj
    for k:=0 to j-i-1
        aj-k = aj-k-1
    ai := m
"""

def insertion_sort(S):
    n = len(S)
    for j in range(1, n):
        print('j is ->', j)
        i = 0
        while S[j] > S[i]:
            i += 1
            print('i,S[j],S[i] is ->', f"{i},{S[j]},{S[i]}")
        m = S[j]
        for k in range(0, j-i):
            S[j-k] = S[j-k-1]
        S[i] = m 
    return S 


### Greedy Algorithms
# This approach selects the best choice at each step, instead of considering all sequences 
# of steps that may lead to an optimal solution.
# Algorithms that make what seems to be the "best" choice at each step are called greedy algorithms

# ALGORITHM 6 Greedy Change-Making Algorithm
# Before we embark on our proof, we show that there are sets of coins 
# for which the greedy algorithm does not necessarily produce change using the fewest coins possible
# c1 = 25
# c2 = 10
# c3 = 5
# c4 = 1
"""
procedure change(c1, c2, ..., cr: values of denominations of coins, where c1 > c2 > ... > cr; n: a positive integer)
    for i := 1 to r
        di := 0 {di counts the coins of denomination ci used}
        while n >= ci
            di := di + 1 {add a coin of denomination ci}
            n := n - ci
"""
def coin_change(coins: list, n: int):
    record = {str(k): 0 for k in coins}
    for i in range(0, len(coins)):
        while n >= coins[i]:
            record[str(coins[i])] += 1
            n -= coins[i]
    return record 

# ALGORITHM 7 Greedy Algorithm for Scheduling Talks.
"""
procedure schedule(s1 <= s2 <= ... <= sn: start times of talks, e1 <= e2 <= ... <= en: ending time of talks)
    S := ∅
    for j:= 1 to n
        if talk j is compatiable with S then 
        S := S U {talk j}
    return S{S is the set of talks scheduled}
"""
