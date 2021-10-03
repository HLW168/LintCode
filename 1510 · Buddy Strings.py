class Solution:
    """
    @param A: string A
    @param B: string B
    @return: bool
    """
    def buddyStrings(self, A, B):
        # Write your code here
        # 長度不同一定是 false
        if len(A) != len(B):
            return False
        # AB 一樣 且有重複的字符
        if A == B and len(A) > len(set(A)):
            return True
        
        a_pointer = 0
        b_pointer = 0
        # 紀錄 AB 中不一樣的字符
        diff = []

        while a_pointer < len(A) and b_pointer < len(B):
            while a_pointer < len(A) and b_pointer < len(B) and A[a_pointer] == B[b_pointer]:
                a_pointer += 1
                b_pointer += 1

            if a_pointer < len(A):
                # 紀錄不一樣的位置
                diff.append(a_pointer)
                
            a_pointer += 1
            b_pointer += 1

                # 沒有兩個不同的字符
        if len(diff) != 2:
            return False
        # 確認是否能調換
        elif A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
            return True
            
        return False
