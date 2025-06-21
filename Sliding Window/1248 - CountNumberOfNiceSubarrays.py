from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1

        for r in nums:
            if r % 2 == 1:
                prefix += 1
            count += freq[prefix- k]
            freq[prefix] += 1

        return count
        
