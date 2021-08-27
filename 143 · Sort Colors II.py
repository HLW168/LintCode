class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.sortNColors(colors, 0, len(colors)-1, 1, k)

 #把数组一分为二，直到分成的数组只有1种颜色， 或者数组的开头 >= 数组的结尾，然后用partition 的方式分成<= k 和 >k 两边，然后一直做
    def sortNColors(self, colors, start, end, colorFrom, colorTo):
        # 出口條件
        if colorFrom == colorTo:
            return
        if start >= end:
            return
        
        # 找 pivot
        colorMid = (colorFrom + colorTo) // 2
        # 設 left 和 right 來區隔
        left = start
        right = end

        while left <= right:
            if colors[left] <= colorMid:
                # 不需要排序的情況
                left += 1
                continue
            if colors[right] > colorMid:
                # 不需要排序的情況
                right -= 1
                continue
            
            #需要排序的情況，就交換
            colors[left], colors[right] = colors[right], colors[left]
            left += 1
            right -= 1

        self.sortNColors(colors, start, right, colorFrom, colorMid)
        self.sortNColors(colors, left, end, colorMid+1, colorTo)

            
