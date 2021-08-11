class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

class InterfaceQueue:
    def push(self, element):
        pass

    # define an interface for pop method
    # write your code here
    def pop(self):
        pass

    # define an interface for top method
    # write your code here
    def top(self):
        pass

class MyQueue(InterfaceQueue):
    # you can declare your private attributes here
    def __init__(self):
        # do initialization if necessary
        self.head = None
        self.tail = None
    # implement the push method
    # write your code here
    def push(self, val):
        new_tail = LinkedListNode(val)
        if self.head is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            if self.tail is None:
                self.head.next = new_tail
                self.tail = new_tail
            else:
                self.tail.next = new_tail
                self.tail = new_tail
    # implement the pop method
    # write your code here
    def pop(self):
        if self.head is not None:
            val = self.head.val
            self.head = self.head.next
            return val
        else:
            self.tail = None
            return -1
	# implement the top method
    # write your code here
    def top(self):
        if self.head is not None:
            return self.head.val
        else:
            return -1
        
# Your MyQueue object will be instantiated and called as such:
# MyQueue queue = new MyQueue();
# queue.push(123);
# queue.top(); will return 123;
# queue.pop(); will return 123 and pop the first element in the queue
