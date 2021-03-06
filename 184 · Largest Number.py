from functools import cmp_to_key
class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        # write your code here
        # 利用兩兩比大小做排序
        nums.sort(key = cmp_to_key(lambda x, y: 1 if str(x)+str(y) < str(y)+str(x) else -1))
        if nums[0] == 0:
            return '0'
        return "".join([str(x) for x in nums])
