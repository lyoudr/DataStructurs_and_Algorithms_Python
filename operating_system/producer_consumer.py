from multiprocessing import Process, Lock, Array, Value
import os

def info():
    print('process id:', os.getpid())

def f(l , i):
    info()
    l.acquire()
    print('hello world', i)
    l.release()

def producer(buffer, counter, buffer_size, in_index):
    run_times = 0
    while True :
        next_produced = 1
        while counter.value == buffer_size.value : 
            pass
        
        print('in_index is =>', in_index.value)
        buffer[in_index.value] = next_produced; 
        in_index.value = (in_index.value + 1) % buffer_size.value; 
        counter.value = counter.value + 1
        run_times = run_times + 1
        if  run_times > 5:
            print("producer is exiting...")
            return
        

def consumer(buffer, counter, buffer_size, out_index):
    run_times = 0
    while True:
        while counter.value == 0:
            pass
        
        print('out_index is =>', out_index.value)
        buffer[out_index.value] = 0 # consume item in buffer[out_index]
        out_index.value = (out_index.value + 1) % buffer_size.value
        counter.value = counter.value - 1
        run_times = run_times + 1
        if run_times > 5:
            print("consumer is exiting...")
            return

if __name__ == '__main__':
    # lock = Lock()
    buffer = Array('i', range(5))
    counter = Value('i', 0)
    buffer_size = Value('i', 5)
    in_index = Value('i', 0)
    out_index = Value('i', 0)
    pro = Process(target = producer, args=(buffer, counter, buffer_size, in_index))
    con = Process(target = consumer, args=(buffer, counter, buffer_size, out_index))

    pro.start()
    con.start()

    pro.join()
    con.join()


    