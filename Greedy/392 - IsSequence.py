class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if s == '': return True
        if n > m: return False

        j = 0
        for i in range(m):
            if t[i] == s[j]:
                if j == n - 1: 
                    return True
                j +=1
        return False
        
        
