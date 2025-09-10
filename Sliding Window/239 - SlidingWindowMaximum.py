from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        list = [] 
        dq = deque()
        for i in range(len(nums)):
            if dq and dq[0] <= i-k:
                dq.popleft()

            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            if i >= k-1:
                list.append(nums[dq[0]])

        return list

        
