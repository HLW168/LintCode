"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        # edge cases
        if head is None: return None

        # dummy Node
        dummy = ListNode(0)
        dummy.next = head
        
        # 去除多餘的迴圈
        length = self.get_length(head)
        k = k % length
        
        # 快慢指針
        slow = dummy
        fast = dummy
        
        # 讓快指針差 k 步
        for i in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # 斷開重組
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None

        return dummy.next

    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
