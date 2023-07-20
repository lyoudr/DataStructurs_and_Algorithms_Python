# priority Queue
# This is a collection of priorititized elements that allows arbitrary element insertion, and allows the removal of the element that has first priority.
# When an element is added to a priority queue, the user designates its priority by providing an associated key.

# priority queue P:
### 9.2 Implementing a Priority Queue
# 9.2.1 The Composition Design Pattern

from linked_list import PositionalList


class PriorityQueue:
    '''Abstract base class for a priority queue.'''

    class _Item:
        '''Lightweight composite to store priority queue items.'''
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __lt__(self, other):
            return self._key < other._key               # compare items based on their keys
    

    def is_empty(self):
        '''Return True if the priority queue is empty.'''
        return len(self) == 0

class Empty(Exception):
    pass

class UnsortedPriorityQueue(PriorityQueue):            # base class defines _Item
    '''A min-oriented priority queue implemented with an unsorted list.'''

    def _find_min(self): # O(n)
        '''Return Position of item with minimum key.'''
        if self.is_empty():                            # is_empty inherited from base class
            raise Empty('Priority queu is empty')
        small = self._data.first()
        walk = self._data.after(small)
        
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small
    
    def __init__(self):
        '''Create a new empty Priority Queue.'''
        self._data = PositionalList()
    

    def __len__(self):
        '''Return the number of items in the priority queue.'''
        return len(self._data)
    
    def add(self, key, value): # O(1)
        '''Add a key-value pair.'''
        self._data.add_last(self._Item(key, value))
    
    def min(self):
        '''Return but do not remove (k,v) tuple with minimum key.'''
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self): # O(n)
        '''Remove and return (k, v) tuple with minimum key.'''
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)



class SortedPriorityQueue(PriorityQueue): 
    '''An min-oriented priority queue implemented with a sorted list.'''

    def __init__(self):
        '''Create a new empty Priority Queue.'''
        self._data = PositionalList()
    
    def __len__(self):
        '''Return the number of items in the priority queue.'''
        return len(self._data)
    
    def add(self, key, value): # O(n)
        '''Add a key-value pair.'''
        newest = self._Item(key, value)                        # make new item instance
        walk = self._data.last()                               # walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)                       # new key is smallest   
        else:
            self._data.add_after(walk, newest)                 # newest goes after walk
    
    def min(self):
        '''Return but do not remove (k, v) tuple with minimum key.'''
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        '''Remove and return (k, v) tuple with minimum key.'''
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

# 9.3 Heap 
# => binary heap : This data structure allows us to perform both insertions and removals in logarithmic time,
# Heap-Order Priority : In a heap T, for every position p other than the root, the key stored at p is greater than or equal to the key stored at p's parent.
# Also, a minimum key is always stored at the root of T
# For the sake of efficiency, as will become clear later, we want the heap T to have as small a height as possible.
# We enforce this requirement by insisting that the heap T satisfy an additional structural property = it must be what we term "complete"

# Complete Bianry Tree Property : 
# A heap T with height h is a complete binary tree if levels 0, 1, 2, ..., h - 1 of T have the maximum number of nodes possible 
# and the remaining nodes at level h reside in the leftmost possible positions at that level.
# We will use the composition pattern to store key-value pairs as items in the heap
# 20 = 1
# 21 = 2
# 22 = 4

# The len and is_empty methods can be implemented based on examination of the tree,

### Up-Heap Bubbling After an Insertion

# After this action, the tree T is complete, but it may violate
# A swap either resolves the violation of the heap-order property
# Thus, in the worst case, the number of swaps performed in the execution of method "add" is equal to the height of T
# Instead, we ensure that the shape of the heap respects the "complete binary tree property" by deleting the leaf at the last position p of T, defined as the rightmost position at the bottommost level of the tree.
# To preserve the item from the last position p, we copy it to the root r


# Down-Heap Bubbling After a Removal
# where p initially denotes the root of T:
# (1) If p has no right child, let c be the left child of p.
# (2) Otherwise (p has both children), let c be a child of p with minimal key.

# A swap either resolves the violation of the heap-order
# so "remove_min" => [logn] = height of T
# This downward swapping process is called "down-heap bubbling "


# 9.3.3 Array-Based Representation of a Complete Binary Tree

# We recall that in this implementation, the elements of T are stored in an array-based list A
# Implementing a priority queue using an array-based heap representation allows us to avoid some com
# if p is the root of T, f(p) = 0
# 

# 9.3.4 Python Heap Implementation
# An implementation of a priority queue using an array-based heap

class HeapPriorityQueue(PriorityQueue):
    '''A min-oriented priority queue implemented with a binary heap. (binary tree with complete)'''
    # ------------------------------- nonpublic behaviors -----------------------------------------
    def _parent(self, j):
        return (j-1) // 2
    
    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left(j)  < len(self._data)
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        '''Swap the elements at indices i and j of array.'''
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _upheap(self, j): # O(logn)
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)
    
    def _downheap(self, j): # O(logn)
        if self._has_left(j):
            left = self._left(j)
            small_child = left                 # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)    # recur at position of small child
    
    # ----------------------------- public behaviors -------------------------------------------------
    def __init__(self):
        '''Create a new empty Priority Queue.'''
        self._data = []
    
    def __len__(self):
        '''Return the number of items in the priority queue.'''
        return len(self._data)
    
    def add(self, key, value): # O(logn)
        '''Add a key-value pair to the priority queue.'''
        self._data.append(self._Item(key, value))                    # append new item to last position of this heap
        self._upheap(len(self._data) - 1)                            # start upheap bubbling until find element small than current element

    def min(self):
        '''
            Return but do not remove (k, v) tuple with minimum key.
            Raise Empty exception if empty.
        '''
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self): # O(logn)
        '''
            Remove and return (k, v) tuple with minimum key.
            Raise Empty exception if empty.
        '''
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0 , len(self._data) - 1)                         # put minimum item at the end
        item = self._data.pop()                                     # and remove it from the list;
        self._downheap(0)
        return (item._key, item._value)


