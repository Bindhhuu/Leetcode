class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        count = 1
        pos = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > pos:
                count += 1
                pos = points[i][1]
        
        return count
