class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1   
        r = max(nums)  

        def helper(j):
            x = 0
            for i in nums:
                x += math.ceil(i/j)
            return x

        while l < r:
            mid = (l+r)//2

            if helper(mid) <= threshold:
                r = mid
            else:
                l = mid+1        
        return l
