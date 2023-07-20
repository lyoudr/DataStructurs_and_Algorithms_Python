# Instead of 
# O(n) recursive calls
# each of wich runs in O(n) time
# overall running time is O(n2)

# 3.2 The Seven Functions Used in This Book
# 1. The Constant Function
# f(n) = c

# 2. The Logarithm Function
# f(n) = logb n

# 3. The Linear Function
# f(n) = n

# a. Find Maxf
def find_max(data):
    ''' Return the maximum element from a nonempty Python list.'''
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val 
    return biggest

# execute c' + c''* n times , so this algorithm runs O(n) times

# b. Prefix Average
# A Quadratic-Time Algorithm
def prefix_average1(S): # O(n2)
    '''Return list such taht, for all j, A[j] equals average of S[0], ..., S[j].'''
    n = len(S)                         # constant time
    A = [0] * n                        # O(n) time
    for j in range(n):                 # O(n) time => n times, for i = 0, ..., n - 1
        total = 0                      # begin computing S[0] + ... + S[j]
        for i in range(j + 1):         # O(n2) time => 1 + 2 + 3 + ... + n = n(n + 1) / 2 = O(n2)
            total += S[i]
        A[j] = total / (j + 1)         # record the average
    return A


def prefix_average2(S): # O(n2)
    '''Return list such that, for all j, A[j] equals average of S[0], ..., S[j].'''
    n = len(S)
    A = [0] * n                           # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j + 1]) / (j + 1)  # record the average 
        # we use sum(S[0: j + 1]) to compute the partial sum, S[0] + ... + S[j]
    return A 

# A Linear-Time Algorithm
def prefix_average3(S): # O(n)
    '''Return list such that, for all j, A[j] equals average of S[0], ..., S[j].'''
    n = len(S)                            # O(1) time
    A = [0] * n                           # O(n) time, create new list of n zeros
    total = 0
    for j in range(n) :                   # O(n) time
        total += S[j]                     # update prefix sum to include S[j]
        A[j] = total / (j + 1)            # compute average based on current sum
    return A

# Three-Way Set Disjointness
def disjoint1(A, B, C):
    '''Return True if there is no element common to all three lists.'''
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False          # we found a common value
    return True

# This simple algorithm loops through each possible triple of values from the three sets to see if 
# those values are equivalent.
# If each of the original sets has size n, then the worst-case running time of this function is O(n3)

def disjoint2(A, B, C):
    '''Return True if there is no element common to all three lists.'''
    for a in A:                             # O(n) time
        for b in B:                         # O(n2) time
            if a == b:                      # only check C if we found match from A and B
                for c in C:
                    if a == c:              # (and thus a == b == c)
                        return False        # we found a common value
    return True                             # if we reach this, sets are disjoint

### Element Uniqueness
# A problem that is closely related to the three-way set disjointness problem is the "element uniqueness problem"
# In the element uniqueness problem, we are given a single sequence S with n elements and asked whether all elements of that collections are distinct from each other.
def unique1(S): # O(n2)
    '''Return True if there are no duplicate elements in sequence S.'''
    for j in range(len(S)):
        for k in range(j + 1, len(S)) :
            if S[j] == S[k]:
                return False                 # found duplicate pair
    return True                              # if we reach this, elements were unique

# Using Sorting as a Problem-Solving Tool
# An even better algorithm for the element uniqueness problem is based on using sorting as a problem-solving tool.
# by sorting of elements, we are guaranteed that any duplicate elements will be placed next to each other.
# Thus, to determine if there are any duplicates, all we need to do is perform a single pass over the sorted sequence

def unique2(S): # O(nlogn)
    '''Return True if there are no duplicate elements in sequence S.'''
    temp = sorted(S)                          # O(nlogn)
    for j in range(1, len(temp)):             # O(n)
        if temp[j - 1] == temp[j]:
            return False
    return True

# 3.4.2 The "Contra" Attack

# 1. Contrapositive (反證法)
# if p is true, then q is true
# if q is not true, then p is not true

# Example: Let a and b be integers. If ab is even, then a is even or b is even.
# Justification: If a is odd and b is odd, then ab is odd

# 2. Contradiction (矛盾)
# q is true
# supposing that "q is false" and then showing that this assumpmtion leads to a contradiction

# Example: Let a and b be integers. If ab is odd, then a is odd and b is odd.
# Justification: suppose "a is even" or "b is even". 

# a = 2j 
# ab = (2j)b = 2(jb), that is, ab is even.

# 3.4.3 Induction and Loop Invariants
# integer parameter "n" (usually denoting an intuitive notion of the "size" of the problem)
# Induction n >= 1, there is finite sequence of implications that starts with something known to be true and ultimately leads to showing that q(n) is true.
# if q(j) is true for all j < n, then q(n) is true.

# Fibonacci function F(n)
# F(1) = 1 < 2 = 2的1次方
# F(2) = 2 < 4 = 2的2次方
# F(n) = F(n - 2) + F(n - 1) for n > 2

# Base case: (n <= 2). F(1) = 1, F(2) = 2
# Induction step: (n > 2). F(n) = F(n − 2) + F(n − 1). Moreover, since both n - 2 and n - 1 are less than n,
# F(n) < 2的n-2次方 + 2的n-1次方
# we can apply the inductive assumption (sometimes called the "inductive hypothesis")

# Loop Invariants
# finds the smallest index at which element val occurs in sequence S.
def find(S, val):
    '''Return index j such that S[j] == val, or -1 if no such element.'''
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j                # a match was found at index j
        j += 1
    return -1
