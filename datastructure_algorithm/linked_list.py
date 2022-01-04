# 7.1 Singly Linked Lists
# A "singly linked list", in its simplest form, is a collection of nodes that collectively form a linear sequence.
# Each node stores a reference to an object that is an elemment of the sequence, as well as reference to the next node of the list

# Linked List does not have a predetermined fixed size;
# it uses space proportionally to its current number of elements.

# Inserting an Element at the Head of a Singly Linked List
def add_first(L, e):
    newest = Node(e)
    newest.next = L.head
    L.head = newest
    L.size = L.size + 1

def remove_fist(L):
    if L.head == None:
        raise Exception
    L.head = L.head.next
    L.size = L.size - 1

class Empty(Exception):
    '''Error attempting to access an element from an empty container.'''
    pass


# insert and delete elements in constant time only at the head of linked list.
class LinkedStack:
    ''' LIFO Stack implemmentation using a singly linked list for storage . '''

    # ------------------------------ nested _Node class -----------------------------
    class _Node:
        ''' Lightweight, nonpublic class for storing a singly linked node.'''
        __slots__ = '_element', '_next'

        def __init__(self, element, next):        # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node

    # ------------------------------ stack methods ---------------------------------
    def __init__(self):
        ''' Create an empty stack. '''
        self._head = None                         # reference to the head node
        self._size = 0
    
    def len(self):
        '''Return the number of elements in the stack.''' 
        return self._size

    def is_empty(self):
        ''' Return True if the stack is empty.''' 
        return self._size == 0
    
    def push(self, e):
        ''' Add element e to the top of the stack '''
        self._head = self._Node(e, self._head)    # create and link a new node
        self._size += 1
        self.traverse(self._head)
    
    def top(self):
        ''' 
            Return (but do not remmove) the element at the top of the stack.
            Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element                # top of stack is at head of list
    
    def pop(self):
        '''
            Remomve and return the element from the top of the stack (i.e. LIFO)
            Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next             # bypass the former top node
        self._size -= 1
        return answer
    
    def traverse(self, e):
        print('node is =>', e._element)
        if e._next:
            self.traverse(e._next)


