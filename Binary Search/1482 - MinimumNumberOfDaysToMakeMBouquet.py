class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        l = min(bloomDay)
        r = max(bloomDay)

        if (m * k) > len(bloomDay):
                return -1
        
        def helper(ans):
            counter, bouquet = 0, 0
            for i in bloomDay:
                if i <= ans:
                    counter += 1
                    if counter == k:
                        bouquet += 1
                        counter = 0

                else:
                    counter = 0
            return bouquet >= m
        
        ans = -1 
        while l < r:
            mid = (l+r)//2
            if helper(mid):
                r = mid

            else:
                l = mid + 1
  
        return l


        
