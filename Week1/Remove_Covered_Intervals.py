class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        count = right = 0
        intervals.sort(key=lambda a: (a[0],-a[1]))
        
        for start,end in intervals:
            count += end > right
            right = max(right,end)
        return count