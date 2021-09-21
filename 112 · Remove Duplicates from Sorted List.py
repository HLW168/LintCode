"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None: return head

        dummy = ListNode(0)
        dummy.next = head
        
        left = head
        right = head.next

        while right:
            if right.val == left.val:
                left.next = right.next
                right = right.next
            else:
                left = right
                right = right.next

        return dummy.next
