from typing import MutableMapping


from collections.abc import MutableMapping

class MapBase(MutableMapping):
    '''Our own abstract base class that includes a nonpublic _Item class.'''

    # ---------------------------- nested _Item class ----------------------
    class _Item:
        '''Lightweight composite to store key-value pairs as map items.'''
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __eq__(self, other):
            return self._key == other._key    # compare items based on their keys
        
        def __ne__(self, other):
            return not (self == other)        # opposite of __eq__
        
        def __It__(self, other):
            return self._key < other._key     # compare items based on their keys


class UnsortedTableMap(MapBase):
    '''Map implementation using un unordered list.'''

    def __init__(self):
        '''Create an empty map.'''
        self._table = []                       # list of _Item's
    
    def __getitem__(self, k):
        '''Return value associated with key k (raise KeyError if not found.)'''
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: '+ repr(k))

    def __setitem__(self, k, v):
        '''Assign vlaue v to key k, overwriting existing value if present.'''
        for item in self._table:
            if k == item._key:
                item._value = v
                return 
        # did not find match for key
        self._table.append(self._Item(k, v))
    
    def __delitem__(self, k):
        '''Remove item associated with key k (raise KeyError if not found).'''
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return 
        raise KeyError('Key Error: ' + repr(k))
    
    def __len__(self):
        '''Return number of items in the map.'''
        return len(self._table)
    
    def __iter__(self):
        '''Generate iteration of the map's keys'''
        for item in self._table:
            yield item._key

from random import randrange

class HashMapBase(MapBase):
    '''Abstract base class for map using hash-table with MAD compression.'''

    def __init__(self, cap = 11, p = 109345121):
        '''Create an empty hash-table map.'''
        self._table = cap * [None]
        self._n = 0 
        self._prime = p                       # prime for MAD compression
        self._scale = 1 + randrange(p - 1)    # scale from 1 to p-1 for MAD
        self._shift = randrange(p)            # shift from 0 to p-1 for MAD
    
    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)
    
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)     # number 2 * x - 1 is often prime
    
    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1
    
    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v


class ChainHshMap(HashMapBase):
    '''Hash map implemented with separate chaining for collision resolution.'''

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))    # no match found
        return bucket[k]                               # mayu raise KeyError


    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()        # bucket is noew to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:              # key was new to the table
            self._n += 1                               # increase overall map size'
    
    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))    # no match found
        del bucket[k]                                  # may raise KeyError
    

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:                     # a nonempty slot
                for key in bucket:
                    yield key
    
    def show(self):
        list_a = []
        for bucket in self._table:
            if bucket is not None:
                for item in bucket._table:
                    data = (item._key, item._value)
                    list_a.append(data)
            else:
                list_a.append(bucket)
        print('list_a is =>', list_a)


# Linear Probing

class ProbeHashMap(HashMapBase):
    '''Hash map implemented with linear probing for collision resolution.'''
    _AVAIL = object()                       # sentinal marks locations of previous deletions

    def _is_available(self, j):
        '''Return True if index j is available in table.'''
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    
    def _find_slot(self, j, k):
        '''Search for key k in bucket at index j.

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found success is False and index denotes first available slot.
        
        '''

        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)                        # found a match
            j = (j + 1) % len(self._table)


    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))     # no match found
        return self._table[s]._value
    

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)           # insert new item
            self._n += 1                                # size has increased
        else:
            self._table[s]._value = v                   # overwrite exsting

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL()
    
    def __iter__(self):
        for j in range(len(self._table)):               # scan entire table
            if not self._is_available(j):
                yield self._table[j]._key
            

# We cannot stop the search upon reaching an _AVAIL sentinel

### 10.3 Sorted Maps
# The traditional map ADT allows a user
# If we can assume that time stamps are unique for a particular system
# 00:00 : 'Good'
# In fact, the fast performance of hash-based implementations of the map ADT relies on the intentionally scattering of keys that may seem very 
# so that they are more uniformly distributed in a hash table
# sorted map

