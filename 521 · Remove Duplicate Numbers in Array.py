class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        #排序 nums
        nums.sort()
        # 雙指針
        left, right = 0, 1

        # 用右指針遍歷
        while right < len(nums):
            if nums[right] != nums[left]:
                # left 要先加 1 才能把下一位變成 unique
                left += 1
                # 把 unique 的值放到前面
                nums[left] = nums[right]
            right += 1
        return left +1 
         
