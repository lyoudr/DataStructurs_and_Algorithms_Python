# base cases n = 0
# It also contains one or more recursive cases,
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
"""
    A recursion trace closely mirrors the programming language's execution of the recursion.
    In Python, each time a function (recursive or otherwise) is called, a structure known as an 
    'activation record' or 'frame' is created to store information about the progress of that invocation of the function.
    recursive case in which a function invokes itself. 
"""
# factorial function
"""
    {
        1
        n * (n-1)!
    }
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

"""
Binary Search
"""
def binary_search(low, high, S, target):
    if low < high:
        mid = (low + high) // 2
        if S[mid] == target:
            return True
        elif S[mid] < target: 
            return binary_search(mid + 1, high, S, target)
        elif S[mid] > target:
            return binary_search(low, mid - 1, S, target)
    else:
        return False

"""
Cumulative disk space usage
"""
import os 
def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(path, childpath)
    return total

# C-4.9 Write a short recursive Python function that finds the minimum and maximum values in a sequences without using any loops
def recursion(S, i, min_v, max_v):
    if i == (len(S)):
        print('min_v is ->', min_v)
        print('max_v is ->', max_v)
        return min_v, max_v
    else:
        print('S[i] is ->', S[i])
        if S[i] < min_v:
            return recursion(S, i+1, S[i], max_v)
        elif S[i] > max_v:
            return recursion(S, i+1, min_v, S[i])
        else:
            return recursion(S, i+1, min_v, max_v)


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        self.merge(list1, list2)

    def merge(self, list1, list2, list3 = None):
        temp1 = list1
        temp2 = list2
        temp3 = list3
        if temp1 and temp2:
            if temp1.val > temp2.val:
                temp3 = self.append(temp3, temp2.val)
                temp2 = temp2.next
            else:
                temp3 = self.append(temp3, temp1.val)
                temp1 = temp1.next
            self.merge(temp1, temp2, temp3)
        elif temp1:
            temp3 = self.append(temp3, temp1.val)
            temp1 = temp1.next
            self.merge(temp1, temp2, temp3)
        elif temp2:
            temp3 = self.append(temp3, temp2.val)
            temp2 = temp2.next
            self.merge(temp1, temp2, temp3)
        return temp3

    def append(self, head, data):
        cur = head
        new_node = ListNode(data)

        if not head:
            head = new_node
            return head
        
        while cur.next:
            cur = cur.next

        cur.next = new_node
        return head


### ----------- Reinforcement --------
# R-4.1 Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements.
    # What is your running time and space usage ?
     