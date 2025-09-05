import heapq
from sortedcontainers import SortedList  # optional for ordered available servers

class Solution:
    def busiestServers(self, k, arrival, load):
        from sortedcontainers import SortedList
        
        n = len(arrival)
        count = [0] * k
        busy = []  # min-heap: (end_time, server_id)
        available = SortedList(range(k))
        
        for i in range(n):
            t = arrival[i]
            # free servers that have finished
            while busy and busy[0][0] <= t:
                _, s = heapq.heappop(busy)
                available.add(s)
            
            if not available:
                continue  # drop request
            
            # find server >= i % k
            idx = available.bisect_left(i % k)
            if idx == len(available):
                idx = 0  # wrap around
            
            server = available.pop(idx)
            count[server] += 1
            heapq.heappush(busy, (t + load[i], server))
        
        mx = max(count)
        return [i for i, c in enumerate(count) if c == mx]