# 9.3.5 Analysis of a Heap-Based Priority Queue
# The space requirement is O(n).
# The running time of operation, 
# In this section, we describe the bottom-up heap construction, 
# and provide an implementation that can be used by the constructor of a 
# heap-based priority queue.
# The new entry is placed initially at the root, but may have to move down with down-heap bub

# Python Implementation of a Bottom-Up Heap Construction
# we can implement the bottom-up heap construction process with a single loop that makes a call to _downheap 
# In fact, that loop can start with the deepest nonleaf, since there is no effect when down-heap is called at a leaf position.
# We have redesigned the constructor of the class to accept an optional parameter that can be any sequence of (k, v) tuples 
# Rather than initializing self._data to an empty list, we use a list comprehension syntax to create an initial list of item 

class HeapPriorityQueueBottomUp(HeapPriorityQueue):
    
    def __init__(self, contents = ()):
        '''
            Create a new priority queue.
            By default, queue will be empty. If contents is given, 
            it should be as an iterable sequence of (k, v) tuples specifying the initial contents.
        '''
        self._data = [self._Item(k, v) for k, v in contents]       # empty by default
        if len(self._data) > 1:
            self._heapify()
    
    def _heapify(self):
        start = self._parent(len(self) - 1)
        for j in range(start, -1 , -1):
            self._downheap(j)

# 9.3.7 Python's heapq Module
# Python's standard distribution includes a "heapq" module that provides support for heap-based priority queues.
# That module does not provide any priority queue class;
# instead it provides functions that allow a standard Python list to be managed as a heap.
# Its model is essentially the same as our own, with n elements stored in list cells L[0] through L[n-1], 
# based on the level-numbering indices with the smalleast element at the root in L[0].
# We note that heapq does not separately manage associated values; elements serve as their own key.



# 9.4 Sorting with a Priority Queue
# sort a collection C of comparable elements.
# That is, we can produce a sequence of elements of C in increasing order (or at least in nondecreasing order if there are duplicates)

def pq_sort(C):
    '''Sort a collection of elements stored in a positional list.'''
    n = len(C)                                  # C is a positional list.
    P = HeapPriorityQueue()

    for j in range(n): # O(nlogn)
        element = C.delete(C.first())
        P.add(element, element)                 # use element as key and value

    for j in range(n): # O(nlogn)
        (k, v) = P.remove_min()
        C.add_last(v)                           # store smallest remaining element in C
        
# We next discuss as choice of priority queue implementations that in effect cause the pq_sort computation to behave as one of several classic sorting algorithms.

# 9.4.1 Selection-Sort and Insertion-Sort
# In Phase 2, the running time of each remove_min operation is proportional to the size of P
# We repeatedly remove an entry with smallest key from the priority queue P.
# The size of P starts at n and 
# Thus, the first operation takes time O(n), the second one takes time O(n-1), and so on.


# 9.4.2 Heap-Sort
# If the collection C to be sorted is implemented by means of an array-based 
# There are four major reasons for building distributed system: resource sharing, computation speedup,reliability and


# 9.5.2 Implementing an Adaptable Priority Queue
# HeapPriorityQueue 
# To implement a Locator class, we will extend the existing _Item composite to add an additional field designating the current index of the element within the array-based representation of our heap
# When we perform priority queue operations on our heap, and items are 

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    # --------------------- nested Locator class -------------------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = '_index'                                         # add index as additional field

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j
    
    # --------------------- nonpublic behaviors --------------------------
    # override swap to record new indices
    def _swap(self, i, j):
        super()._swap(i, j)                                          # perform the swap
        self._data[i]._index = i                                     # reset locator index (post-swap)
        self._data[j]._index = j                                     # reset locator index (post-swap)


    # The _bubble utility determines whether to apply up-heap or down-heap bubbling
    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)
    
    def add(self, key, value):
        """Add a key-value pair."""
        token = self.Locator(key, value, len(self._data))            # initialize locator index
        self._data.append(token)
        self._upheap(len(self._data) - 1)       
        return token 
    
    def update(self, loc, newkey, newval):
        """Update the key and value for the entry identified by Locator loc."""
        j = loc._index
        if not(0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        loc._key = newkey
        loc._value = newval
        self._bubble(j)
    
    def remove(self, loc):
        """Remove and return (k, v) pair identified by Locator loc."""
        j = loc._index
        if not(0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        if j == len(self) - 1:                                       # item at last position
            self._data.pop()                                         # just remove it
        else:
            self._swap(j, len(self) - 1)                             # swap item to the last position
            self._data.pop()                                         # remove it from the list
            self._bubble(j)                                          # fix item displaced by the swap
        return (loc._key, loc._value)
        