
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        sol = 0
        res = 0
        count = {'a': 0, 'b': 0, 'c': 0}

        for i in range(len(s)):
            count[s[i]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                res += len(s) - i
                count[s[sol]] -= 1
                sol += 1

        return res

  #TC: O(n)
  #SC: O(1)
