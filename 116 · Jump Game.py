class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        l = len(A) #Ａ的長度
        dp = [1] + [0] * (l-1) #用來記錄是否可以到達的 list
        for i in range(l):
            if dp[i] == 0:
                continue #0的話不會前進
            for j in range(A[i]): #當前數字左邊的下標
                if i + j + 1 < l:
                    dp[i + j + 1] = 1
        return dp[-1] == 1 #看最後一個數字是否可以到達