# M.find_min() => Return the (key, value) pair with minimum key (or None, if map is empty).
# M.find_max() => Return the (key, value) pair with maximum key (or None, if map is empty).
# M.find_It(k) => Return the (key, value) pair with the greatest key that is strictly less than k (or None, if no such item exists).
# M.find_le(k) => Return the (key, vlaue) pair with the greatest key that is less than or equal to k (or None, if no such item exists).
# M.find_gt(k) => Return the (key, value) pair with the least key that is strictly greater than k (or None, if no such item exists).
# M.find_ge(k) => Return the (key, value) pair with the least key that is greater than or equal to k (or None, if no such item exists).
# M.find_range(start, stop) => Iterate all (key, value) pairs with start <= key < stop. If start is None, iteration concludes with maximum key.
# iter(M) => Iterate all keys of the map according to their natural order, from smallest to largest.
# reversed(M) => Iterate all keys of the map in reverse order; in Python, this is implemented with the __reversed__ method.



# 10.3.1 Sorted Search Tables
# We store the map's items in an array-based sequence A so that they are in increasing order of their keys, assuming the keys have a naturally defined order.

# The primary advantage of this representation, and our reason for insisting that A be "array-based", is that it allows us to use the "binary search" 
# algorithm for a variety of efficient operations.
# While such an approach could be used to implement the __contains__ method  of the map ADT,
 
# The important realization is that while performing a binary search,
# SortedTableMap => supports the sorted map ADT.
# notable feature of our design is the inclusion of a "_find_index"
# This method using the binary search algorithm.
# but by convention
# For __delItem__ we again rely on the convenience of "_find_index"

class SortedTableMap(MapBase):
    '''Map implementation using a sorted table.'''

    # ------------------------ nonpublic behaviors ------------------------
    def _find_index(self, k, low, high): # O(logn) 
        '''
        Return Bianry Search
        Return index of the leftmost item with key greater than or equal to k.
        Return high + 1 if no such item qualifies.
        That is, j will be returned such that:
            all items of slice table[low:j] have key < k
            all items of slice table[j:high+1] have key >= k
        '''

        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:                  # found exact match
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)    # Note: may return mid
            else:
                return self._find_index(k, mid + 1, high)   # anser is right of mid
    
    # ------------------------ public behaviors --------------------------
    def __init__(self):
        '''Create an empty map.'''
        self._table = []
    

    def __len__(self):
        '''Return number of items in the mpa.'''
        return len(self._table)
    

    def __getitem__(self, k):
        '''Return value associated with key k (raise KeyError if not found).'''
        j = self._find_index(k, 0, len(self._table) - 1)
        print('j is =>', j)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value


    def __setitem__(self, k, v):
        '''Assign value v to key k, overwriting existing value if present.'''
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v                         # reassign value
        else:
            self._table.insert(j, self._Item(k, v))           # adds new item
    

    def __delitem__(self, k):
        '''Remove item associated with key k (raise KeyError if not found.)'''
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)                                    # delete item
    

    def __iter__(self):
        '''Generate keys of the map ordered from minimum to maximum'''
        for item in self._table:
            yield (item._key, item._value)
    

    def __reversed__(self):
        '''Generate keys of the map ordered from maximum to minimum.'''
        for item in reversed(self._table):
            yield item._key
    

    def find_min(self):
        '''Return (key, value) pair with minimum key (or None if empty).'''
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None
    

    def find_max(self):
        '''Return (key, value) pair with maximum key (or None if empty).'''
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None
    

    def find_ge(self, k):
        '''Return (key, value) pair with least key greater than or equal to k.'''
        j = self._find_index(k, 0, len(self._table) - 1)          # j's key >= k
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None
    
    def find_le(self, k):
        '''Return (key, value) pair with least key less than or equal to k.'''
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            if self._table[j]._key == k:
                return (self._table[j]._key, self._table[j]._value)
            else:
                return (self._table[j-1]._key, self._table[j-1]._value)
        else:
            return None



    def find_lt(self, k):
        '''Return (key, value) pair with greatest key strictly less than k.'''
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)
        else:
            return None
    

    def find_gt(self, k):
        '''Return (key, value) pair with least key strictly greater than k.'''
        j = self._find_index(k, 0, len(self._table) - 1)           # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            j += 1
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None


    def find_range(self, start, stop):
        '''Iterate all (key, value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        '''
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1) # find first result
        
        while j < len(self._table) and (stop is None or self._table[j]._key < stop): # 若有 stop, 則大於 stop 就跳出
            yield(self._table[j]._key, self._table[j]._value)
            j += 1


