"""
Semaphore S 
1. is an integer variable that, apart from initialization, is accessed only through two standard atomic operations : wait() and signal()

"""
from multiprocessing import Process, Array, Value

# acquire symaphore

def wait(synch):
    while (synch.value <= 0):
        pass
    synch.value = synch.value - 1


def signal(synch):
    synch.value = synch.value + 1


def main_func(synch, num, shared_v):
    while True:
        # get symaphore
        wait(synch)

        # critical section
        shared_v.value = num
        print('shared_v.value is =>', shared_v.value)

        # release symaphore
        signal(synch)


if __name__ == '__main__':
    synmaphore = Value('i', 1)
    shared_v = Value('i', 1)
     
    p1 = Process(target = main_func, args = (synmaphore, 1, shared_v))
    p2 = Process(target = main_func, args = (synmaphore, 2, shared_v))
    p3 = Process(target = main_func, args = (synmaphore, 3, shared_v))
    
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


# 1. Producer and Consumer problem

def producer(buffer, in_index, empty, full, mutex):
    while True:
        next_prod = 1
        wait(empty)
        wait(mutex)

        buffer[in_index.value] = next_prod
        print('in_index.value is =>', in_index.value)
        print('buffer[in_index.value] is =>', buffer[in_index.value])
        in_index.value = (in_index.value + 1) % 5

        signal(mutex)
        signal(full)

def consumer(buffer, out_index, empty, full, mutex):
    while True:
        wait(full)
        wait(mutex)

        buffer[out_index.value] = 0
        print('out_index.value is =>', out_index.value)
        print('buffer[out_index.value] is =>', buffer[out_index.value])
        out_index.value = (out_index.value + 1) % 5

        signal(mutex)
        signal(empty)


# if __name__ == '__main__':
#     buffer = Array('i', range(5))
#     in_index = Value('i', 0)
#     out_index = Value('i', 0)

#     empty = Value('i', 5)
#     full = Value('i', 0)
#     mutex = Value('i', 1)
     
#     producer = Process(target = producer, args = (buffer, in_index, empty, full, mutex))
#     consumer = Process(target = consumer, args = (buffer, out_index, empty, full, mutex))
    
    
#     producer.start()
#     consumer.start()

#     producer.join()
#     consumer.join()


# 2. reader-writer problem





