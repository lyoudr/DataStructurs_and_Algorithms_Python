# 5.3 Dynamic Arrays and Amortization
# Code Fragment 5.1: An experiemnt to explore the relationship between a list's length and its underlying size in Python
import sys
def define_size(n):
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)

# Exercise 
# R-5.2: Redesign the experiment so that the program outputs only those values of k 
# at which the existing capacity is exhausted. For example, on a system consistent with the results of Code Fragment 5.2
# your program should output that the sequence of array capacities are 0, 4, 8, 16, 25     
def output_define_size(n):
    data = []
    cur_size = sys.getsizeof(data)
    output_index = []
    for k in range(n):
        data_size = sys.getsizeof(data)
        if data_size != cur_size:
            output_index.append(k-1)
            cur_size = data_size
        data.append(None)
    return output_index

# R-5.3 Modify the experiment from Code Fragment 5.1 in order to demonstrate that Python's list
# class occasionally shrinks the size of its underlying array 
# when elements are poped from a list
def shrink(n):
    data = [None] * n
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.pop()


import ctypes
# Code Fragment 5.3
class DynamicArray:
    '''A dynamic array class akin to a simplified Python list.'''

    def __init__(self):
        '''Create an empty array.'''
        self._n = 0                                   # count actual elements
        self._capacity = 1                            # default array capacity
        self._A = self._make_array(self._capacity)    # low-level array
    
    def __len__(self):
        '''Return number of elements stored in the array.'''
        return self._n
    
    def append(self, obj): # O(n)
        '''Add object to end of the array.'''
        if self._n == self._capacity:                 # not enough room
            self._resize(2 * self._capacity)          # so double capacity
        self._A[self._n] = obj                        # O(1)                  
        self._n += 1
    
    def __getitem__(self, k):
        '''Return element at index k.'''
        if 0 <= k < self._n:
            return self._A[k]                             # retrieve from array
        elif 0 >= k > -self._n:
            return self._A[self._n - abs(k)]
        else:
            raise IndexError('invalid index')


    def _resize(self, c): # O(n)                      # nonpublic utitity
        '''Resize internal array to capacity c.'''
        B = self._make_array(c)                       # new (bigger) array
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B                                   # use the bigger array
        self._capacity = c                            # set capacity to double size

    def _improved_resize(self, c):
        B = self._make_array(c)
        B[:self._n] = self._A[:]

    def _make_array(self, c):                         # nonpublic utility
        '''Return new array with capacity c.'''
        return (c * ctypes.py_object)()               # make an array with capacity     

    def insert(self, k, value):
        '''Insert value at index k, shifting subsequent values rightward.'''
        if self._n == self._capacity:                 # not enough room
            self._resize(2 * self._capacity)          # so double capacity
        for j in range(self._n, k, -1):               # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1                                  # store newest element

    def remove(self, value):
        '''Return first occurrence of value (or raise ValueError).'''
        # note : we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value :                  # found a match !
                for j in range(k, self._n - 1):       # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None           # help garbage collection
                self._n -= 1                          # we have one less item
                return
        raise ValueError('value not found')           # only reached if no match

    def show(self):
        for index in range(0, self._n):
            print(self._A[index])

# Exercises
# R-5.4 : Our DynamicArray class, as given in Code Fragment 5.3, does not support
# use of negative indices with __getitem__. Update that method to better 
# match the semantics of a Python list.
def __getitem__(self, k):
    '''Return element at index k.'''
    if 0 <= k < self._n:
        return self._A[k]                             # retrieve from array
    elif 0 >= k > -self._n:
        return self._A[self._n - abs(k)]
    else:
        raise IndexError('invalid index')

# R-5.6 Our implementation of insert for the DynamicArray class, as given in Code Fragment 5.5, 
# has the following inefficiency. In the case when a re- size occurs, 
# the resize operation takes time to copy all the elements from an old array to a new array, 
# and then the subsequent loop in the body of insert shifts many of those elements. 
# Give an improved implementation of the insert method, so that, 
# in the case of a resize, the elements are shifted into their final position during that operation, 
# thereby avoiding the subsequent shifting.
def _improved_resize(self, c):
    B = self._make_array(c)
    B[:self._n] = self._A[:]


# R-5.7 Let A be array of size n >= 2 containing integers from 1 to n-1, inclusive, with exactly one repeated.
# Describe a fast algorithm for finding the integer in A that is repeated
def find_repeat(A):
    record = {}
    for i in A:
        if not record.get(i):
            record[i] = True
        else:
            return i 
    return None

# 5.3.2 Amortized Analysis of Dynamic Arrays  
# However, notice that by doubling the capacity during an array replacemment, our new array allows us to add n new 
# This fact allows us to show that performing a series of operations on an initially empty dynamic array is efficient in terms of its total running time.

# Using an algorithm design pattern called "amortization", we can show that performing a 
# Thus, the total amount of cyber-dollars spent for any computation will be proportional to the total time spent on that 
# Proposition 5.1: Let S be a sequence implemented by means of a dynamic array with initial capacity one,

# Justification : Let us assume that one cyber-dollar is enough to pay for the execution of each append operation in S
# An overflow occurs when the array S has 2i elements
# That is, we can pay for the execution of n append operations using 3n cyber-dollars
# In other words, the amortized running time of each append ope O(n)

