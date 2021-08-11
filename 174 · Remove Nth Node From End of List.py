"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        # edge cases
        if head is None or n <= 0: return head

        # 快慢指針
        dummy = ListNode(None)
        dummy.next = head
        slow = dummy
        fast = dummy

        # 讓快指針跟慢指針差 n - 1
        for i in range(n):
            fast = fast.next
           
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next
