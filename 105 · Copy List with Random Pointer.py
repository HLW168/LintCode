"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        # 利用 hash map 來建立映射關係 (node -> new node)
        # 然後再 copy 所有 node 的 next 以及 random pointer
        if not head:
            return None
        
        # mapping the node to new node
        map = {}
        curr = head
        while curr:
            # curr 配對的 label
            map[curr] = RandomListNode(curr.label)
            curr = curr.next
        
        # copy the next and random pointer
        for node in map:
            if node.next:
                # 把 node 的下一位指向 node.next 的 label
                map[node].next = map[node.next]
            if node.random:
                map[node].random = map[node.random]
        
        return map[head]