class LinkedQueue : 
    ''' FIFO queue implementation using a singly linked list for storage. '''
    
    class _Node :
        ''' Lightweight, nonpublic class for storing a singly linked node.'''
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):        # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node
    
    def __init__(self):
        ''' Create an empty queue. '''
        self._head = None
        self._tail = None
        self._size = 0
        self._count = 0
    
    def __len__(self):
        ''' Return the number of elements in the queue. '''
        return self._size
    
    def is_empty(self):
        ''' Return True if the queue is empty. '''
        return self._size == 0
    
    def first(self):
        ''' Return (but do not remove) the element at the front of the queue. '''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
    
    def dequeue(self):
        ''' 
            Remove and return the first element of the queue (i.e., FIFO).
            Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        self.traverse(self._head)
        return answer
    
    def enqueue(self, e):
        ''' 
            Add an element to the back of queue.
        '''
        newest = self._Node(e, None)               # node will be new tail node
        if self.is_empty():
            self._head = newest                    # special case : previously empty
        else :
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        self.traverse(self._head)
    

    def traverse(self, e):
        if e:
            print('e._element is =>', e._element)
            if e._next:
                self.traverse(e._next)
        

    def count(self, node):
        self._count += 1
        if node._next:
            self.count(node._next)
        return self._count
    
    def find_node(self, node, element):
        if node._element != element:
            return self.find_node(node._next, element)
        return node

    def swap(self, x_value, y_value):
        node_x = self.find_node(self._head, x_value)
        node_y = self.find_node(self._head, y_value)
        node_x._element = y_value
        node_y._element = x_value
        self.traverse(self._head)
        
## 7.2.1 Round-Robin Schedulers
# 7.2.2 Implementing a Queue with a Circularly Linked List 
# CircularQueue class
# When enqueue is called, a new node is placed just after the tail but before the current head, 
# In addition to the traditional queue operations, the "CircularQueue" class supports a "rotate" method that more efficiently enacts the combination of removing the front element reinseting it at the back of the queue.

class CircularQueue:
    ''' Queue implementing using circularly linked list for storage. '''
    class _Node :
        ''' Lightweight, nonpublic class for storing a singly linked node.'''
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):        # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node
    
    def __init__(self):
        '''Create an empty queue'''
        self._tail = None                         # will represent tail of queue
        self._size = 0
    
    def __len__(self):
        ''' Return the number of elements in the queue. '''
        return self._size
    
    def is_empty(self):
        ''' Return True if the queue is empty.'''
        return self._size == 0
    
    def first(self):
        ''' 
            Return (but do not remove) the element at the front of the queue.
            Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        ''' 
            Remove and return the first element of the queue (i.e., FIFO)
            Raise Empty exception if the queue is empty
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next               
        
        if self._size == 1:                     # removing only element
            self._tail = None                   # queue becomes empty
        else :
            self._tail._next = oldhead._next    # bypass the old head
        self._size -= 1
        self.traverse(self._tail._next)
        return oldhead._element
    
    def enqueue(self, e):
        ''' Add an element to the back of queue. '''
        newest = self._Node(e, None)            # node will be new tail node
        if self.is_empty():
            newest._next = newest               # initialize circularly
        else :
            newest._next = self._tail._next     # new node points to head
            self._tail._next = newest           # old tail points to new node
        self._tail = newest
        self._size += 1
        self.traverse(self._tail._next)
    
    def rotate(self):
        ''' Rotate front element to the back of the queue. '''
        if self._size > 0:
            self._tail = self._tail._next       # old head becomes new tail
        self.traverse(self._tail._next)

    def traverse(self, e):
        print('e._element is =>', e._element)
        if e._next and e._element != self._tail._element:
            self.traverse(e._next)

    def the_same(self, node_x, node_y):
        print('node_x._element is =>', node_x._element)
        if node_x == node_y:
            print('in the same queue')
            return True
        else :
            self.the_same(node_x._next, node_y)


## 7.3 Doubly Linked Lists
# we define a linked list in which each node keeps an explicit reference to the node before it and reference to the node after it.
# Such a structure is known as a "doubly linked list"
# In order to avoid some special nodes at both ends of the list
# a "header" node at the beginning of the list
# a "trailer" node at the end
# These nodes are known as "sentinels" (or guards)
# and they do not store elements of the primary sequence.
# With array-based sequences, an integer index was a 


# 7.3.1 Basic Implementation of a Doubly Linked List 
class _DoublyLinkedBase:
    '''A base class providing a doubly linked list representation '''
    
    class _Node:
        ''' Lightweight, nonpublic class for storing a doubly linked node. '''
        __slots__ = '_element', '_prev', '_next'  # streamline memory

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        '''Create an empty list'''
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer                  # trailer is after header
        self._trailer._prev = self._header
        self._size = 0

    
    def __len__(self):
        '''Return the number of elements in the list.'''
        return self._size
    
    def is_empty(self):
        '''Return True if list is empty'''
        return self._size == 0

    def _insert_between(self, e, pred, succ):
        '''Add element e between two existing nodes and return new node. '''
        newest = self._Node(e, pred, succ) # linked to neighbors
        pred._next = newest
        succ._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        '''Delete nonsentinel node from the list and return its element.'''
        pred = node._prev
        succ = node._next
        pred._next = succ
        succ._prev = pred
        self._size -= 1
        element = node._element                            # record delete element
        node._prev = node._next = node._element = None     # deprecate node
        return element

## 7.3.2 Implementing a Deque with a Doubly Linked List
# The "double-ended queue (deque)", 就是可以在頭.尾新增或刪除元素的 queue

class LinkedDeque(_DoublyLinkedBase):
    '''Double-ended queue implementation based on a doubly linked list.'''
    def first(self):
        '''Return (but do not remove) the element at the front of the deque'''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element                            # real item just after header
    
    def last(self):
        '''Return (but do not remove) the element at the back of the deque'''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element                          # real item just before trailer
    
    def insert_first(self, e):
        '''Add an element to the front of the deque'''
        self._insert_between(e, self._header, self._header._next)    # after header
        self.traverse(self._header._next)


    def insert_last(self, e):
        '''Add an element to the back of the deque'''
        self._insert_between(e, self._trailer._prev, self._trailer)  # before trailer
        self.traverse(self._header._next)


    def delete_first(self):
        '''
            Remove and return the element from the front of the deque
            Raise Empty exception if the deque is empty.
        '''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)
        

    def delete_last(self):
        '''
            Remove and return the element from the back of the deque.
            Raise Empty exception if the deque is empty. 
        '''
        if self.is_empty():
            raise Empty("Deque is empty") 
        return self._delete_node(self._trailer._prev)
    
    def traverse(self, e):
        print('node element is =>', e._element)
        if e._next:
            self.traverse(e._next)

    # def swap(self, x_node, y_node):
    #     # For y to x
    #     x_node._prev._next = y_node
    #     x_node._next._prev = y_node

    #     # For x to y 
    #     y_node._prev._next = x_node
    #     y_node._next._prev = x_node
        
        
    #     self.traverse(self._header)

# In Linked List , If we want to specify specific position. We don't use index. Instead, we use the element
# 7.4.1 The Positional List Abstract Data Type
# A position acts as a marker or token within the broader positional list.
# A postion "p" is unaffected by changes elsewhere in a list

# p.element() : Return the element stored at position p.
# L : list L
# L.first() : Return the position of the first element of L, or None if L is empty.
# L.last() : Return the position of the last element of L, or None if L is empty.
# L.before(p) : Return the position of L immediately before position p, or None if p is the first position.
# L.after(p) : Return the position of L immediately after poisition p, or None if p is the last position.
# L.add_first(e) : Insert a new element e at the front of L, returning the position of the new element
# L.add_last(e) : Insert a new element e at the back of L, returning the position of the new element
# L.add_before(p, e) : Insert a new element e just before position p in L, returning the position of the new element.
# L.add_after(p, e) : Insert a new element e just after position p in L, returning the position of the new element.
# L.replace(p, e) : Replace the element at position p with element e, returning the element formerly at position p.
# L.delete(p) : Remomve and return the element at position p in L, invalidating the position.

class PositionalList(_DoublyLinkedBase):
    '''A sequential container of elements allowing positional access.'''

    # ---------------------------- nested Position class -----------------------------
    class Position : 
        ''' An abstraction representing the location of a single element.'''
        def __init__(self, container, node):
            '''Constructor should not be invoked by user.'''
            self._container = container
            self._node = node
        
        def element(self):
            '''Return the element stored at this Position.'''
            return self._node._element
        
        def __eq__(self, other):
            '''Return True if other is a Position representing the same location'''
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            '''Return True if other does not represent the same location.'''
            return not (self == other)                # opposite of __eq__
        
    # ---------------------------- utility method -------------------------------------
    def _validate(self, p):
        '''Return position"s node, or raise appropriate error if position is invalid.'''
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        '''Return Position instance for given node (or None if sentinel).'''
        if node is self._header or node is self._trailer:
            return None
        else :
            return self.Position(self, node)
    
    # ---------------------------- accessors ------------------------------------------

    def first(self):
        '''Return the first Position in the list (or None if list is empty).'''
        return self._make_position(self._header._next)
    
    def last(self):
        '''Return the last Position in the list (or None if list is empty).'''
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        '''Return the Position just before Position p (or None if p is first).'''
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        '''Return the Position just after Position p (or None if p is last).'''
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        '''Generate a forward iteration of the elements of the list.'''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ---------------------------- mutators ------------------------------------------
    def _insert_between(self, e, pred, succ):
        '''Add element between existing nodes and return new Position.'''
        node = super()._insert_between(e, pred, succ)
        return self._make_position(node)
    
    def add_first(self, e):
        '''Insert element e at the front of the list and return new Position.'''
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        '''Insert element e at the back of the list and return new Position.'''
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        '''Insert element e into list before Position p and return new Position.'''
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        '''Insert element e into list after Position p and return new Position.'''
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        '''Remove and return the element at Position p.'''
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p, e):
        '''
            Replace the element at Position p with e.
            Return the element formerly at Position p.
        '''
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

