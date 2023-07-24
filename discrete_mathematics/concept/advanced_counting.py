### Divide-and-Conquer Recurrence Relations
"""
1. a recursive algorithm divides a problem of size n into a subproblems, where each subproblem is of size n/b
2. suppose that a total of g(n) extra operations are required in the conquer step of the algorithm to combine the solutions of the subproblems into a solution of the original problem
    f(n) = af(n/b) + g(n)
"""

# 1. Binary Search
"""
    size n sequence
    f(n) = f(n/2) + 2
"""

# 2.Finding the Maximum and Minimum of a Sequence
"""
    f(n) = 2f(n/2) + 2
"""
def find_max(S):
    if len(S) < 2:
        return S[0]
    else:
        mid = len(S) // 2
        return (max(find_max(S[:mid]), find_max(S[mid:])))

# 3. Merge Sort O(nLogn)
"""
    M(n) = 2M(n/2) + n
"""
def merge(L, R, S):
    i = j = 0
    while i + j < len(S):
        if j == len(R) or (i < len(L) and L[i] < R[j]):
            S[i+j] = L[i]
            i += 1
        else:
            S[i+j] = R[j]
            j += 1

def merge_sort(S):
    l = len(S)
    if l < 2: return
    # divide
    mid = l // 2
    L = S[:mid]
    R = S[mid:]

    merge_sort(L)
    merge_sort(R)

    # conquer
    merge(L, R, S)
    return S

# 4. Fast Multiplication of Integers
"""
1. This fast multiplication algorithm proceeds by splitting each of two 2n-bit integers into two blocks, each with n bits.
    f(2n) = 3f(n) + Cn
"""

# 5. Fast Matrix Multiplication
"""
    f(n) = 7f(n/2) + 15n2/4
    f(n) = af(n/b) + g(n)
         = a2f(n/b2) + ag(n/b) + g(n)
"""