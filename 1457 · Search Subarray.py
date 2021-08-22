class Solution:
    """
    @param arr: The array 
    @param k: the sum 
    @return: The length of the array
    """
    def searchSubarray(self, arr, k):
        # Write your code here
        # 利用前綴和求 array
        d = dict()
        d[0] = 0
        prefixSum = 0
        for i in range(len(arr)):
            prefixSum += arr[i]
            if (prefixSum - k) in d:
                return i + 1 - d[prefixSum-k]
            if prefixSum not in d:
                d[prefixSum] = i + 1 # 紀錄位置
        return -1
