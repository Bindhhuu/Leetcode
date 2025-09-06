class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        sq = []
        i = 1

        while i*i <= n:
            sq.append(i*i)
            i += 1

        for i in range(1, n+1):
            for s in sq:
                if s > i:
                    break
                dp[i] = min(dp[i], 1+dp[i-s])
        return dp[n]
