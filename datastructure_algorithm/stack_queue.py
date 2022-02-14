
class Empty(Exception):
    '''Error attempting to access an element from an empty container.'''
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


def reverse_file():
    """Overwrite given file with its contents line-by-line reversed."""

    S = ArrayStack()
    original = open('/Users/ann.ke/Ann/os/sample.txt')
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open('/Users/ann.ke/Ann/os/new_sample.txt', 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    
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
    ''' Return True if all HTML tags are properly match; False otherwise. '''
    S = ArrayStack()
    j = raw.find('<')                 # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j + 1)      # find next '>' character
        if k == -1 : 
            return False              # invalid tag
        tag = raw[j + 1:k]            # strip away <>
        if not tag.startswith('/'):   # this is opening tag
            S.push(tag)
        else :
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k + 1)
    return S.is_empty()




# The Queue Abstract Data Type
# first-in, first-out (FIFO) queue.
# The queue abstract data type (ADT)
# 6.2.2 Array-Based Queue Implementation
# For the stack ADT, we created a 

class ArrayQueue:
    ''' FIFO Queue implementation using a Python list as underlying storage. '''
    DEFAULT_CAPACITY = 5       # moderate capacity for all new queues

    def __init__(self):
        ''' Create an empty queue '''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0          # is an integer representing the current number of elements stored in the queue (as apposed to the length of the _data list)
        self._front = 0         # is an integer that represents the index with _data of the first element of the queue

    def __len__(self):
        ''' Return the number of elements in the queue. '''
        return self._size
    
    def is_empty(self):
        ''' Return True if the queue is empty. '''
        return self._size == 0
    
    def first(self):
        ''' Return (but do not remomve) the element at the front of the queue.
            Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        ''' Remove and return the first element of the queue (i.e. FIFO).
            Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        print('self._front is =>', self._front)
        print('self._data is =>', self._data)
        return answer
    
    def enqueue(self, e):
        ''' Add an element to the back of queue.'''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))                  # double the array size
        # avail => the right index to add new element
        avail = (self._front + self._size) % len(self._data) # adding element to circular queue
        print('avail is =>', avail) 
        self._data[avail] = e
        print('self._data is =>', self._data)
        self._size += 1
    
    def _resize(self, cap):
        ''' Resize to a new list of capacity >= len(self). '''
        old = self._data                                    # keep track of existing list
        self._data = [None] * cap                           # allocate list with new capacity
        walk = self._front
        for k in range(self._size):                         # only consider existing elements
            self._data[k] = old[walk]                       # intentionaly shift indices
            walk = (1 + walk) % len(old)                    # use old size as modules
        self._front = 0




# 6.3 Double-Ended Queues
# queue-like structure that supports insertions and deletion at both the front and the back of the queue.
# Such structure is called a "double-ended queue", "deque"
# The deque abstract data type (ADT) is more general than both the stack and queue ADTs.

class DeQue :
    DEFAULT_CAPACITY = 5

    def __init__(self):
        '''Create an empty queue '''
        self._data = [None] * DeQue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._back = 0

    def __len__(self):
        ''' Return the number of elements in the queue.'''
        return self._size
    
    def is_empty(self):
        ''' Return True if the queue is empty.'''
        return self._size == 0
    
    def first(self):
        ''' Return (but do not remomve) the element at the front of the queue.
            Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    
    def last(self):
        ''' Return (but do not remomve) the element at the end of the queue.
            Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._back]
    
    def add_last(self, e):
        ''' Add an element to the back of queue.'''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))                  # double the array size
        # avail => the right index to add new element
        avail = (self._front + self._size) % len(self._data) # adding element to circular queue
        self._data[avail] = e
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data)
    

    def add_first(self, e):
        ''' Add an element to the front of the queue. '''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))                  # double the array size
        # avail => the right index to add new element
        if self._data[self._front] :
            self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data)
    
    def delete_last(self):
        ''' Remove and return the last element of the queue.
            Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._back]
        self._data[self._back] = None # help garbage collection
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def delete_first(self):
        ''' Remove and return the first element of the queue (i.e. FIFO).
            Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        self._back = (self._front + self._size - 1) % len(self._data)
        return answer

    def _resize(self, cap):
        ''' Resize to a new list of capacity >= len(self). '''
        old = self._data                                    # keep track of existing list
        self._data = [None] * cap                           # allocate list with new capacity
        walk = self._front
        for k in range(self._size):                         # only consider existing elements
            self._data[k] = old[walk]                       # intentionaly shift indices
            walk = (1 + walk) % len(old)                    # use old size as modules
        self._front = 0

# Python's array-based list class, 
# a call to insert or pop with index k uses 