class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_len = float('inf')
        sums = 0
        n = len(nums)

        for r in range(n):
            sums += nums[r]
            while sums >= target:
                min_len = min(min_len, r-l+1)
                sums -= nums[l]
                l += 1
        
        if min_len < float('inf'):
            return min_len
        else:
            return 0
