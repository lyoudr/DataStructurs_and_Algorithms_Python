# 12.2 Merge-Sort

# Divide-and-conquer

# 1. Divide:
# If the input size is smaller than a certain threshold (say, one or two elements), 
# solve the problem directly using a straightforward method and return the solution so obtained
# Otherwise, divide the input data into two or moredisjoint subsets
# S => n
# S1 = n/2
# S2 = n/2 


# 2. Conquer:
# Recursively solve the subproblems associated with the subsets

# 3. Combine:
# Take the solutions to subproblems and merge them into a solution 

from linked_list import LinkedQueue
import math


def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S): # O(n1 + n2)
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1


def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2: return                  # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]                     # copy of first half
    S2 = S[mid:n]                     # copy of second half
    
    # conquer
    merge_sort(S1)
    merge_sort(S2)

    # merge results
    merge(S1, S2, S)                  # merge sorted halves back into S


# 12.2.4 Merge-Sort and Recurrence Equations
# There is another way to justify that the running time of the merge-sort algorithm is O(nlogn)
# Namely, we can deal more directly with the recursive nature of the merge-sort algorithm
# In this section, we present such an analysis of the running time of merge-sort, and in so doing, introduce the mathematical concept of a recurrence equation (also known as "recurrence relation")
# Let the function t(n) denote the worst-case running time of merge-sort
# In order to simplify our characterization of t(n), let us restrict our attention to the case when n is a power of 2.



# 12.2.5 Alternative Implementations of Merge-Sort
# Sorting Linked Lists
# The merge-sort algorithm can easily be adapted to use any form of a basic queue as its container type.
# We provide such an implementation, based on use of the LinkedQueue

def merge(S1, S2, S):
    '''Merge two sorted queue instances S1 and S2 into empty queue S.'''
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():                        # move remaining elements of S1 to S
        S.enqueue(S1.dequeue())   
    while not S2.is_empty():                        # move remaining elements of S2 to S
        S.enqueue(S2.dequeue())


def merge_sort(S):
    '''Sort the elements of queue S using the merge-sort algorithm'''
    n = len(S)
    if n < 2:
        return                                       # list is already sorted
    # divide
    S1 = LinkedQueue()
    S2 = LinkedQueue()
    while len(S1) < n // 2:                         # move the first n // 2 elements to S1
        S1.enqueue(S.dequeue())
    while not S.is_empty():                         # move the rest to S2
        S2.enqueue(S.dequeue())
    
    # conquer (with recursion)
    merge_sort(S1)                                  # sort first half
    merge_sort(S2)                                  # sort second half
    # merge results
    merge(S1, S2, S)                                # merge sorted halves back into S

# A Bottom-Up (Nonrecursive) Merge-Sort
# We merge these runs into runs of length four, 
# merge these new runs into tuns of length eight, and so on, until the array is sorted
def merge(src, result, start, inc):
    print('result is =>', result, start, inc)
    """Merge src[start:start+inc] and src[start+inc:start_2"""
    end1 = start + inc                              # boundary for run 1
    end2 = min(start + 2*inc, len(src))             # boundary for run 2
    print('end1, end2 is =>', end1, end2)
    x, y, z = start, start + inc, start             # index into run 1, run 2, result
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]
            x += 1                                  # copy from run 1 and increment x
        else:
            result[z] = src[y]
            y += 1                                  # copy from run 2 and increment y
        z += 1
    if x < end1:
        result[z:end2] = src[x:end1]                # copy remainder of run 1 to output
    elif y < end2:
        result[z:end2] = src[y:end2]                # copy remainder of run 2 to output

def bottom_merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    logn = math.ceil(math.log(n, 2))
    print('logn is =>', logn)
    src, dest = S, [None] * n
    for i in (2**k for k in range(logn)):             # pass i creates all runs of length 2i
        for j in range(0, n, 2**i):
            merge(src, dest, j, i)
        src, dest = dest, src
    if S is not src:
        S[0:n] = src[0:n]


# Quick Sort
# Like merge-sort, this algorithm is also based on the divide-and-conquer paradigm, but it uses this technique in a somewhat opposite manner
# as all the hard work is done before the recursive calls

# The quick-sort algotithm sorts a sequence S using a simple recursive approach.
# The main idea is to apply the "divide-and-conquer" technique, where by we divide S into subsequences, 
# recur to sort each subsequence, and then combine the sorted subsequences by a simple concatenation.
# the execution of quick-sort can be visualized by means of a binary recursion tree, called the "quick-sort tree"
# 1. Divide : 
# 2. Conquer : Recursively sort sequences L and G.
# 3. Combine : Put back the elements into S in order by first 
# inserting the elements of L, 
# then those of E, 
# and finally those of G

# Perfoming Quick-Sort on General Sequences
# we provide a more streamlined implementation of quick-sort using an array-based sequence in Section 12.3.2.
# Our implementation chooses the first item of the queue as the pivot

