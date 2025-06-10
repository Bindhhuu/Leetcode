class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        great = {}
        stack = []

        for i in nums2:
            while stack and i > stack[-1]:
                prev = stack.pop()
                great[prev] = i
            stack.append(i)
        
        for i in stack:
            great[i] = -1
        
        return [great[i] for i in nums1]
