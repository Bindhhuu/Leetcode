class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        maxx = 0

        curr_sum = sum(cardPoints[:k])
        maxx = curr_sum

        for i in range(1, k+1):
            left = cardPoints[k-i]
            right = cardPoints[-i]
            curr_sum = curr_sum - left + right
            maxx = max(maxx, curr_sum)
        
        return maxx

#TC = O(k)
#SC = O(1)
