class Solution:
    """
    @param nums: a integer array
    @param target: 
    @return: return a integer
    """
    def KDifference(self, nums, target):
        # write your code here
        count = 0
        s = set()
        for num in nums:
            if (num - target) in s:
                count += 1
            if (num + target) in s:
                count += 1
            
            s.add(num)
        return count
