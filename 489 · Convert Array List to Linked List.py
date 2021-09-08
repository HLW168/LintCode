"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: nums: an integer array
    @return: the first node of linked list
    """
    def toLinkedList(self, nums):
        # write your code here
        dummy = ListNode(0)
        prev = dummy
        nums.reverse()
        for i in range(len(nums)):
            number = nums.pop()
            current = ListNode(number)
            prev.next = current
            prev = prev.next
        
        return dummy.next
