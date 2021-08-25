class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        self.tmp = [0] * len(A)
        self.merge_sort(A, 0, len(A)-1)

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        #分開排序
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        #合併
        self.merge(nums, left, right)

    def merge(self, nums, left, right):
        mid = (left + right) // 2
        i, j = left, mid + 1
        for k in range(right-left+1):
            if i <= mid and (j > right or nums[i] <= nums[j]):
                self.tmp[k] = nums[i]
                i += 1
            else:
                self.tmp[k] = nums[j]
                j += 1
        for k in range(right-left+1):
            nums[left+k] = self.tmp[k]
