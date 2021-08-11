"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: An integer list
    """
    def toArrayList(self, head):
        # write your code here
        List = []
        curr = head
        while curr:
            List.append(curr.val)
            curr = curr.next
        return List
