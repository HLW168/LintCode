class Solution:
    """
    @param secret: An string
    @param guess: An string
    @return: An string
    """
    def getHint(self, secret, guess):
        # write your code here
        a, b, n = 0, 0, len(secret)
        # 利用 數組 來記錄出現過的紀錄
        ds = [0 for i in range(10)]
        dg = [0 for i in range(10)]

        #遍歷 Secret 來找出數字和位置相同的 (a)
        for i in range(n):
            x = ord(secret[i]) - ord('0') # 轉換成數字
            y = ord(guess[i]) - ord('0')
            if x == y: #數字和位置相同的情況
                a += 1
            # 數組紀錄出現過的次數
            ds[x] += 1
            dg[y] += 1
           
        # 遍歷數字10，來找出相同數字，其中可能包含相同位置
        for i in range(10):
            b += min(ds[i], dg[i])
        
        return str(a) + 'A' + str(b-a) + 'B'
