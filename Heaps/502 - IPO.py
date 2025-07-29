class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proj = list(zip(capital, profits))
        proj.sort()
        i = 0
        max_heap = []

        for _ in range(k):
            while i < len(proj) and proj[i][0] <= w:
                heapq.heappush(max_heap, -proj[i][1])
                i += 1
        
            if not max_heap:
                break
        
            w += -heapq.heappop(max_heap)

        return w
