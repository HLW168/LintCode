class DoubleListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Dequeue:
    
    def __init__(self):
        self.head = None
        self.tail = None

    """
    @param: item: An integer
    @return: nothing
    """
    def push_front(self, item):
        if not self.head and not self.tail:
            self.init_node(item)
        else:
            node = DoubleListNode(item)
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev = node
            node.prev.next = node
            self.head = node
        print("push_front: ", self.head.val, self.tail.val)

    """
    @param: item: An integer
    @return: nothing
    """
    def push_back(self, item):
        if not self.head and not self.tail:
            self.init_node(item)
        else:
            node = DoubleListNode(item)
            node.prev = self.tail
            node.next = self.tail.next
            self.tail.next = node
            node.next.prev = node
            self.tail = node
        print("push_back: ", self.head.val, self.tail.val)

    """
    @return: An integer
    """
    def pop_front(self):
        if self.head == self.tail:
            return self.delete_node().val
        else:
            node = self.head
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next
            print("pop_front: ", self.head.val, self.tail.val)
            return node.val

    """
    @return: An integer
    """
    def pop_back(self):
        if self.head == self.tail:
            return self.delete_node().val
        else:
            node = self.tail
            self.tail.prev.next = self.tail.next
            self.tail.next.prev = self.tail.prev
            self.tail = self.tail.prev
            print("pop_back: ", self.head.val, self.tail.val)
            return node.val

    def init_node(self, item):
        node = DoubleListNode(item)
        node.prev = node
        node.next = node
        self.head = node
        self.tail = node

    def delete_node(self):
        node = self.head
        self.head = self.tail = None
        return node
