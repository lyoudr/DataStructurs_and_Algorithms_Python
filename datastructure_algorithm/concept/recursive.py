# 4.1.1 The Factorial Function
# n! = n*(n-1)*(n-2)*...3*2*1
# 5! = 5 * 4 * 3 * 2 *1
# In Python, each time a function (recursive or otherwise) is called, a structure known as "activation record" of frame is craeted to store informaion
def factorial(n): # O(n)
    if n == 0:
        return 1
    else :
        return n * factorial(n - 1)

def binary_search(data, target, low, high): # O(logn)
    if low > high:
        return False 
    else :
        mid = (low + high) // 2
        if target == data[mid]:
            print('mid is =>', mid)
            return (True, mid)
        elif target > data[mid]:
            binary_search(data, target, mid + 1, high)
        else :
            binary_search(data, target, low, mid - 1)

# 4.1.4 File Systems
import os

def disk_usage(path): # a type of Multiple Recursion
    '''Retrun the number of bytes used by a file/folder and any descendents.'''
    total = os.path.getsize(path)                                  # account for direct usage
    if os.path.isdir(path):                                        # if this is a directory
        for filename in os.listdir(path):   
            child_path = os.path.join(path, filename)               # compmose full path to child
            total += disk_usage(child_path)
    print('{0:<7}'.format(total), path)
    return total

# The idea that we can sometimes get a tighter bound on a series of operations by considering the cumulative effect
# rather than assuming that each achieves a worst case is a technique called amortization.


# English Ruler 
def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


# 4.3 Recursion Run Amok
# Although recursion is a very powerful tool, it can easily be 
# An Inefficient Recursion for Computing Fibonacci Numbers

# F0 = 0
# F1 = 1
# Fn = Fn-2 + Fn-1 for n > 1

def bad_fibonacci(n):
    '''Return the nth Fibonacci number'''
    if n <= 1:
        return n
    else :
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)

# An Efficient Recursion for Computing Fibonacci Numbers
def good_fibonacci(n): # O(n)
    '''Return pair of Fibonacci numbers, F(n) and F(n-1)'''
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        print('a, b is =>', (a, b))
        return (a + b, a)

# Fortunately, the Python interpreter can be dynamically reconfigured to change the default recursive limmit


# 4.4 Further Examples of Recursion
# We organize our presentation by considering the maximum number of recursive calls that may be started from within the body of a single activation.

# If a recursive call starts at most one other, we call this a linear recursion.
# If a recursive call may start two others, we call this a binary recursion.
# If a recursive call may start three or more others, this is multiple recursion.

# 4.4.1 Linear Recursion
# the "linear recursion" terminology reflects the structure of the recursion trace
# Summing the Elements of a Sequence Recursively
# A recursive algorithm for computing the sum of a sequence of numbers based on this intuition is implemented in Figure 4.9
def linear_sum(S, n):
    '''Return the sum of the first n numbers of sequence S.'''
    if n == 0:
        return 0
    else :
        print('S[n-1] is =>', S[n-1])
        return  S[n - 1] + linear_sum(S, n - 1)

# Reversing a Sequence with Recursion
def reverse(S, start, stop):
    print('strat is =>', start)
    print('stop is =>', stop)
    '''Reverse elements in implicit slice S[start:stop].'''
    if start < stop - 1:             # if at least 2 elements
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)

# Recursive Algorithms For Computing Powers
# power(x, n) =>
# 1                    if n = 0
# x * power(x, n-1)    otherwise

def power(x, n): # O(n)
    '''Compute the value x**n for integer n.'''
    if n == 0:
        return 1
    else:
        print('x is =>', x)
        return x * power(x, n - 1)

def power(x, n):  # O(logn)
    '''Compute the value x**n for integer n.'''
    if n == 0:
        return 1
    else :
        partial = power(x, n // 2)     # rely on truncated division
        print('partial is =>', partial)
        result = partial * partial
        if n % 2 == 1:
            print('n is =>', n)
            print('x is =>', x)
            result *= x                # if n odd, include extra factor of x
        return result

# The improved version also provides significant saving in reducing the memory usuage.

# 4.4.2 Binary Recursion
def binary_sum(S, start, stop): # O(n)
    '''Return the sum of the numbers in impmlicit slice S[start:stop].'''
    if start > stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else :
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

# 4.4.3 Multiple
# Generalizing from binary recursion, we define "multiple recursion" as a process in which a function may make more than two recursive calls.

# summation puzzles:
# pot + pan = bib
# dog + cat = pig
# boy + girl = baby


### An Inefficient Recursion for Computing Fibonacci Numbers 
"""
    F0 = 0
    F1 = 1 
    Fn = Fn-2 + Fn-1 for n > 1
"""
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# good efficient fibonacci
def good_fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        print('a, b is ->', (a, b))
        (a, b) = good_fibonacci(n-1)
        print('a+b, a is ->' (a+b, a))
        return (a+b, a)

def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

def reverse_seq(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse_seq(S, start+1, stop-1)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial 
        if n % 2 == 1:
            result *= x 
        return result
    
# C-4.10
# Describe a recursive algorithm to compute the integer part of the base-two logarithm of n using only addition and integer division
def log(n, ans):
    if n == 1:
        return ans
    else:
        n = (n // 2)
        ans += 1
        return log(n, ans)
# C-4.11 
# Describe an efficient recursive function for solving the element uniqueness problem, which runs in time that is at most O(n2) in the worst case without using sorting
def unique(S, start):
    current = S[start]
    if start + 1 < len(S):
        for i in S[start+1:]:
            if i == current:
                return False
        unique(S, start+1)
    return True

# C-4.15
# Write a recursive function that will output all the subsets of a set of n
# elements (without repeating any subsets).
def find_all_subset(S, output:list, start, end):
    if type(S) != list:
        S = list(S)
    subset = set()
    if start < end and end <= len(S):
        for i in S[start:end]:
            subset.add(i)
        output.append(subset)
        end += 1
        find_all_subset(S, output, start, end)
    else:
        start += 1
        end = start + 1
        if start <= len(S) - 1:
            find_all_subset(S, output, start, end)
        else:
            return output
        
