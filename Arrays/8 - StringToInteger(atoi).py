class Solution:
    def myAtoi(self, s: str) -> int:
        maxx = 2**31
        minn = 2**31-1
        i = 0
        result = 0
        sign = 1
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

            if sign == 1 and (s[i] == '-' or s[i] == '+'):
                if s[i] == '-':
                    sign = -1
                else:
                    sign = 1
                i += 1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if result > (maxx - digit) // 10:
                return maxx if sign == 1 else minn
            result = result * 10 + digit
            i += 1
        return sign * result    


