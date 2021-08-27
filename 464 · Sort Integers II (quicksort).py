class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if A is None or len(A) == 0: return
        self.quickSort(A, 0, len(A)-1)

    def quickSort(self, A, start, end):
        # 出口
        if start >= end: return

        # partition
        pivot = A[(start + end)//2]
        left, right = start, end

        while left <= right:
            while left <= right and A[left] < pivot:
                # 不用動
                left += 1
            while left <= right and A[right] > pivot:
                # 不用動
                right -= 1
            if left <= right:
                # 需要交換
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
