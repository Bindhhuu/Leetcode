class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, sol, total):
            if len(sol) == k:
                if total == n:
                    res.append(sol[:])
                return

            for i in range(start, 10):
                if total+i > n:
                    break

                sol.append(i)
                backtrack(i+1, sol, total+i)
                sol.pop()

        backtrack(1, [], 0)
        return res
