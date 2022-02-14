import math

### Example 1 
# Give a recursive algorithm for computing n!, where n is a nonnegative integer.
"""
    procedure factorial(n: nonnegative integer)
    if n = 0 then return 1
    else return n * factorial(n-1)
    {output is n!}
"""
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

### Example 2
# Give a recursive algorithm for computing an, where a is a nonzero real number and n is a nonnegative integer
"""
    procedure power(a: nonzero real number, n: nonnegative integer)
    if n = 0 then return 1
    else return a * power(a, n-1)
    {output is an}
"""
def power(a: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return a * power(a, n-1)


### Example 3 
# Give a recursive algorithm for computing the greatest common divisor of two nonnegative integers a and b with a < b.
"""
    procedure gcd(a, b: nonnegativeintegers with a < b)
    if a = 0 then return b
    else return gcd(b mod a, a)
    {output is gcd(a,b)}
"""
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    else:
        oa = a
        a = b % a
        b = oa
        return gcd(a , b)

### Example 4 A Recursive Linear Search Algorithm
"""
    procedure search(i, j, x: i, j, x integers, 1 <= i <= j <= n)
    if ai = x then
        return i
    else if i = j then 
        return 0
    else
        return search(i+1, j, x)
    {ourput is the location of x in a1, a2, ..., an if it appears; otherwise it is 0}
"""
def linear_search(i, j, x, arr):
    if arr[i] == x:
        return i
    elif i == j:
        return 0
    else:
        return linear_search(i+1, j, x, arr)

### Example 6 Construct a recursive version of a binary search algorithm
"""
    procedure binary search(i, j, x: i, j, x integers, 1 <= i <= j <= n)
    m := math.floor((i + j)/2)
    if x = am then 
        return m
    else if x < am and i < m then
        return bianry search(i, j, m-1, x)
    else if x > am and j > m then
        return binary search(i, j, m+1, x)
    else 
        return 0
"""
def binary_search(i, j, x, arr):
    m = math.floor((i+j)/2)
    if x == arr[m]:
        return m
    elif x < arr[m] and i < m:
        return binary_search(i, m-1, x, arr)
    elif x > arr[m] and j > m:
        return binary_search(m+1, j, x, arr)
    else:
        return 0


### Example 7 Recursive Modular Exponentiation
"""
    procedure mpower(b, n, m: integers with b > 0 and m >= 2, n >= 0)
    if n = 0 then
        return 1
    else if n i even then
        return mpower(b, n/2, m)2 mode m
    else 
        return mpower(b, math.floor(n/2), m)2 mod m * b mod m
    {output is bn mode m}
"""
def mpower(b, n, m):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(mpower(b, n/2, m), 2) % m
    else:
        return (pow(mpower(b, math.floor(n/2), m), 2) % m * b % m) % m



#### Proving Recursive Algorithm Correct
### Example 8
"""
    Prove that Algorithm 2, which compute powers of real numbers, is correct.
    BASIS STEP: for n = 0, power(a, 0) = 1
    INDUCTIVE STEP: 
        hypothesis: for n = k, f(k) = power(a, k) = ak
        prove: for n = k+1, f(k+1) = power(a, k+1) = ak+1 is correct
            => f(k+1) = power(a, k+1) = a * power(a, k) = a * ak = ak+1
"""


### Example 9
"""
    Prove that Example 7 is right
"""


#### Recursion and Iteration
### Iterative
# We can start with the value of the functionat one or more integers, the base cases, 
# and successively apply the recursive definition to 
# find the values of the function at successive larger integers
# Often an iterative approach for the evaluation of a recursively defined sequence requires much 
# less computation than a procedure using recursion

# ALGORITHM 7 A Recursive Algorithm For Fibonacci Numbers
"""
    procedure fibonacci(n: nonnegative integer)
    if n = 0 then return 0
    else if n = 1 then return 1
    else return fibonacci(n-1) + fibonacci(n-2)
    {output is fibonacci(n)}
"""
def fibonacci(n):                                    # O(n2)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# ALGORITHM 8 An Iterative Algorithm for Computing Fibonacci Numbers
"""
    procedure iterative fibonacci(n: nonnegative integer)
    if n = 0 then return 0
    else 
        x := 0
        y := 1
        for i := 1 to n - 1
            z := x + y
            x := y
            y := z
        return y
"""
def iterative_fibonacci(n):                           # O(n)
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        for i in range(1, n):
            z = x + y
            x = y
            y = z
        return y

def merge(L, R, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S): # O(n1 + n2)
        if j == len(R) or (i < len(L) and L[i] < R[j]):
            S[i + j] = L[i]
            i += 1
        else:
            S[i + j] = R[j]
            j += 1
    

# ALGORITHM 9 A Recursive Merge Sort
def merge_sort(S):
    l = len(S)
    if l < 2: return 
    m = l // 2
    L = S[:m]
    R = S[m:]

    merge_sort(L)
    merge_sort(R)

    merge(L, R, S)
    return S

# Example 10 Merge two lists 2, 3, 4, 5 and 1, 4.


    