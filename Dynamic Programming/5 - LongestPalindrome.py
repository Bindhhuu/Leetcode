class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # return the valid palindrome substring

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes (centered on one char)
            odd = expandAroundCenter(i, i)
            # Even length palindromes (centered between two chars)
            even = expandAroundCenter(i, i+1)

            # Pick the longer one from current center
            current_longest = odd if len(odd) > len(even) else even

            # Update result
            if len(current_longest) > len(longest):
                longest = current_longest

        return longest
