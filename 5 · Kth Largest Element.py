class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, k, nums):
        # write your code here
        n = len(nums)
        # 將 k 轉換為 第 k 小
        k = n-k
        return self.partition(nums, 0, n-1, k)

    def partition(self, nums, start, end, k):
        # left, right 從 start 和 end 開始
        left, right = start, end
        # pivot 從左邊開始，因為是第 k 小
        pivot = nums[left]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        if k <= right:
            # 找 start - right
            return self.partition(nums, start, right, k)
        if k >= left:
            # 找 left - end
            return self.partition(nums, left, end, k)
        return nums[k]
