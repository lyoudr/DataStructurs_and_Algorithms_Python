class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass 
class ArrayStack: 
    """LIFO Stack implementation using a Python list as underlying storage."""
    
    def __init__(self):
        """Create an empty stack."""
        self._data = []
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO)
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

# Practice 
# C-6.16 Modify the ArrayStack implementation so that the stack's capacity is limited to maxlen elements
#, where maxlen is an optional parameter to the constructure. 
# If push is called when the stack is at full capacity, throw a Full exception.
class Full(Exception):
    pass 

class ModifiedArrayStack(ArrayStack):
    def __init__(self, maxlen, *args, **kwargs):
        self._maxlen = maxlen
        super().__init__(*args, **kwargs)
    
    def push(self, e):
        print("len is ->", len(self._data))
        print("self._maxlen is ->", self._maxlen)
        if len(self._data) + 1 > self._maxlen:
            raise Full('stack is full')
        else:
            super().push(e)
    
### Reversing Data Using a Stack
def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')       # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

# An Algorithm for Matching Dellimiters
def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise;"""
    lefty = '{[('
    righty = ')]}'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False 
            if righty.index(c) != lefty.index(S.pop()):
                return False 
    return S.is_empty()
    
def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)        # 從 index j+1 開始找
        if k == -1:
            return False 
        tag = raw[j+1:k] 
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False 
            if tag[1:] != S.pop():
                return False 
        j = raw.find('<', k+1)
    return S.is_empty()                # were all opening tags matched ?



class ArrayQueue: 
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10             # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queu is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO)
        Raise Empty exception if the queue is empty

        # Shrinking the Underlying Array
        # A robust approach is to reduce the array to half of its current size.
        # whenever the number of elements stored in it falls below 1/4 of its capacity.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None                # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))       # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e 
        self._size += 1
    
    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data 
        self._data = [None] * cap 
        walk = self._front 
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

# R-6.3 Implement a function with signature transfer(S, T) that transfers all elements
# from stack S onto stack T, so that the element that starts at the top os S is the 
# first to be inserted onto T, and element at the bottom of S ends up at the top of T.

def transfer(S: ArrayStack, T: ArrayStack):
    while not S.is_empty():
        e =  S.pop()
        T.push(e)

# R-6.4 Give a recursive method for removing all the elements from a stack
def recursive_remove(S: ArrayStack):
    if not S.is_empty():
        S.pop()
        recursive_remove(S)
    print('S._data is ->', S._data)

# R-6.5 Implement a function that reverses a list of elements by pushing them onto a stack in one order,
def reverse_list(l: list):
    S = ArrayStack()
    for e in l:
        S.push(e)
    i = 0
    while not S.is_empty() and i < len(l):
        l[i] = S.pop()
        i += 1
    print('reversed l is ->', l)
    return l

# 7.1.1 Singly Linked List
class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""
    # ------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next): 
            self._element = element 
            self._next = next
    
    # ------------------------- stack methods -------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None 
        self._size = 0
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO)
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element 
        self._head = self._head._next 
        self._size -= 1
        return answer