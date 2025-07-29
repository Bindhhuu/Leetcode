class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []

        if not nums1 or not nums2 or k == 0:
            return result

        heap = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(result) < k:
            current_sum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                new_sum = nums1[i] + nums2[j + 1]
                heapq.heappush(heap, (new_sum, i, j + 1))

        return result
            
