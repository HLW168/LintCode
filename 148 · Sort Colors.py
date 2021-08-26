class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        # 先處理 0 到 左邊 (以 1 當 pivot)
        start = self.pivot_partition(nums, 1, 0)
        # 再處理 1 到 左邊 (以 2 當 pivot)
        self.pivot_partition(nums, 2, start)

    def pivot_partition(self, nums, pivot, start):
        left, right = start, len(nums)-1 # 用 index

        # 先討論 不用移動的情況
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1    
        #討論需要移動的情況
            if left <= right:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right -= 1
        return left
