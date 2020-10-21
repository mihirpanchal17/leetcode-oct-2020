class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[1])
        print(points)
        count = 0
        end = -float('inf')
        for balloon in points:
            if balloon[0] > end:
                count += 1
                end = balloon[1]
                
        return count