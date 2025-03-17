class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        count = 0

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    count += 1
                    i +=1
                    j += 1
                    
                else:
                    return 0
        return count
