"""
Dining-Philosophers Solutions Using Monitors
deadlock-free solution to the dining-philosophers
"""
from multiprocessing import Process, Array, Value

class DiningPhilosophers():
    state = Array('i', range(5))
    condition = Array('i', range(5))

    def pickup(self, index):
        self.state[index] = 'hungry'
        self.test(index)
        if self.state[index] != 'eating':
            self.condition[index].wait()
    
    def putdown(self, index):
        self.state[index] = 'thinking'
        self.test((index + 4) % 5)
        self.test((index + 1) % 5)

    def test(self, index):
        if self.state[index + 4] % 5 != 'eating' and self.state[index] == 'hungry' and self.state[index + 1] % 5 != 'eating':
            self.state[index] = 'eating'
            self.condition[index].signal()
    
    def init_code(self):
        for index in range(5):
            self.state[index] = 'thinking'
        

# conditional-wait => x.wait(c)

# A monitor to allocate a single resource

class ResourceAllocator:
    busy
    condition x

    def acquire(time):
        if busy:
            x.wait(time)
        busy = True
    
    def release():
        busy = False
        x.signal()
    
    def initialization_code():
        busy = False
    
      