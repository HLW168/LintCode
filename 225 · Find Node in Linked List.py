"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: the head of linked list.
    @param: val: An integer.
    @return: a linked node or null.
    """
    def findNode(self, head, val):
        # write your code here
        curr = head
        while curr:
            if curr.val != val:
                curr = curr. next
            else:
                break
        return curr

       
