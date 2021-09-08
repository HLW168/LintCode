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
    @return: Head node.
    """
    def removeDuplicates(self, head):
        # write your code here
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        map = {}

        while curr.next:
            if not (map.get(curr.next.val)):
                map[curr.next.val] = 1
                curr = curr.next
            else:
                curr.next = curr.next.next
        
        return dummy.next
