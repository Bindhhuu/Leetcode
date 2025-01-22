class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L =0
        R = len(nums)-1

        while L <=R:
            M = L+ ((R-L)//2)

            if nums[M] == target:
                return M

            elif nums[M] < target:
               L= M+1
            
            else:
                R= M-1

        if nums[M] < target:
            return M+1
        else:
            return M
