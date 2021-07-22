"""
Peterson's solution 
1. It is restricted to two processes.
2. It is satisfied the requirements of critical-section problem
    (1) Mutual exclusion : If process Pi is executing in its critical section, then no other processes can be executing in their critical section.
    (2) Progress : If no process is executing in its critical section and some processes wish to enter their critical sections, then only those processes that are not executing in their remainder sections can participate in deciding which will enter its critical section next, and this selection cannot be postponed indefinitely.
    (3) Bounded waiting : There exists a bound, or limit, on the number of times that other processes are allowed to enter their critical sections after a process has made a request to enter its critical section and before that request is granted.

"""

from multiprocessing import Process, Array, Value


def pi_process(flag, turn, count):
    print('I turn.value is =>', turn.value)
    while True:
        # Entry Section
        flag[0] = 1 # Pi is ready to go to its critical section
        turn = 1 # Pi give chance to Pj
        while flag[1] and turn == 1:
            pass # if Pj is ready to go to its critical section and turn is Pj, Pi waiting for Pj
        
        # Critical Section
        if turn == 0:
            count.value = count.value + 1
            print('turn is i, count is =>', count.value)
        if turn == 1:
            count.value = count.value - 1
            print('turn is j, count is =>', count.value)

        # Remainder Section
        flag[0] = 0

def pj_process(flag, turn, count):
    print('J turn.value is =>', turn.value)
    while True:
        # Entry Section
        flag[1] = 1 # Pj is ready to go to its critical section
        turn.value = 0 # Pj give chance to Pi
        while flag[0] and turn.value == 0:
            pass # if Pi is ready to go to its critical section and .value is Pi, Pj waiting for Pi
        
        # Critical Section
        if turn.value == 0:
            count.value = count.value + 1
            print('turn is i, count is =>', count.value)
        if turn.value == 1:
            count.value = count.value - 1
            print('turn is j, count is =>', count.value)

        # Remainder Section
        flag[1] = 0


if __name__ == '__main__':
    flag = Array('i', [0, 0])
    turn = Value('i', 0)
    count = Value('i', 0)
    i_pro = Process(target = pi_process, args = (flag, turn, count))
    j_pro = Process(target = pj_process, args = (flag, turn, count))

    i_pro.start()
    j_pro.start()

    i_pro.join()
    j_pro.join()


#### 6.6 Real-Time CPU Scheduling
# Soft real-time systems => provide no gurantee as to when a critical real-time process will be scheduled. They guarantee only that the process will be given preference over noncritical processes.
# Hard real-time systems => A task must be serivced by its deadline; service after the deadline has expired is the same as no service at all.

# Event Latency = Interrupt Latency + Dispatch Latency

# Interrupt Latency => the period of time from the arrival of an interrupt at the CPU to the start of the routine that services the interrupt

# Dispatch Latency => The amount of time required for the scheduling dispatcher to stop one process and start nother process
# 1. => conflict 
    # (1) Preemption of any process running in the kernel
    # (2) Release by low-priority processes of resources needed by a high-priority process
# 2. => dispatch

### 6.6.2 Priority-Based Scheduling 

# The most important feature of a real-time operating system is to respond immediately to a real-time process as soon as that process requires the CPU.
# preemptive, priority-based scheduler only guarantees soft real-time functionality.
# Hard real-time systems must further guarantee that real-time tasks will be serviced in accord with their deadline requirements
    # (1) the processes are considered "periodic" , that is, they require the CPU at constant intervals (periods).
    # (2) t => fixed processing time 
    # (3) d => deadline
    # (4) p => period
    # 0 <= t <= d <= p

    # a process may have to announce its deadline requirements to the scheduler.
    # "Admission-control" algorithm => the schedular does one of two things => 
        # (a) admits the process, guaranteeing that the process will complete on time.
        # (b) rejects the request as impossible if it cannot guarantee that the task will be serviced by its deadline.

