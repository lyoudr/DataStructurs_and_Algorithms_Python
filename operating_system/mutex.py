"""
Mutext Lock
"""

from multiprocessing import Process, Array, Value

def acquire(available):
    while not available.value :
        pass
    available.value = False


def release(available):
    available.value = True



def main_func(available, num, shared_v):
    while True:
        # get lock
        acquire(available)

        # critical section
        shared_v.value = num
        print('shared_v is =>', shared_v.value)

        # release lock
        release(available)


if __name__ == '__main__':
    available = Value('i', True)
    shared_v = Value('i', 1)
     
    p1 = Process(target = main_func, args = (available, 1, shared_v))
    p2 = Process(target = main_func, args = (available, 2, shared_v))
    p3 = Process(target = main_func, args = (available, 3, shared_v))
    
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

