from typing import List


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.length = 0
        self.head = None

    def __len__(self):
        return self.length

    def count_length(self, node):
        self.length += 1
        if node.next:
            self.count_length(node.next)
        return self.length

    def rm_node(self, node, n, index):
        print('index is =>', index)
        if n == 1:
            self.head = node.next
        if index + 1 == n :
            node.next = node.next.next        # clear node
            print('node.val is =>', node.val)
            print('node.next.val is =>', node.next.val)
        elif index + 1 != n and node.next:
            index += 1
            self.rm_node(node.next, n, index)
        return None
    
    def display(self, node, res):
        res.append(node.val)
        if node.next:
            self.display(node.next, res)
        return res

    def removeNthFromEnd(self, head: List[ListNode], n : int) -> List[ListNode]:
        self.head = head
        length = self.count_length(self.head)
        print('length is =>', length)
        target_n = length - n + 1
        print('target_n is =>', target_n)
        self.rm_node(self.head, target_n, 1)
        return self.display(self.head, [])
