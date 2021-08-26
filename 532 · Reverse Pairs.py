class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        # write your code here
        tmp = [0] * len(A)
        # 紀錄 revers pairs 有幾個
        self.count = 0
        self.mergeSort(A, 0, len(A)-1, tmp)
        return self.count

    def mergeSort(self, nums, start, end, tmp):
        # edge case 
        if start >= end: return
        # 分治
        mid = start+(end-start)//2
        self.mergeSort(nums, start, mid, tmp)
        self.mergeSort(nums, mid+1, end, tmp)
        self.merge(nums, start, end, tmp)

    def merge(self, A, start, end, tmp):
        mid = start+(end-start)//2
        # 需要在前後段遍歷，所以需要 i 和 j 去看 前段的值是否會大於後段的值
        i = start
        j = mid+1
        index = start
        while i <= mid and j <= end:
            if A[i] > A[j]:
                # 表示 reverse pair
                # tmp 就是要去 sort 數組，所以要把小的值放前面
                tmp[index] = A[j]
                self.count += mid+1-i
                j += 1
            else:
                tmp[index] = A[i]
                i += 1
            index += 1
        while i <= mid:
            tmp[index] = A[i]
            i += 1
            index += 1
        while j <= end:
            tmp[index] = A[j]
            j += 1
            index += 1
        
        # 放回原數組
        for i in range(start, end+1):
            A[i] = tmp[i]
