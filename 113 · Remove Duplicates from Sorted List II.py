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
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head

        #双指针
        prev = dummy
        curr = head

        while curr and curr.next:
            if curr.next and curr.next.val != curr.val:
                curr = curr.next
                prev = prev.next
                continue

            # duplicates
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next

            # remove the first duplicates
            prev.next = prev.next.next
        
        return dummy.next
