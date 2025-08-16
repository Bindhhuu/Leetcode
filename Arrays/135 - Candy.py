class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        count = [1] * len(ratings)

        for i in range(n):
            if ratings[i] > ratings[i-1]:
                count[i] = count[i-1] + 1
        
        for i in range(n-2):
            if ratings[i] > ratings[i+1]:
                count[i] = max(count[i], count[i+1] + 1)
        
        return sum(count)
