class Solution:
    def subarraySumClosest(self, nums):
        pre = [0] * (len(nums) + 1)
        for i in range(len(nums)):
          pre [i + 1] = pre[i] + nums[i]
        sort_pre = sorted(pre)
        print(sort_pre)
        min_diff = float("inf")
        sum1, sum2 = 0, 0
        a, b= 0, 0

        for i in range(1, len(sort_pre)):
          diff = sort_pre [i] - sort_pre [i - 1]
          if abs(diff) < min_diff:
            sum1, sum2, min_diff = sort_pre[i - 1], sort_pre[i], abs(diff)
            print(sum1, sum2, min_diff)
        for i in range(len(pre)):
          if sum1 == pre[i]:
            a = i
            print(a)
            break
        for i in range(len(pre) - 1, -1, -1):
          if sum2 == pre[i]:
            b = i
            print(b)
            break

        return [min(a, b), max(a, b) - 1]
