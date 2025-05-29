class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_chars = sorted(s, key=lambda c: (-freq[c], c))
        return ''.join(sorted_chars)
