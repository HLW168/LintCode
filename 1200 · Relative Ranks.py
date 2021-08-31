class Solution:
    """
    @param nums: List[int]
    @return: return List[str]
    """
    def findRelativeRanks(self, nums):
        # write your code here
        score = {}
        for i in range(len(nums)):
            score[nums[i]] = i
        sortedScore = sorted(nums, reverse=True)
        ans = [0] * len(nums)

        for i in range(len(sortedScore)):
            res = str(i+1)
            if i == 0:
                res = 'Gold Medal'
            if i == 1:
                res = 'Silver Medal'
            if i == 2:
                res = 'Bronze Medal'
            ans[score[sortedScore[i]]] = res

        return ans

        return ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
