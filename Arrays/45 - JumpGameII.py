class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        far = 0
        curr = 0

        for i in range(len(nums)-2):
            far = max(far, i + nums[i])
            
        if i == curr:
            jumps += 1
            curr = far
        return jumps
