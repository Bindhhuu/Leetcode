from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  
        for i, num in enumerate(nums):
            if i > max_reach:  
                return False
            max_reach = max(max_reach, i + num)  
            if max_reach >= len(nums) - 1:  
                return True
        return False

#better approach
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n-1

        for i in range(n-1, -1, -1):
            maxx = nums[i]
            if i+maxx >=target:
                target = i
        
        return target == 0
