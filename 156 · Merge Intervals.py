"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if not intervals: return []

        # 排序
        intervals = sorted(intervals, key=lambda interval:interval.start)

        # 定義 last 和 output
        last, output = None, []

        # 遍歷 intervals
        for interval in intervals:
            if not last or last.end < interval.start:
                output.append(interval)
                last = interval
            else:
                # 看尾巴到哪裡
                last.end = max(last.end, interval.end)   
        
        return output
