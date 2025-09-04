class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(s.split()[::-1])
        # or
        n = len(s)
        word = []
        i = 0

        while i < n:
            while i < n and s[i] == " ":
                i += 1
            if i >= n:
                break
            start = i
            while i < n and s[i] != " ":
                i += 1
            end = s[start:i]
            word.append(end)

        l, r = 0, len(word) - 1
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1

        res = ""
        for idx, end in enumerate(word):
            if idx > 0:
                res += " "
            res += end

        return res
