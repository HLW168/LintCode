class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prefix = {}
        prefix[0] = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum in prefix:
                return [prefix[prefix_sum], i]
            prefix[prefix_sum] = i + 1
        return [-1, -1]