# Geometric Increase in Capacity
# Although the proof of Porposition 5.1 relies on the array being doubled each time
# With a base of 2 ()
# The key to perfomance is that the amount of additional space is proportional to the current size of the array.
# Using a fixed increment 
# Proposition 5.2: Performing a series of n append operations on an initially empty dynamic array using a fixed increment with each resize takes n2 time.
# Justification: Therefore, performing the n append operations takes n2 time.

# 5.3.3 Python's List Class 
# provide empirical evidence that Python's list class is using a form of dynamic arrays for its storage.
# With that said, it is clear that Python's implementation of the "append" method exhibits amortized constant-time behavior.
# We can get a more accurate measure of the amortized cost per operation by performing a series of n append operations on an initially empty list and determining the average cost of each.

from time import time                     # import time function from time module

def compute_average(n):
    '''Perform n appends to an empty list and return average time elapsed.'''
    data = []
    start = time()                        # record the start time (in seconds)    
    for k in range(n):
        data.append(None)
    end = time()                          # record the end time (in seconds)
    return (end - start) / n              # compute average per operation

# 5.4.1 Python's List and Tuple Classes
# The nonmutating behaviors of the "list"
# Constant-Time Operations
# The length of an instance is returned in constant time because an instance explicitly maintains such state information.

# Mutating Behaviors 

# list comprehension

# 5.5 Using Array-Based Sequences
# 5.5.1 Storing High Scores for a Game
# The first application we study is storing a sequence of high score entries for a video game.
# This is representative of many applications 
# We could just as easily have chosen to store records for patients in a hospital or the names of players on a football team.

class GameEntry:
    '''Represents one entry of a list of high scores.'''

    def __init__(self, name, score):
        self._name = name
        self._score = score
    
    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._score
    
    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)  # e.g., '(Bob, 98)'


class Scoreboard:
    '''Fixed-length sequence of high scores in nondecreasing order.'''
    def __init__(self, capacity = 10):
        '''
            Initialize scoreboard with given maximum capacity.
            All entries are initially None.
        '''
        self._board = [None] * capacity                      # reserve space for future scores
        self._n = 0
    

    def __getitem__(self, k):
        '''Return entry at index k.'''
        return self._board[k]
    
    
    def __str__(self):
        '''Return string representation of the high score list.'''
        return '\n'.join(str(self._board[j]) for j in range(self._n))
    

    def add(self, entry):
        '''Consider adding entry to high scores.'''
        score = entry.get_score()

        # Does new entry qualify as a high score ?
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):                     # no score drops from list
                self._n += 1                                   # so overall number increases
            
            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]              # shift entry from j-1 to j
                j -= 1
            self._board[j] = entry

# The Insertion-Sort Algorithm

# Algorithm InsertionSort(A):
# Input : An array A of n comparable elements
# Output : The array A with elements rearranged in nondecreasing order

def insertion_sort(A):
    '''Sort list of comparable elements into nondecreasing order.'''
    for k in range(1, len(A)):               # from 1 to n-1
        cur = A[k]                           # current element to be inserted
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur                       

# 5.5.3 Simple Cryptography

# This field studies ways of performing encryption, which takes a message, called the plaintext, and converts it into a scrammbled message, called ciphertext.
class CaesarCipher:
    '''Class for doing encryption and decryption using a Caesar cipher.'''

    def __init__(self, shift):
        '''Construct Caesar cipher using given integer shift for rotation'''
        encoder = [None] * 26                                # temp array for encryption
        decoder = [None] * 26                                # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)                     # will store as string
        self._backward = ''.join(decoder)                    # since fixed
    

    def encrypt(self, message):
        '''Return string representing encripted message.'''
        return self._transform(message, self._forward)
    

    def decrypt(self, secret):
        '''Return decrypted message given encrypted secret.'''
        return self._transform(secret, self._backward)
    

    def _transform(self, original, code):
        '''Utility to perform transformation based on given code string.'''
        msg = list(original)
        print('msg is =>', msg)
        for k in range(len(msg)):
            if msg[k].isupper():
                print('msg[k] is =>', msg[k])
                j = ord(msg[k]) - ord('A') 
                print('j is =>', j) 
                print('code[j] is =>', code[j])            # index from 0 to 25
                msg[k] = code[j]                           # replace this character
        return ''.join(msg)

# Mulidimensional Data Sets 
# Lists tuples, and strings in Python are one-dimensional. Many computer applications involve multidimensional data sets
# medical imaging may provide three-dimensional scans of a patient, and a company's valuation is often based upon a high number of in

# To properly initialize a two-dimensional list, we must ensure that each cell of the primary list refers to an "independent" instance of a secondary list.
# This can be accomplished through the use of Python's list comprehension syntax.

class TicTacToe:
    '''Management of a Tic-Tac-Toe game (does not do strategy).'''

    def __init__(self):
        '''Start a new game.'''
        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'X'
    

    def mark(self, i, j):
        '''Put an X or O mark at position (i,j) for next player's turn'''
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        
        self._board[i][j] = self._player

        if self._player == 'X':
            self._player = 'O'
        else :
            self._player = 'X'
    

    def _is_win(self, mark):
        '''Check whether the board configuration is a win for the given player.'''
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][0] == board[2][0] or
                mark == board[0][1] == board[1][1] == board[2][1] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0])
    
    def winner(self):
        '''Return mark of winning player, or None to indicate a tie.'''
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None
    
    def __str__(self):
        '''Return string representation of current game board.'''
        rows = [ '|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n' .join(rows)    