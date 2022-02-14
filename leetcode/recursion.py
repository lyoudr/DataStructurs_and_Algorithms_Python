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

# Merge Two Sorted Lists

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
        