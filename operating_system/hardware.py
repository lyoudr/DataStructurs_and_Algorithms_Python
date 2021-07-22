"""
Hardware solution

"test_and_set" and "compare_and_swap" are atomic, which means that when two processes call these method simultaneously, this method will be conducted in sequence since they are uninterrpted.
supported by hardware
"""

from multiprocessing import Process, Value


def test_and_set(target):
    rv = target.value
    target.value = 1
    return rv


def compare_and_swap(lock, expected, new_value):
    temp = lock.value
    if lock.value == expected:
        lock.value = new_value
    return temp

                         
def func(con_val, lock, count):
    while True:
        while(compare_and_swap(lock, 0, 1) != 0): # while(test_and_set(lock)):
            pass # do nothing

        # critical section
        count.value = con_val
        print('count is =>', count.value)
        lock.value = 0

        # remainder section


if __name__ == '__main__':
    count = Value('c', 'n')
    lock = Value('i', 0)
    pi = Process(target = func, args = ('i', lock, count))
    pj = Process(target = func, args = ('j', lock, count))

    pi.start()
    pj.start()

    pi.join()
    pj.join()