### 10.3.2 Two Applications of Sorted Maps
# Furthermore, to take advantage of the inexact or range searches afforded by a sorted map, there should be some reason why nearby keys have relevance to a search

### Flight Databases
# 
# Maintaining a Maxima Set  with a Sorted Map
# so that the cost is the key field and performance(speed) is the value field.
class CostPerformanceDatabase:
    '''
        Maintain a database of maximal (cost, performance) pairs.
        c : cost 
        p : performance
    '''

    def __init__(self):
        '''Create an empty database.'''
        self._M = SortedTableMap()         # or a more efficient sorted map
    
    def best(self, c):
        '''Return (cost, performance) pair with largest cost not exceeding c.

        Return None if there is no such pair.
        '''
        return self._M.find_le(c)
    

    def add(self, c, p): # O((1 + r)logn)
        '''Add new entry with cost c and performance p.'''
        # determine if (c, p) is dominated by an existing pair
        other = self._M.find_le(c)                      # other is at least as cheap as c
        while other is not None and other[1] <= p:      # if its performance is as good,
            return                                      # (c, p) is dominated, so ignore
        self._M[c] = p                                  # else, add (c, p) to database 
        # and now remove any pairs that are dominated by (c, p)
        other = self._M.find_gt(c)                      # other more expensive than c
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)


### 10.4 Skip Lists
# we saw that a sorted array will allow O(logn)-time searches via the binary search algorithm.
# Unfortunately, update operations on a sorted array have O(n) worst-case running time because of the need to shift elements.
# we refer to h as the height of skip list S.
# that Si+1 contains more or less alternate items of Si
# Functions that generate numbers that can be view
# pseudo-random number generators
# Nevertheless, the bounds are expected for the skip list
# while binary search has worst-case bound with 
# Instead, it depends on the use of a random-number generator in the implementation of the insertions to help decide where to place the new item.
# Each level is a list Si and each tower contains positions storing the same item across consecutive lists.
# next(p) : Return the position following p on the same level.
# prev(p) : Return the position preceding p on the same level.
# below(p) : Return the position below p in the same tower.

### Algorithm SkipSearch(k):
    # Input: A search key k
    # Output: Position p in the bottom list S0 with the largest key such that key(p) <= k
    # p = start
    # while below(p)

### Algorithm SkipInsert(k, v):
    # Input: Key k and value v
    # Output: Topmost position of the item inserted in the skip list
    # p = SkipSearch(k)
    # q = None            {q will represent top node in new item's tower}
    # i = -1

### Removal in a Skip List
# A set is an unordered collection of elements, without duplicates, that typically supports efficient membership tests. 
# If the position "p" stores an entry with key different from k, we raise a KeyError

# Maintaing the Topmost Level


### 10.4.2 Probabilistic Analysis of Skip Lists *
# In any case, if we terminate position insertion
# __getitem__, __setitem__, __delitem__ worst case running time => O(n + h)


# Let us begin by determing the expected value of the height h of a skip list S with n entries
# The probability that a given entry has a tower of height i >= 1
# Hence, the probabiliby Pi that level i has at least one position is at most
# for the probability that any one of n different events occurs is at most the sum of the probabilities that each occrus


### 10.5 Sets, Multisets, and Multimaps