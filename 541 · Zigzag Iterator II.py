import collections
class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        self.queue = collections.deque([])
        self.vecs = vecs
        for row, vec in enumerate(vecs):
            if vec:
                self.queue.append((row,0))

    """
    @return: An integer
    """
    def _next(self):
        # write your code here
        if not self.hasNext():
            return -sys.maxsize
        row, col = self.queue.popleft()
        result = self.vecs[row][col]
        if col+1 < len(self.vecs[row]):
            self.queue.append((row, col+1))
        return result

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.queue) > 0

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result
