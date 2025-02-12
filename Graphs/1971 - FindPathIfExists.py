# Recursive DFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        seen.add(source)

        def dfs(i):
            if i == destination:
                return True
            for n in graph[i]:
                if n not in seen:
                    seen.add(n)
                    if dfs(n):
                        return True
            
            return False
        
        return dfs(source)
