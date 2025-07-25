class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (A,B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1.0/value
        
        def dfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            queue = deque([(start, 1.0)])
            seen = {start}
            while queue:
                node, prod = queue.popleft()
                if node == end:
                    return prod
                for nei, w in graph[node].items():
                    if nei not in seen:
                        seen.add(nei)
                        queue.append((nei, prod*w))
            return -1.0
        return [dfs(c, d) for c, d in queries]
