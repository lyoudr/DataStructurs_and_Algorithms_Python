### 2.1.1 Object-Oriented Design Goals
# 1. Robust
# 2. Adaptability => Software, needs to be able to evolve over time in response to changing conditions in its environment. (evolvability)
# 3. Reusability => Going hand in 

### 2.1.2 Object-Oriented Design Principles
# 1. Modularity 
# 2. Abstraction
# 3. Encapsulation 
# Different components of a software system should not reveal the internal details of their re


# (1) patterns for solving "algorithm design problems".
# Recursion
# Amortization
# 
# (2) patterns for solving software engineering problems.


# Class-Responsibility-Collaborator (CRC) cards
# action => responsibbility
# actor => component 


# 1 actor is responsible for several actions
# ex. actor A : action a, action b, action c

# CamelCase naming class name
# For documentation => docstring 

def scale(data, factor):
    """Multiply all entries of numeric data list by the given factor.

    data    an instance of any mutable sequence type (such as a list)
            containing numeric elements
    
    factor  a number that serves as the multiplicative factor for scaling
    """
    for j in range(len(data)):
        data[j] *= factor

    return data

# print('__name__ is =>', __name__)
# if __name__ == '__main__':
#     result = scale([1, 2, 3], 2)
#     print('result is =>', result)


class CreditCard:
    '''A consumer credit card.'''

    def __init__(self, customer, bank, acnt, limit):
        '''Create a new credit card instance.

        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        '''

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self):
        '''Return name of the customer'''
        return self._customer
    
    def get_bank(self):
        '''Return the bank's name'''
        return self._bank
    
    def get_account(self):
        '''Return the card identifying number(typically stored as a string)'''
        return self._account
    
    def get_limit(self):
        '''Return current credit limit.'''
        return self._limit
    
    def get_balance(self):
        '''Return current balance'''
        return self._balance
    

    def charge(self, price):
        '''Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        '''
        if price + self._balance > self._limit:       # if charge would exceed limit.
            return False                              # cannot accept charge
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        '''Process customer payment that reduces balance.'''
        self._balance -= amount
    
# method coverage => as each of the methods is called at least once,
# statement coverage => as there is never a case in which a charge is rejected due to the credit limit.

# if __name__ == '__main__':
wallet = []
wallet.append(CreditCard('John Bowman', 'California Savings',
                            '5391 0375 9387 5309', 2500))
# wallet.append(CreditCard('John Bowman', 'California Federal',
#                          '3485 0399 3395 1954', 3500))
# wallet.append(CreditCard('John Bowman', 'California Finance',
#                          '5391 0375 9387 5309', 5000))

for val in range(1, 17):
    wallet[0].charge(val)
    # wallet[1].charge(2*val)
    # wallet[2].charge(3*val)

for c in range(1):
    print('Customer =', wallet[c].get_customer())
    print('Bank =', wallet[c].get_bank())
    print('Account =', wallet[c].get_account())
    print('Limit =', wallet[c].get_limit())
    print('Balance =', wallet[c].get_balance())

    while wallet[c].get_balance() > 100:
        wallet[c].make_payment(100)
        print('New balance =', wallet[c].get_balance())


class Vector:
    '''Represent a vector in a multidimensional space.'''

    def __init__(self, d):
        '''Create d-dimensional vector of zeros.'''
        self._coords = [0] * d
    

    def __len__(self):
        '''Return the dimension of the vector.'''
        return len(self._coords)
    
    def __getitem__(self, j):
        '''Return jth coordinate of vector.'''
        return self._coords[j]

    def __setitem__(self, j, val):
        '''Set jth coordinate of vector to given value.'''
        self._coords[j] = val
    
    def __add__(self, other):
        '''Return sum of two vectors.'''
        if len(self) != len(other):                         # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))                          # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        '''Return True if vector has same coordinates as other.'''
        return self._coords == other._coords
    
    def __ne__(self, other):
        '''Return True if vector differs from other.'''
        return not self == other                            # rely on existing __eq__ definition
    
    def __str__(self):
        '''Produce string representation of vector.'''
        return '<' + str(self._coords)[1:-1] + '>'          # adapt list representation

# 2.3.3 Iterators 
# Iteration is an important concept in the design of data structures.

# In short, an iterator for a collection provides one key behavior.
# It supports a special method named "__next__" that returns the next element of the collection.

# Fortunately, it is rare to have to directly implement an iterator class.
# Our preferred approach is the use of "generator" syntax, which automatically produces an iterator of yielded values.

class SequenceIterator:
    '''An iterator for any of Python's sequence types.'''
    
    def __init__(self, sequence):
        '''Create an iterator for the given sequence.'''
        self._seq = sequence                                # keep a reference to the underlying data
        self._k = -1                                        # will increment to 0 on first call to next
    

    def __next__(self):
        '''Return the next element, or else raise StopIteration error.'''
        self._k += 1                                        # advance to next index
        if self._k < len(self._seq):
            return(self._seq[self._k])                      # return the data element
        else:
            raise StopIteration()
    
    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator.'''
        return self

class Range:
    '''A class that mimic's the built-in range class.'''

    def __init__(self, start, stop = None, step = 1):
        '''Initialize a Range Instance

        Semantics is similar to built-in range class.
        '''
        if step == 0:
            raise ValueError('step cannot be 0')
        
        if stop is None:                                   # special case of range(n)
            start, stop = 0, start
        
        # calculate the effective length core
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    
    def __len__(self):
        '''Return number of entries in the range.'''
        return self._length
    

    def __getitem__(self, k):
        '''Return entry at index k (using standard interpretation if negative).'''
        if k < 0:
            k += len(self)                                # attempt to convert negative index
        
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step