## Python code for performing insertion-sort on a positional list
# 7.5 Sorting a Positional List
 
def insertion_sort(L):
    ''' Sort PositionalList of comparable elements into nondecreasing order.'''
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)               # next item to place
            value = pivot.element()
            if value > marker.element():          # pivot is already sorted
                marker = pivot                    # pivot becomes new marker
            else :                                # must relocate pivot
                walk = marker                     # find leftmost item greater than value
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)         # reinsert value before walk


# 7.6 Case Study : Maintaining Access Frequencies
# favorites list ADT => "len" and "is_empty" methods
# access(e) : Access the element e, incrementing its access count, and adding it to the favorites list if it is not already present.
# remove(e) : Remove element e from the favorites list, if present.
# top(k) : Return an iteration of the k mmomst accessed elements.

# Using the "Composition Pattern"
# composition pattern => we define a single object that is composed of two or more other objects

class FavoritesList:
    '''List of elements ordered from most frequently accessed to least'''

    # ----------------------------------- nested _Item class --------------------------------
    class _Item:
        __slots__ = '_value', '_count'           # streamline memmory usage
        def __init__(self, e):
            self._value = e
            self._count = 0
    
    # ------------------------------------ nonpublic utilities ------------------------------
    def _find_postion(self, e):
        '''Search for element e and return its Position (or None if not found).'''
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk
    
    def _movmte_up(self, p):
        '''Move item at Position p earlier in the list based on access count.'''
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)

            if cnt > walk.element()._count :                                # must shift forward 
                while (walk != self._data.first() and
                       cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))           # delete/reinsert
    
    # ------------------------------------ public methods ----------------------------------
    def __init__(self):
        '''Create an empty list of favorites'''
        self._data = PositionalList()
    
    def __len__(self):
        '''Return number of entries on favorites lists.'''
        return len(self._data)
    
    def is_empty(self):
        '''Return True if list is empty'''
        return len(self._data) == 0
    
    def access(self, e):
        '''Access element e, thereby increasing its access count.'''
        p = self._find_postion(e)
        if p is None:
            p = self._data.add_last(self._Item(e))    # If new, place at end
        p.element()._count += 1                       # always increment count
        self._move_up(p)                              # consider momving forward
    
    def remove(self, e):
        '''Remmomve element e from the list of favorites.'''
        p = self._find_postion(e)                     # try to locate existing element
        if p is not None:
            self._data.delete(p)                      # delete, if found
    
    def top(self, k):
        '''Generate sequence of top k elements in terms of access count.'''
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)


# 7.6.2 Using a List with the Move-to-Front Heuristic
# Each time we access an element we move it all the way to the front of the list.
class FavoritesListMTF(FavoritesList):
    '''List of elements ordered with move-to-front heuristic.'''

    # we override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        '''Move accessed item at Position p to front of list.'''
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))                    # delete/reinsert
    
    # we override top because list is no longer sorted
    def top(self, k):
        '''Generate sequence of top k elements in terms of access count.'''
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        
        # we begin by making a copy of the original list
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)
        
        # we repeatedly find, report, and remove element with largest count
        for j in range(k):
            print('j is =>', j)
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            print('highPos.element()._value is =>', highPos.element()._value)
            # we have found the element with highest count
            yield (highPos.element()._value, highPos.element()._count)                             # report element to user
            temp.delete(highPos)