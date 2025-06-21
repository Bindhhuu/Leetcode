from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1

        for r in range(len(nums)):
            prefix += nums[r]
            count += freq[prefix - goal]
            freq[prefix] += 1
        
        return count