# overrides an existing method
# extend its superclass 



## 2.4 Inheritance
# 2.4.1 Extending the CreditCard Class
class PredatoryCreditCard(CreditCard):
    '''An extension to CreditCard that compounds interest and fees.'''

    def __init__(self, customer, bank, acnt, limit, apr):
        '''Create a new predatory credit card instance.
        
        The initial balance is zero.

        customer       the name of the customer (e.g., 'John Bowman')
        bank           the name of the bank (e.g., 'California Savings')
        acnt           the acount identifier (e.g., '5391 0375 9387 5309')
        limit          credit limit (measured in dollars)
        apr            annual percentage rate (e.g., 0.0825 for 8.25% APR)
        '''
        super().__init__(customer, bank, acnt, limit)          # call super constructor
        self._apr = apr
    

    def charge(self, price):
        '''
        Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        '''
        success = super().charge(price)                       # call inherited method
        if not success:
            self._balance += 5                                # assess penalty
        return success                                        # caller expects return value
    

    def process_month(self):
        '''Assess monthly interest on outstanding balance.'''

        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

# Progression class implements the conventions of a Python iterator, 
# namely the special "__next__" and "__iter__" methods.
# _advance to update the value of the self._current field.
class Progression:
    '''Iterator producing a generic progression.
    
    Default iterator produces the whole numbers 0, 1, 2, ...
    '''

    def __init__(self, start = 0):
        '''Initialize current to the first value of the progression.'''
        self._current = start
    
    def _advance(self):
        '''Update self._current to a new value.
        
        This should be overridden by a subclass to customize progression.

        By convention, if current is set to None, this designates the end of a finite progression.
        '''
        self._current += 1
    
    def __next__(self):
        '''Return the next element, or else raise StopIteration error.'''
        if self._current is None:             # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current            # record current value to return 
            self._advance()                   # advance to prepare for next time
            return answer                     # return the answer
    
    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator.'''
        return self
    

    def print_progression(self, n):
        '''Print next n values of the progression.'''
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):            # inherit from Progression
    '''Iterator producing an arithmetic progression.'''

    def __init__(self, increment = 1, start = 0):
        '''Create a new arithmetic progression.

        increment     the fixed constant to add to each term (default 1)
        start         the first term of the progression (default 0)
        '''
        super().__init__(start)                      # initialize base class
        self._increment = increment
    
    def _advance(self):
        '''Update current value by adding the fixed increment.'''
        self._current += self._increment


class GeometricProgression(Progression):             # inherit from Progression
    '''Iterator producing a geometric progression.'''

    def __init__(self, base = 2, start = 1):
        '''Create a new geometric progression.
        
        base          the fixed constant multiplied to each term (default 2)
        start         the first term of the progression (default 1)
        '''
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        '''Update current value by multiplying it by the base value.'''
        self._current *= self._base



class FibonacciProgression(Progression):
    '''Iterator producing a generalized Fibonacci progression.'''

    def __init__(self, first = 0, second = 1):
        '''Create a new fibonacci progression.
        
        first      the first term of the progression (default 0)
        second     the second term of the progression (default 1)
        '''
        super().__init__(first)                     # start progression at first
        self._prev = second - first
    

    def _advance(self):
        '''Update current value by taking sum of previous two.'''
        self._prev, self._current = self._current, self._prev + self._current


# 2.4.3 Abstract Base Classes
# we say a class is an "abstract base class" if its only purpose is to serve as a base class through inheritance
# More formally, an "abstract base" class is one that cannot be directly instantiated .
# "Concrete class" is one that can be instantiated.
# tempelate method pattern => is when an abstract base class provides concrete behaviors that rely upon 

from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
    '''Our own version of collections.Sequence abstract base class.'''

    @abstractmethod  # The second advanced technique is the use of the @abstractmethod decorator immediately before the __len__ and __get__item
    def __len__(self):
        '''Return the length of the sequence.'''
    
    @abstractmethod
    def __getitem__(self, j):
        '''Return the element at index j of the sequence.'''
    
    def __contains__(self, val):
        '''Return True if val found in the sequence; False otherwise.'''
        for j in range(len(self)):
            if self[j] == val:
                return True
        raise ValueError('value not in sequence')
    
    def index(self, val):
        '''Return leftmost index at which val is found (or raise ValueError)'''
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')       # never found a match
    
    def count(self, val):
        '''Return the number of elements equal to given value'''
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

# Nested Classes
# Nesting one class in the scope of another makes clear that the nested class exists for support of the outer class.