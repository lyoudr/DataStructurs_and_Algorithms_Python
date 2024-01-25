from typing import Optional
# 21. Merge Two Sorted Lists
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode()
        current = dummy

        # Iterate through both lists until one of them is exhausted
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next 
        
            # Move the current pointer to the last merged node
            current = current.next

        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2
        
        return dummy.next
