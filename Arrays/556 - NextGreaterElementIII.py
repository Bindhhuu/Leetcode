class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digit = list(str(n))
        i = len(digit) - 2

        while i >= 0 and digit[i] >= digit[i+1]:
            i -= 1

        if i == -1:
            return -1
        
        j = len(digit) -1
        while digit[j] <= digit[i]:
            j -= 1
        
        digit[i], digit[j] = digit[j], digit[i]
        digit[i+1:] = reversed(digit[i+1:])

        result = int("".join(digit))
        return result if result < 2 ** 31 else -1
