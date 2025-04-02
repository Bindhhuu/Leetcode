from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        can1, can2, count1, count2 = None, None, 0, 0
        
        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
            elif count1 == 0:
                can1, count1 = num, 1
            elif count2 == 0:
                can2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
    
        count1, count2 = 0, 0
        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
        
        threshold = len(nums) // 3
        return [x for x, c in [(can1, count1), (can2, count2)] if c > threshold]
