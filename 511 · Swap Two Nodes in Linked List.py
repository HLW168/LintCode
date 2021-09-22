"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head

        # find the index of v1 value
        prev_a, curr_a, index_a = self.find(dummy, v1)
        # find the index of v2 value
        prev_b, curr_b, index_b = self.find(dummy, v2)

        if not curr_a or not curr_b: 
            return head
        if index_a == index_b:
            return head

        prev_a.next = curr_b
        prev_b.next = curr_a

        curr_b.next, curr_a.next = curr_a.next, curr_b.next

        return dummy.next
    
    def find(self, dummy, target):
        prev = dummy
        curr = dummy.next
        index = 0
        while curr:
            if curr.val == target:
                return prev, curr, index
            prev = curr
            curr = curr.next
            index += 1
        return None, None, index
