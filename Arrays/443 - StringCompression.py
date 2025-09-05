class Solution:
    def compress(self, chars: List[str]) -> int:
        w = 0
        r = 0

        while r < len(chars):
            ch = chars[r]
            count = 0

            while r < len(chars) and chars[r] == ch:
                r += 1
                count += 1

            chars[w] = ch
            w += 1

            if count > 1:
                for c in str(count):
                    chars[w] = c
                    w += 1

          return w