def quick_sort(S): # O(n) each time
    '''Sort the elements of queue S using the quick-sort algorithm.'''
    n = len(S)
    if n < 2:
        return                                     # list is already sorted
    
    # divide
    p = S.first()                                  # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue() 
    G = LinkedQueue()

    while not S.is_empty():                        # divide S into L, E, and G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:                                      # S.first() must equal pivot
            E.enqueue(S.dequeue())
    
    # conquer(with recursion)
    quick_sort(L)
    quick_sort(G)
    
    # concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

# The height of quick-sort tree T is => n

# Picking Pivots at Random
# let us introduce randomization into the algorithm and pick as the "pivot" a random element of the input sequence.
# Randomized quick-sort => pick an element of S at random as the pivot, keeping the rest of the algorithm unchanged.
# good
# n => the size of the input for this call
# L => size at least n/4
# G => size at least 3n/4

# In-place quick-sort modifies the input sequence using element swapping and does not explicitly create subsequences.
# Instead, a subsequence of the input sequence is implicitly represented by a range of positions specified by a leftmost index a and a rightmost index b

def inplace_quick_sort(S, a, b):
    '''Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm.'''
    if a > b: return
    pivot = S[b]                  # last element of range is pivot
    left = a                      # will scan rightward
    right = b - 1
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        
        if left <= right:
            S[left], S[right] = S[right], S[left]               # swap values
            left, right = left + 1, right - 1
    
    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)

# we note that the complete quick-sort algorithm needs space for a stack propotional to the depth of the recursion tree,
# Pivot Selection
# As described in Section 12.3.1, this can be improved upon by using a randomly chosen pivot for each partition step.
# In practice, another common 

### Hybrid Approaches
# Although quick-sort has very 

class _Item:
        '''Lightweight composite to store priority queue items.'''
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __lt__(self, other):
            return self._key < other._key 

def decorated_merge_sort(data, key = None):
    '''Demonstration of the decorate-sort-undecorate pattern.'''
    if key is not None:
        for j in range(len(data)): 
            data[j] = _Item(key(data[j]), data[j])         # decorate each element
    merge_sort(data)
    if key is not None:
        for j in range(len(data)):
            data[j] = data[j]._value

# Down-Heap Bubbling After a Removal


### Bucket-Sort
# S should be sorted according to the keys of the keys of the entries
# we can sort S in O(n) time

def bucket_sort(array):
    # create empty buckets
    bucket = [[]] * len(array)
    
    # Insert elements into their respective buckets
    for j in array:
        print('j is =>', j)
        index_b = int(10 * j)
        bucket[index_b].append(j)
    print('1. bucket is =>', bucket)
    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    
    # Get the sorted elements
    print('2. bucket is =>', bucket)
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


### Stable Sorting
# When sorting key-value pairs, an important issue is how equal keys are handled.
# S = ((k0, v0), ..., (kn-1, vn-1))
# We say that a sorting algorithm is "stable" if, for any two entries (ki, vi) and (kj, vj)
# entry (ki, vi) also precedes entry (kj, vj) after sorting

# Our informal description of bucket-sort in 

### Radix-Sort
# lexicographic (dictionary)
# (k1, l1) < (k2, l2) if k1 < k2 of if k1 = k2 and l1 < l2
# We leave to a simple exercise (R-12.18) the determination of how this approach 
### Proposision 12.6
# Let S be a sequence of n key-value pairs, each of which has a key (k1, k2, ..., kd), 
# where ki is an integer in the range [0, N - 1] for some integer N >= 2
# We can sort S lexicographically in time O(d(n + N)) using radix-sort.

# Radix sort can be applied to any key that can be viewed as composite of smaller
# For example, we can apply it to sort character strings of moderate length, as each individual character can be represented as an integer value. 



### 12.5 Comparing Sorting Algorithms
# We have studied several methods, such as insertion-sort, and selection-sort, that have O(n2)-time behavior in the average and worst case.
# We have also studied several methods with O(nlogn)-time behavior, including heap-sort, merge-sort, and quick-sort

# Insertion Sort
# But the O(n2)-time performance of insertion-sort

# Heap Sort
# small- and medium-sized sequences, when input data can fit into main memory.

# During the second phase of pq_sort, 

# Randomized quick-selection algorithm
import random

def quick_select(S, k):
    """ Return the kth smalleast element of list S, for k from 1 to len(S). """
    if len(S) == 1:
        return S[0]
    pivot = random.choice(S)              # pick random pivot elemetn from S
    L = [x for x in S if x < pivot]       # elements less than pivot
    E = [x for x in S if x == pivot]      # elements equal to pivot
    G = [x for x in S if pivot < x]       # elements greater than pivot
    if k <= len(L):      
        return quick_select(L, k)         # kth smalleast lies in L
    elif k <= len(L) + len(E):
        return pivot
    else:
        j = k - len(L) - len(E)           # new selection parameter  
        return quick_select(G, j)         # kth smallest is jth in G



### Graphs
# graphs have applications in modeling many domains, including mapping, transportation

# vertices : 頂點 => nodes
# edges : 邊 => arcs

# Edges in a graph are either "directed" or "unidirected"
# An edge (u, v) is said to be directed from u to v if the pair (u, v) is ordered, with u preceding v.
 