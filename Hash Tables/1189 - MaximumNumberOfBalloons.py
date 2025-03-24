class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        counter = defaultdict(int)
        word = 'balloon'

        for i in text:
            if i in word:
                counter[i] +=1
        
        if any(i not in counter for i in word):
            return 0
        else:
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])
