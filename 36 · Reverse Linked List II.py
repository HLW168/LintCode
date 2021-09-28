"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        
        # two pointers
        p1 = dummy
        p2 = head

        # 前進 m-1 步，紀錄 m-1 和 m
        for i in range(m-1):
            p1 = p1.next
            p2 = p2.next
        
        # 紀錄 m-1 & m
        p1_frozen = p1
        p2_frozen = p2

        # 前進至m
        p1 = p1.next
        p2 = p2.next

        # reversed
        for i in range(n-m):
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

        p1_frozen.next = p1
        p2_frozen.next = p2

        return dummy.next

