class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen = set(jewels)
        count = 0
        
        for i in stones:
            if i in seen:
                count += 1

        return count
