class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        sortedNums = sorted(nums, reverse=True)
        print(sortedNums)
        for i in range(1, len(sortedNums)):           
            if sortedNums[i] == sortedNums[i-1]:
                return sortedNums[i]
            else:
                break       
        return sortedNums[i]
