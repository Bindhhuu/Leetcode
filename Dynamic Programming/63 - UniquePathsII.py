class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 1:
            return
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]== 1:
                    dp[i][j] = 0
                elif not(i == 0 and j ==0):
                    up = dp[i-1][j] if i > 0 else 0
                    down = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = up + down
        
        return dp[m-1][n-1]
